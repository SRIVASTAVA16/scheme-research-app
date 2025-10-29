# 🚀 DEPLOY YOUR APP NOW - Quick Start Guide

## ⚠️ IMPORTANT: Why Vercel Won't Work

Your app is built with **Streamlit**, which requires:
- Persistent WebSocket connections
- Long-running server processes
- Stateful sessions

**Vercel only supports serverless functions** (Flask, FastAPI, Next.js), so Streamlit apps **cannot run on Vercel**.

---

## ✅ SOLUTION: Deploy to Streamlit Cloud (100% FREE)

Streamlit Cloud is the official hosting platform - it's **free, fast, and made for Streamlit apps**.

### 🎯 3-Step Deployment Process

#### STEP 1: Push to GitHub

```bash
# Navigate to your project
cd /vercel/sandbox/research-app

# Initialize git (if not already done)
git init
git branch -M main

# Add all files
git add .

# Commit
git commit -m "Initial commit - Scheme Research Assistant"

# Create a new repository on GitHub at: https://github.com/new
# Then connect and push:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

#### STEP 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**: https://share.streamlit.io/
2. **Sign in** with your GitHub account
3. **Click "New app"**
4. **Fill in the form**:
   - Repository: `YOUR_USERNAME/YOUR_REPO_NAME`
   - Branch: `main`
   - Main file path: `main.py`
5. **Click "Deploy"**

#### STEP 3: Add Your API Key

1. In Streamlit Cloud dashboard, click on your app
2. Go to **Settings** (⚙️) → **Secrets**
3. Add this in TOML format:

```toml
GEMINI_API_KEY = "your_actual_gemini_api_key_here"
```

4. Click **Save**

---

## 🎉 YOUR APP IS LIVE!

Your app will be available at:
```
https://YOUR_USERNAME-YOUR_REPO_NAME.streamlit.app
```

Example: `https://johndoe-scheme-research.streamlit.app`

---

## 🔑 Get Your Gemini API Key

If you don't have one yet:
1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with Google
3. Click "Create API Key"
4. Copy and use it in Streamlit Cloud secrets

---

## 🏠 Run Locally (For Testing)

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GEMINI_API_KEY=your_key_here" > .env

# Run the app
streamlit run main.py
```

Opens at: `http://localhost:8501`

---

## 🆘 Troubleshooting

### "Module not found" error
- Make sure all dependencies are in `requirements.txt`
- Redeploy the app

### "API key not found" error
- Check that you added `GEMINI_API_KEY` in Streamlit Cloud secrets
- Make sure there are no extra spaces or quotes

### App won't start
- Check the logs in Streamlit Cloud dashboard
- Verify your GitHub repository has all files

---

## 📊 Alternative Platforms (If You Want Options)

| Platform | URL | Free Tier | Setup Time |
|----------|-----|-----------|------------|
| **Streamlit Cloud** ⭐ | https://share.streamlit.io | ✅ Unlimited | 5 min |
| Render | https://render.com | ✅ Limited | 10 min |
| Hugging Face Spaces | https://huggingface.co/spaces | ✅ Unlimited | 10 min |
| Railway | https://railway.app | ✅ $5/month | 10 min |

**Recommendation**: Use Streamlit Cloud - it's the easiest and best option.

---

## ✨ Features of Your Deployed App

Once live, users can:
- ✅ Paste government scheme URLs
- ✅ Get AI-powered analysis
- ✅ Ask questions about schemes
- ✅ View source references
- ✅ Access from anywhere with internet

---

## 🎯 Quick Checklist

- [ ] Code pushed to GitHub
- [ ] Streamlit Cloud account created
- [ ] App deployed from GitHub repo
- [ ] `GEMINI_API_KEY` added to secrets
- [ ] App is accessible via live URL
- [ ] Tested with sample scheme URLs

---

## 📞 Need More Help?

- **Streamlit Docs**: https://docs.streamlit.io/streamlit-community-cloud
- **Deployment Guide**: See `DEPLOYMENT_GUIDE.md` for detailed instructions
- **Community Forum**: https://discuss.streamlit.io/

---

**Ready to deploy? Follow the 3 steps above! 🚀**
