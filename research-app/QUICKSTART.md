# ⚡ Quick Start Guide

Get up and running in 5 minutes!

## 🎯 TL;DR

```bash
# 1. Run setup script
./setup.sh  # Linux/Mac
# OR
setup.bat   # Windows

# 2. Add your API key to .env file
# GEMINI_API_KEY=your_key_here

# 3. Activate virtual environment
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows

# 4. Run the app
streamlit run main.py
```

## 📝 Step-by-Step

### 1️⃣ Get API Key (2 minutes)
- Go to https://makersuite.google.com/app/apikey
- Sign in and create an API key
- Copy it

### 2️⃣ Setup Project (2 minutes)
```bash
# Automated setup
./setup.sh  # or setup.bat on Windows
```

### 3️⃣ Configure (30 seconds)
Edit `.env` file:
```
GEMINI_API_KEY=paste_your_key_here
```

### 4️⃣ Run (30 seconds)
```bash
source venv/bin/activate  # Activate environment
streamlit run main.py      # Start app
```

## 🎮 Using the App

1. **Paste URLs** in sidebar (government scheme articles)
2. **Click "Analyze URLs"** button
3. **Ask questions** like:
   - "What are the eligibility criteria?"
   - "How do I apply?"
   - "What documents are needed?"

## ✅ Verify Setup

```bash
python test_key.py         # Should show SUCCESS
python test_connection.py  # Should show SUCCESS
```

## 🆘 Common Issues

| Problem | Solution |
|---------|----------|
| `pip not found` | Use `python3 -m pip install -r requirements.txt` |
| `Permission denied` | Run `chmod +x setup.sh` |
| `API key not found` | Check `.env` file exists and has correct format |
| `Module not found` | Activate virtual environment first |

## 📚 More Help

- Detailed setup: See [SETUP_GUIDE.md](SETUP_GUIDE.md)
- Project info: See [README.md](README.md)

---

**That's it!** You're ready to analyze government schemes with AI. 🚀
