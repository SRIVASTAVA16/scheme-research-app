# 🚀 Deployment Guide for Scheme Research Assistant

## ⚠️ Important Note About Vercel

**Streamlit applications cannot be deployed directly on Vercel** because:
- Vercel is designed for serverless functions (Flask, FastAPI, Next.js)
- Streamlit requires persistent WebSocket connections
- Vercel's serverless architecture doesn't support long-running processes

## ✅ Recommended Deployment Options

### Option 1: Streamlit Cloud (FREE & EASIEST) ⭐

Streamlit Cloud is the official, free hosting platform for Streamlit apps.

#### Steps to Deploy:

1. **Push your code to GitHub**
   ```bash
   cd /vercel/sandbox/research-app
   git init
   git add .
   git commit -m "Initial commit - Scheme Research Assistant"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io/
   - Sign in with your GitHub account
   - Click "New app"

3. **Configure Your App**
   - Repository: Select your GitHub repo
   - Branch: `main`
   - Main file path: `main.py`
   - Click "Deploy"

4. **Set Environment Variables**
   - In Streamlit Cloud dashboard, go to "Settings" → "Secrets"
   - Add your secrets in TOML format:
   ```toml
   GEMINI_API_KEY = "your_actual_gemini_api_key_here"
   ```

5. **Access Your Live App**
   - Your app will be available at: `https://YOUR_USERNAME-YOUR_REPO_NAME.streamlit.app`
   - Example: `https://johndoe-research-app.streamlit.app`

#### Advantages:
- ✅ Free forever
- ✅ Automatic HTTPS
- ✅ Auto-deploys on git push
- ✅ Built specifically for Streamlit
- ✅ No configuration needed
- ✅ Persistent storage support

---

### Option 2: Render.com (FREE Tier Available)

Render supports long-running web services and works great with Streamlit.

#### Steps to Deploy:

1. **Push code to GitHub** (same as Option 1, step 1)

2. **Go to Render**
   - Visit: https://render.com/
   - Sign up/Sign in
   - Click "New +" → "Web Service"

3. **Connect Repository**
   - Connect your GitHub account
   - Select your repository

4. **Configure Service**
   - Name: `scheme-research-assistant`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run main.py --server.port=$PORT --server.address=0.0.0.0`

5. **Set Environment Variables**
   - Add: `GEMINI_API_KEY` = `your_actual_key`

6. **Deploy**
   - Click "Create Web Service"
   - Your app will be live at: `https://scheme-research-assistant.onrender.com`

#### Advantages:
- ✅ Free tier available
- ✅ Supports WebSockets
- ✅ Auto-deploys on git push
- ✅ Custom domains supported

---

### Option 3: Hugging Face Spaces (FREE)

Hugging Face Spaces provides free hosting for ML/AI applications.

#### Steps to Deploy:

1. **Create a Space**
   - Visit: https://huggingface.co/spaces
   - Click "Create new Space"
   - Choose "Streamlit" as the SDK
   - Name your space

2. **Upload Files**
   - Upload all your project files
   - Or connect via Git

3. **Add Secrets**
   - Go to Settings → Repository secrets
   - Add: `GEMINI_API_KEY`

4. **Access Your App**
   - Your app will be at: `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`

---

### Option 4: Railway.app (FREE Tier)

Railway provides $5 free credit per month.

#### Steps to Deploy:

1. **Push code to GitHub** (same as Option 1, step 1)

2. **Go to Railway**
   - Visit: https://railway.app/
   - Sign up with GitHub
   - Click "New Project" → "Deploy from GitHub repo"

3. **Configure**
   - Select your repository
   - Railway will auto-detect Python
   - Add environment variable: `GEMINI_API_KEY`

4. **Add Start Command**
   - In Settings, set start command:
   ```bash
   streamlit run main.py --server.port=$PORT --server.address=0.0.0.0
   ```

5. **Deploy**
   - Your app will be live with a Railway URL

---

## 🏠 Running Locally

To run the app on your local machine:

```bash
# Navigate to project directory
cd /vercel/sandbox/research-app

# Activate virtual environment (if you have one)
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
echo "GEMINI_API_KEY=your_actual_key_here" > .env

# Run the app
streamlit run main.py
```

The app will open at: `http://localhost:8501`

---

## 🔑 Getting Your Gemini API Key

1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and use it in your deployment

---

## 📊 Comparison Table

| Platform | Free Tier | Ease of Use | Best For |
|----------|-----------|-------------|----------|
| **Streamlit Cloud** | ✅ Unlimited | ⭐⭐⭐⭐⭐ | Streamlit apps (Recommended) |
| **Render** | ✅ Limited | ⭐⭐⭐⭐ | General web apps |
| **Hugging Face** | ✅ Unlimited | ⭐⭐⭐⭐ | ML/AI projects |
| **Railway** | ✅ $5/month | ⭐⭐⭐ | Full-stack apps |
| **Vercel** | ❌ Not supported | ❌ | Serverless functions only |

---

## 🎯 Recommended Choice

**Use Streamlit Cloud** - It's specifically designed for Streamlit apps, completely free, and requires minimal configuration.

---

## 🆘 Need Help?

If you encounter any issues:
1. Check that your `GEMINI_API_KEY` is correctly set
2. Ensure all files are committed to GitHub
3. Check the deployment logs for errors
4. Verify your requirements.txt includes all dependencies

---

## 📝 Quick Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] `.env` file NOT committed (it's in .gitignore)
- [ ] `GEMINI_API_KEY` added to platform secrets
- [ ] All dependencies in requirements.txt
- [ ] App deployed and accessible
- [ ] Test with sample URLs

---

**Happy Deploying! 🚀**
