# Quick Start Guide - Image Captioning App

## ✅ What's Been Completed

1. **Complete `app.py`** - All TODOs are implemented:
   - BLIP model loading with caching
   - UI with title and sidebar
   - 4 parameter sliders (Temperature, Min Length, Max Length, Number of Variations)
   - File uploader for images
   - Conditional captioning with starting text
   - Multiple caption generation
   - Display of results

2. **`requirements.txt`** - All dependencies listed

3. **`.streamlit/config.toml`** - Streamlit configuration

## ⚠️ IMPORTANT: Before You Deploy

### Step 1: Update Your Information
Open `app.py` and find line 32. Replace:
```python
st.markdown("**Name:** [Your Name] | **Student ID:** [Your Student ID]")
```
With your actual name and student ID:
```python
st.markdown("**Name:** John Doe | **Student ID:** 12345678")
```

## 🚀 Next Steps: Deployment

### Option A: Test Locally First (Recommended)

1. **Create a virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```powershell
   streamlit run app.py
   ```

4. **Test with different images and parameters**

### Option B: Deploy to Streamlit Cloud

Follow the detailed instructions in `DEPLOYMENT_GUIDE.md`. Here's the summary:

1. **Initialize Git** (if not done):
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Create GitHub Repository:**
   - Go to https://github.com/new
   - Create a **PRIVATE** repository
   - Name it something like `yzv211-hw3`

3. **Push to GitHub:**
   ```powershell
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git branch -M main
   git push -u origin main
   ```

4. **Deploy on Streamlit Cloud:**
   - Go to https://share.streamlit.io/
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set Main file path: `app.py`
   - Set App URL: `[YourStudentID]yzv211hw3` (lowercase, no spaces)
   - Click "Deploy"

5. **Grant Access to Private Repo:**
   - Go to https://github.com/settings/installations
   - Find "Streamlit Cloud"
   - Configure → Select your private repository
   - Save

## 📝 For Your Report

You'll need to test and document:

1. **Effect of Temperature:**
   - Try same image with temperature 0.1, 0.5, 1.0, 1.5
   - Note differences in creativity vs accuracy
   - Take screenshots

2. **Length Constraints:**
   - Upload simple image (blue sky, single chair)
   - Set min_length around 10
   - Generate multiple captions with low and high temperatures
   - Compare results

3. **Conditional Captioning:**
   - Upload image
   - Enter starting text like "A beautiful"
   - Generate captions
   - Compare with captions without starting text

4. **Screenshots:**
   - Take screenshots of your app interface
   - Include examples for each scenario
   - Save as separate image files

## 📦 Submission Checklist

- [ ] Updated Name and Student ID in app.py
- [ ] Tested app locally
- [ ] Deployed to Streamlit Cloud
- [ ] App URL: `https://[StudentID]yzv211hw3.streamlit.app`
- [ ] Repository is PRIVATE
- [ ] App is publicly accessible
- [ ] Created ZIP with app.py, images, screenshots
- [ ] Created Report.pdf (max 2 pages)
- [ ] Created URL.txt with Streamlit app link

## 🆘 Troubleshooting

**App shows white screen:**
- Click three dots (⋮) → "Reboot App" in Streamlit Cloud

**Model loading takes too long:**
- First load downloads ~1GB model, be patient
- Subsequent loads are cached

**Can't access private repo:**
- Make sure you granted Streamlit Cloud access in GitHub settings

**Need help?**
- Check `DEPLOYMENT_GUIDE.md` for detailed instructions
- Streamlit docs: https://docs.streamlit.io/

