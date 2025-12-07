# 🚀 Push to GitHub - Quick Steps

## Step 1: Create GitHub Repository (Do This First!)

1. **Go to:** https://github.com
2. **Click:** "+" icon (top right) → "New repository"
3. **Repository name:** `encryption-decryption-app` (or any name)
4. **Description:** "Web-based file encryption/decryption tool"
5. **Visibility:** Choose Public or Private
6. **⚠️ IMPORTANT:** DO NOT check "Initialize with README"
7. **Click:** "Create repository"
8. **Copy the repository URL** - it looks like:
   ```
   https://github.com/yourusername/encryption-decryption-app.git
   ```

## Step 2: Run These Commands

After creating the repository, come back here and run these commands in your terminal:

```bash
# Replace YOUR_USERNAME and REPO_NAME with your actual values
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

**Example:**
```bash
git remote add origin https://github.com/johnsmith/encryption-decryption-app.git
git branch -M main
git push -u origin main
```

## Step 3: Authentication

When you run `git push`, GitHub will ask for:
- **Username:** Your GitHub username
- **Password:** Use a **Personal Access Token** (NOT your password!)

### Get Personal Access Token:
1. Go to: https://github.com/settings/tokens
2. Click: "Generate new token" → "Generate new token (classic)"
3. **Name:** "My Computer"
4. **Select scopes:** Check ✅ "repo"
5. Click: "Generate token"
6. **⚠️ COPY THE TOKEN** (you won't see it again!)
7. Use this token as your password when pushing

---

## ✅ That's It!

After pushing, your code will be on GitHub at:
```
https://github.com/yourusername/encryption-decryption-app
```

