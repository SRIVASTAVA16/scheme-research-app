import nest_asyncio
nest_asyncio.apply()
import streamlit as st
from utils import (
    fetch_scheme_pages_robust, # Using the new function
    divide_into_chunks,
    build_vector_index, 
    load_saved_index,
    respond_to_question
)
# Triggering a new build
st.set_page_config(page_title="📁 Scheme Research Assistant", layout="centered")
st.title("📁 Scheme Research Assistant")

if 'index_db' not in st.session_state:
    st.session_state.index_db = load_saved_index()

st.sidebar.header("🔗 Input Panel")
url_input = st.sidebar.text_area(
    "Paste scheme article URLs (one per line):", 
    height=150,
    help="Enter one full URL per line. E.g., https://pib.gov.in/..."
)
process_button = st.sidebar.button("🚀 Analyze URLs")

if process_button:
    st.session_state.index_db = None 
    urls = [url.strip() for url in url_input.split("\n") if url.strip()]
    
    if not urls:
        st.error("Please enter at least one URL to proceed.")
    else:
        try:
            with st.spinner("🔄 Fetching content from the web..."):
                docs = fetch_scheme_pages_robust(urls) # Calling the new function
                st.success(f"✅ Retrieved {len(docs)} documents")

            with st.spinner("📃 Breaking text into manageable pieces..."):
                text_fragments = divide_into_chunks(docs)
                st.success(f"✅ Divided into {len(text_fragments)} text chunks")

            with st.spinner("🧠 Building knowledge base..."):
                st.session_state.index_db = build_vector_index(text_fragments)
                st.success("✅ Knowledge base built successfully!")
        
        except Exception as e:
            st.error(f"❌ An error occurred during processing: {e}")
            st.session_state.index_db = None

if st.session_state.index_db:
    st.markdown("---")
    st.subheader("🔍 Ask a Question")
    user_question = st.text_input("Type your query about the scheme(s) here:")

    if user_question:
        with st.spinner("💡 Thinking..."):
            try:
                result, docs = respond_to_question(user_question, st.session_state.index_db)
                st.markdown("#### Answer")
                st.write(result)

                st.markdown("---")
                with st.expander("📄 See Sources"):
                    for doc in docs:
                        source_url = doc.metadata.get('source', 'Unknown source')
                        st.markdown(f"**Source:** `{source_url}`")
                        # Display a snippet of the page content
                        st.text(f"Content: {doc.page_content[:300].strip()}...")

            except Exception as e:
                st.error(f"❌ Failed to generate response: {e}")
else:
    st.info("Please analyze URLs in the sidebar to build a knowledge base before asking questions.")