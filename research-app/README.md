# 📁 Scheme Research Assistant

An intelligent web application designed to simplify the process of understanding complex government schemes. Using advanced AI techniques through LangChain and Google Gemini's powerful language models, this application reads, processes, and synthesizes information from scheme URLs into an interactive knowledge base.

## 🌟 Features

- **URL-based Analysis**: Simply provide URLs of government scheme articles
- **AI-Powered Q&A**: Ask specific questions and get accurate answers from the sources
- **Source Tracking**: See exactly which documents your answers come from
- **Persistent Knowledge Base**: ChromaDB vector storage for efficient retrieval
- **User-Friendly Interface**: Clean Streamlit interface for easy interaction

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: LangChain, Google Gemini AI (gemini-pro, embedding-001)
- **Vector Database**: ChromaDB
- **Web Scraping**: BeautifulSoup4, Requests
- **Language**: Python 3.8+

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))
- Internet connection for fetching URLs and API calls

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd research-app
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Gemini API key
# GEMINI_API_KEY=your_actual_api_key_here
```

### 5. Test Your Setup (Optional)

```bash
# Test API key configuration
python test_key.py

# Test internet connection
python test_connection.py
```

### 6. Run the Application

```bash
streamlit run main.py
```

The application will open in your default browser at `http://localhost:8501`

## 📖 How to Use

1. **Enter URLs**: In the sidebar, paste URLs of government scheme articles (one per line)
2. **Analyze**: Click the "🚀 Analyze URLs" button to process the content
3. **Ask Questions**: Once processed, type your questions in the main area
4. **View Answers**: Get AI-generated answers with source references

### Example Questions

- "What are the eligibility criteria?"
- "What benefits does this scheme provide?"
- "How can I apply for this scheme?"
- "What documents are required?"

## 🗂️ Project Structure

```
research-app/
├── main.py              # Main Streamlit application
├── utils.py             # Utility functions (fetching, chunking, indexing)
├── requirements.txt     # Python dependencies
├── vercel.json         # Vercel deployment configuration
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore rules
├── test_key.py         # API key validation script
├── test_connection.py  # Network connectivity test
└── README.md           # This file
```

## 🔧 Configuration

### Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key (required)

### ChromaDB Storage

The application stores vector embeddings in `./chroma_db_store/` directory. This allows for persistent storage across sessions.

## 🚢 Deployment

### Deploy to Vercel

1. Install Vercel CLI: `npm i -g vercel`
2. Set environment variable in Vercel dashboard: `GEMINI_API_KEY`
3. Deploy: `vercel --prod`

The `vercel.json` configuration is already set up for Python deployment.

## 🐛 Troubleshooting

### API Key Issues
- Ensure your `.env` file exists and contains a valid `GEMINI_API_KEY`
- Run `python test_key.py` to verify

### Connection Issues
- Check your internet connection
- Run `python test_connection.py` to verify
- Some networks may block certain URLs

### SSL Certificate Errors
- The app uses `verify=False` for requests to bypass SSL issues
- This is configured in `utils.py`

### No Results Found
- Ensure URLs are accessible and contain text content
- Try with different URLs
- Check that the URLs are not behind authentication

## 📝 Notes

- The application uses `nest_asyncio` to handle async operations in Streamlit
- SSL verification is disabled for web scraping to handle certificate issues
- The vector database persists between sessions in `./chroma_db_store/`

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Google Gemini AI for powerful language models
- LangChain for the AI framework
- Streamlit for the web interface
- ChromaDB for vector storage
