# ⚡ Quick GitHub Setup

## 🚀 Push to GitHub in 5 Steps

### Step 1: Create Repository on GitHub
1. Go to **https://github.com**
2. Click **"+"** → **"New repository"**
3. Name it: `encryption-decryption-app`
4. Click **"Create repository"**
5. **Copy the repository URL**

### Step 2: Configure Git (First Time Only)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Connect to GitHub
```bash
git remote add origin https://github.com/yourusername/encryption-decryption-app.git
```
*(Replace with YOUR repository URL)*

### Step 4: Push to GitHub
```bash
git branch -M main
git push -u origin main
```

### Step 5: Enter Credentials
- **Username:** Your GitHub username
- **Password:** Use a Personal Access Token (not your password)
  - Get token: https://github.com/settings/tokens
  - Select "repo" permissions

---

## 🔄 Update GitHub After Changes

```bash
git add .
git commit -m "Your message"
git push
```

---

**For detailed instructions, see `GITHUB_GUIDE.md`**

