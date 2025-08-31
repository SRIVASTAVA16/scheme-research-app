import os
import requests
from bs4 import BeautifulSoup
import warnings
from dotenv import load_dotenv

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain_core.documents import Document

# This line loads the environment variables from the .env file for local development
load_dotenv()

# Suppress only the InsecureRequestWarning from urllib3
warnings.filterwarnings('ignore', category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Vercel will get this from the Environment Variables you set
# Locally, load_dotenv() will get it from your .env file
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found. Please create a .env file locally or set it in your Vercel project settings.")

def fetch_scheme_pages_robust(url_list):
    """
    A more reliable function to fetch content from URLs using the requests library.
    """
    all_docs = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    for url in url_list:
        try:
            # Added verify=False to bypass SSL certificate errors
            response = requests.get(url, headers=headers, timeout=10, verify=False)
            response.raise_for_status()  # Raise an error for bad status codes

            soup = BeautifulSoup(response.content, 'html.parser')
            for script_or_style in soup(['script', 'style']):
                script_or_style.decompose()
            
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            clean_text = '\n'.join(line for line in lines if line)

            if clean_text:
                doc = Document(page_content=clean_text, metadata={"source": url})
                all_docs.append(doc)
        except requests.RequestException as e:
            print(f"Warning: Could not fetch URL {url} due to error: {e}")
            continue

    if not all_docs:
        raise ValueError("No valid content could be fetched from any of the provided URLs.")
    
    return all_docs

def divide_into_chunks(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)
    if not chunks:
        raise ValueError("Failed to create text chunks from the documents.")
    return chunks

def get_gemini_embeddings():
    """Initializes and returns the Gemini embeddings model."""
    return GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=gemini_api_key
    )

def build_vector_index(chunks):
    embeddings = get_gemini_embeddings()
    try:
        index = FAISS.from_documents(chunks, embeddings)
        index.save_local("faiss_index_store")
    except Exception as e:
        raise RuntimeError(f"FAISS vector index creation failed: {e}")
    return index

def load_saved_index():
    if not os.path.exists("faiss_index_store"):
        return None
    embeddings = get_gemini_embeddings()
    return FAISS.load_local("faiss_index_store", embeddings, allow_dangerous_deserialization=True)

def respond_to_question(query, index):
    docs = index.similarity_search(query)
    if not docs:
        return "No relevant information was found to answer your question.", []
    
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0, google_api_key=gemini_api_key)
    chain = load_qa_chain(llm, chain_type="stuff")
    try:
        # Using invoke for the latest LangChain compatibility
        result = chain.invoke({"input_documents": docs, "question": query}, return_only_outputs=True)
        return result['output_text'], docs
    except Exception as e:
        return f"Error generating response from LLM: {e}", docs

