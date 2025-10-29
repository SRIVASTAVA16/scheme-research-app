# 🎯 START HERE - Deploy Your App in 5 Minutes

## ⚡ Quick Facts

- ❌ **Vercel won't work** (it doesn't support Streamlit apps)
- ✅ **Use Streamlit Cloud** (free, official, perfect for your app)
- ⏱️ **Time needed**: 5-10 minutes
- 💰 **Cost**: $0 (completely free)

---

## 🚀 3 Simple Steps

### STEP 1️⃣: Push to GitHub (2 minutes)

Open your terminal and run:

```bash
cd /vercel/sandbox/research-app

# Initialize git
git init
git branch -M main

# Add and commit files
git add .
git commit -m "Deploy Scheme Research Assistant"

# Create a new repo on GitHub: https://github.com/new
# Name it something like: scheme-research-app

# Connect and push (replace YOUR_USERNAME and YOUR_REPO)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

✅ **Done!** Your code is now on GitHub.

---

### STEP 2️⃣: Deploy to Streamlit Cloud (2 minutes)

1. **Go to**: https://share.streamlit.io/
2. **Sign in** with your GitHub account
3. **Click** "New app" button
4. **Fill in**:
   - Repository: Select your repo from dropdown
   - Branch: `main`
   - Main file path: `main.py`
5. **Click** "Deploy"

⏳ Wait 1-2 minutes while it deploys...

✅ **Done!** Your app is now live!

---

### STEP 3️⃣: Add Your API Key (1 minute)

1. In Streamlit Cloud, click on your app
2. Click **⚙️ Settings** → **Secrets**
3. Paste this (replace with your actual key):

```toml
GEMINI_API_KEY = "your_actual_gemini_api_key_here"
```

4. Click **Save**

🔑 **Don't have an API key?** Get one free at: https://makersuite.google.com/app/apikey

✅ **Done!** Your app is fully functional!

---

## 🎉 Your App is Live!

Your app URL will be:
```
https://YOUR_USERNAME-YOUR_REPO.streamlit.app
```

Example: `https://johndoe-scheme-research.streamlit.app`

---

## 🧪 Test Your App

1. Open your live URL
2. In the sidebar, paste a scheme URL (example below)
3. Click "🚀 Analyze URLs"
4. Ask a question about the scheme

**Example URL to test**:
```
https://pib.gov.in/PressReleasePage.aspx?PRID=1234567
```

---

## 🏠 Run Locally (Optional)

Want to test before deploying?

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
echo "GEMINI_API_KEY=your_key_here" > .env

# Run the app
streamlit run main.py
```

Opens at: `http://localhost:8501`

---

## 📚 More Information

- **Quick Guide**: `DEPLOY_NOW.md`
- **Detailed Guide**: `DEPLOYMENT_GUIDE.md`
- **Summary**: `DEPLOYMENT_SUMMARY.md`
- **Project Info**: `README.md`

---

## 🆘 Having Issues?

### "I don't have a GitHub account"
→ Create one free at: https://github.com/join

### "I don't have a Gemini API key"
→ Get one free at: https://makersuite.google.com/app/apikey

### "The app shows an error"
→ Check that you added `GEMINI_API_KEY` in Streamlit Cloud secrets

### "I want to use Vercel"
→ Not possible - Vercel doesn't support Streamlit apps. Use Streamlit Cloud instead.

---

## ✅ Checklist

- [ ] Code pushed to GitHub
- [ ] Streamlit Cloud account created
- [ ] App deployed
- [ ] API key added to secrets
- [ ] App tested with a URL
- [ ] Live URL shared with others!

---

## 🎊 That's It!

You now have a **live, public, AI-powered research assistant** that anyone can use!

**Share your URL** with colleagues, friends, or on social media! 🚀

---

**Need help?** Check the other documentation files or visit: https://docs.streamlit.io/

**Happy deploying! 🎉**
