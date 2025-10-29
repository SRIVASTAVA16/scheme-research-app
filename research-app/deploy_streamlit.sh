#!/bin/bash

# Deployment Helper Script for Streamlit Cloud
# This script helps you prepare your app for deployment

echo "🚀 Streamlit Cloud Deployment Helper"
echo "======================================"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git branch -M main
    echo "✅ Git initialized"
else
    echo "✅ Git repository already exists"
fi

# Check if .env exists and warn user
if [ -f ".env" ]; then
    echo ""
    echo "⚠️  WARNING: .env file detected!"
    echo "   Make sure .env is in .gitignore (it should be)"
    echo "   You'll need to add GEMINI_API_KEY to Streamlit Cloud secrets"
    echo ""
fi

# Add all files
echo ""
echo "📝 Staging files for commit..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "✅ No new changes to commit"
else
    echo "💾 Committing changes..."
    git commit -m "Prepare for Streamlit Cloud deployment"
    echo "✅ Changes committed"
fi

echo ""
echo "📋 Next Steps:"
echo "=============="
echo ""
echo "1. Create a GitHub repository:"
echo "   - Go to https://github.com/new"
echo "   - Create a new repository (e.g., 'scheme-research-app')"
echo ""
echo "2. Push your code:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
echo "   git push -u origin main"
echo ""
echo "3. Deploy to Streamlit Cloud:"
echo "   - Go to https://share.streamlit.io/"
echo "   - Sign in with GitHub"
echo "   - Click 'New app'"
echo "   - Select your repository"
echo "   - Set main file: main.py"
echo "   - Add secret: GEMINI_API_KEY in Settings → Secrets"
echo ""
echo "4. Your app will be live at:"
echo "   https://YOUR_USERNAME-YOUR_REPO.streamlit.app"
echo ""
echo "📖 For detailed instructions, see DEPLOYMENT_GUIDE.md"
echo ""
echo "✨ Happy deploying!"
