# Image Captioning App - Deployment Guide

## 📋 Prerequisites

1. **GitHub Account** - You need a GitHub account
2. **Streamlit Cloud Account** - Sign up at https://streamlit.io/cloud (free)
3. **Git** - Installed on your local machine

## 🚀 Step-by-Step Deployment Instructions

### Step 1: Update Your Information in app.py

**IMPORTANT:** Before deploying, you MUST update the Name and Student ID in `app.py`:

1. Open `app.py`
2. Find this line (around line 30):
   ```python
   st.markdown("**Name:** [Your Name] | **Student ID:** [Your Student ID]")
   ```
3. Replace `[Your Name]` with your actual name
4. Replace `[Your Student ID]` with your actual student ID

### Step 2: Initialize Git Repository (if not already done)

Open PowerShell or Command Prompt in your project directory and run:

```bash
git init
git add .
git commit -m "Initial commit: Image Captioning App"
```

### Step 3: Create GitHub Repository

1. Go to https://github.com/new
2. **Repository name:** Use a name like `yzv211-hw3` or `image-captioning-app`
3. **Visibility:** Select **PRIVATE** (as required by the assignment)
4. **DO NOT** initialize with README, .gitignore, or license
5. Click "Create repository"

### Step 4: Connect Local Repository to GitHub

GitHub will show you commands. Run these in your project directory:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name.

### Step 5: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Click "New app" or "Sign in" if you haven't already
3. Click "Continue with GitHub" and authorize Streamlit Cloud
4. Fill in the deployment form:
   - **Repository:** Select your private repository
   - **Branch:** `main` (or `master` if that's your default branch)
   - **Main file path:** `app.py`
   - **App URL:** This will be auto-generated, but you can customize it
     - Format: `[StudentID]yzv211hw3` (e.g., `12345678yzv211hw3`)
     - Make sure it's lowercase and follows the format
5. Click "Deploy"

### Step 6: Grant Streamlit Access to Private Repository

If your repository is private, Streamlit needs permission:

1. Go to https://github.com/settings/installations
2. Find "Streamlit Cloud" in the list
3. Click "Configure"
4. Under "Repository access", select:
   - Either "All repositories" OR
   - "Only select repositories" and choose your private repo
5. Click "Save"

### Step 7: Wait for Deployment

- Streamlit will install dependencies from `requirements.txt`
- This may take 5-10 minutes on first deployment
- You'll see logs in the Streamlit Cloud dashboard
- Once deployed, your app URL will be: `https://[StudentID]yzv211hw3.streamlit.app`

### Step 8: Test Your App

1. Visit your app URL
2. Upload a test image
3. Try different parameter settings
4. Verify everything works correctly

## 🔧 Troubleshooting

### App Shows White Screen or Error

1. **Out of Memory:** Click the three dots (⋮) in bottom-right → "Reboot App"
2. **Check Logs:** In Streamlit Cloud dashboard, check the logs for errors
3. **Model Loading Issues:** The BLIP model is large (~1GB), first load may take time

### Changes Not Reflecting

- Streamlit Cloud auto-updates when you push to GitHub
- Wait 1-2 minutes after pushing
- Or manually click "Reboot App" in Streamlit Cloud

### Can't Access Private Repository

- Make sure you've granted Streamlit Cloud access (Step 6)
- Check repository visibility settings on GitHub

## 📝 Files Required for Deployment

Your repository should contain:
- ✅ `app.py` - Main application file
- ✅ `requirements.txt` - Python dependencies
- ✅ `.streamlit/config.toml` - Streamlit configuration (optional but recommended)

## 🎯 Final Checklist

Before submission:
- [ ] Updated Name and Student ID in app.py
- [ ] Repository is PRIVATE on GitHub
- [ ] Streamlit Cloud has access to your private repo
- [ ] App URL follows format: `[StudentID]yzv211hw3.streamlit.app`
- [ ] App is publicly accessible (even though repo is private)
- [ ] All features working: file upload, sliders, caption generation
- [ ] Conditional captioning works with starting text

## 📧 Submission Requirements

1. **ZIP file** containing:
   - `app.py`
   - Selected test images
   - Screenshots of the app interface

2. **Report.pdf** (max 2 pages) with:
   - Selected images
   - Analysis of parameter effects
   - Temperature analysis
   - Length constraint analysis
   - Conditional captioning examples

3. **URL file** (txt) containing:
   - Your Streamlit app URL: `https://[StudentID]yzv211hw3.streamlit.app`

4. **GitHub Repo Link** (must be private)

