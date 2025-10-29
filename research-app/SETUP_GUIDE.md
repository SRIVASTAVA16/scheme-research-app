# 🚀 Complete Setup Guide

This guide will walk you through setting up the Scheme Research Assistant from scratch.

## Prerequisites Checklist

Before you begin, ensure you have:

- [ ] Python 3.8 or higher installed
- [ ] Internet connection
- [ ] Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))
- [ ] Terminal/Command Prompt access

## Quick Setup (Recommended)

### For Linux/Mac Users

```bash
# Run the automated setup script
./setup.sh
```

### For Windows Users

```cmd
# Run the automated setup script
setup.bat
```

The script will:
1. Check Python installation
2. Create a virtual environment
3. Install all dependencies
4. Create a `.env` file from template

After running the script, **edit the `.env` file** and add your actual Gemini API key.

## Manual Setup

If you prefer to set up manually or the automated script doesn't work:

### Step 1: Verify Python Installation

```bash
python3 --version
# Should show Python 3.8 or higher
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install:
- streamlit
- langchain-core
- langchain-community
- langchain-google-genai
- chromadb
- requests
- beautifulsoup4
- python-dotenv
- nest-asyncio

### Step 4: Configure Environment

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your favorite editor
nano .env  # or vim, code, notepad, etc.
```

Add your Gemini API key:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### Step 5: Test Your Setup

```bash
# Test API key
python test_key.py

# Test internet connection
python test_connection.py
```

Both tests should pass with ✅ SUCCESS messages.

### Step 6: Run the Application

```bash
streamlit run main.py
```

The app will open at `http://localhost:8501`

## Troubleshooting

### Issue: "pip: command not found"

**Solution**: Use `python3 -m pip` instead of `pip`:
```bash
python3 -m pip install -r requirements.txt
```

### Issue: "Permission denied" when running setup.sh

**Solution**: Make the script executable:
```bash
chmod +x setup.sh
./setup.sh
```

### Issue: Virtual environment not activating

**Linux/Mac Solution**:
```bash
source venv/bin/activate
```

**Windows Solution**:
```cmd
venv\Scripts\activate.bat
```

### Issue: "GEMINI_API_KEY not found"

**Solution**: 
1. Ensure `.env` file exists in the project root
2. Check that it contains: `GEMINI_API_KEY=your_key_here`
3. No spaces around the `=` sign
4. No quotes around the key

### Issue: SSL Certificate errors

The app is configured to handle SSL issues automatically with `verify=False` in requests. If you still face issues, check your network/firewall settings.

### Issue: "No module named 'streamlit'"

**Solution**: Ensure virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: ChromaDB errors

**Solution**: Delete the existing database and rebuild:
```bash
rm -rf chroma_db_store/
# Then restart the app and re-analyze URLs
```

## Getting Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key
5. Paste it in your `.env` file

**Note**: Keep your API key secret! Never commit it to version control.

## Verifying Installation

Run these commands to verify everything is set up correctly:

```bash
# Check Python version
python3 --version

# Check if virtual environment is active
which python  # Should point to venv/bin/python

# Check installed packages
pip list

# Test API key
python test_key.py

# Test connection
python test_connection.py
```

All checks should pass before running the main application.

## Running the Application

Once setup is complete:

```bash
# 1. Activate virtual environment (if not already active)
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# 2. Run the app
streamlit run main.py
```

The application will:
- Start a local web server
- Open your default browser
- Display the Scheme Research Assistant interface

## Using the Application

1. **Enter URLs**: Paste government scheme URLs in the sidebar (one per line)
2. **Click "Analyze URLs"**: Wait for processing to complete
3. **Ask Questions**: Type questions about the schemes
4. **View Answers**: Get AI-generated responses with sources

## Stopping the Application

Press `Ctrl+C` in the terminal to stop the Streamlit server.

## Deactivating Virtual Environment

When you're done:
```bash
deactivate
```

## Next Steps

- Read the main [README.md](README.md) for more details
- Check out the code in `main.py` and `utils.py`
- Explore deployment options (Vercel, Heroku, etc.)

## Need Help?

If you encounter issues not covered here:
1. Check the error message carefully
2. Ensure all prerequisites are met
3. Try the manual setup process
4. Check that your API key is valid and has quota remaining

## Project Structure Reference

```
research-app/
├── main.py              # Main Streamlit app
├── utils.py             # Helper functions
├── requirements.txt     # Python dependencies
├── .env.example         # Environment template
├── .env                 # Your actual config (create this)
├── setup.sh             # Linux/Mac setup script
├── setup.bat            # Windows setup script
├── test_key.py          # API key test
├── test_connection.py   # Network test
├── README.md            # Project overview
├── SETUP_GUIDE.md       # This file
└── vercel.json          # Deployment config
```

Happy researching! 🎉
