# Step-by-Step Guide to Run the Encryption/Decryption Program

## 📍 Current Location
You are in: `F:\operating system`

---

## ✅ Step 1: Open Terminal in VS Code

1. **Press the backtick key** (`` ` ``) - usually above the Tab key
   - OR press `Ctrl + Shift + `` (backtick)
   - OR go to menu: **Terminal → New Terminal**

2. **You should see a terminal window at the bottom of VS Code**

---

## ✅ Step 2: Verify You're in the Right Folder

**In the terminal, type:**
```
dir
```
**Press `Enter`**

**You should see files like:**
- app.py
- index.html
- style.css
- script.js
- requirements.txt
- encrypt_decrypt.c

**If you don't see these files, type:**
```
cd "F:\operating system"
```
**Press `Enter`**

---

## ✅ Step 3: Install Python Dependencies

**In the terminal, type:**
```
pip install -r requirements.txt
```
**Press `Enter`**

**What you'll see:**
```
Collecting Flask==3.0.0
Collecting flask-cors==4.0.0
Installing collected packages...
Successfully installed Flask-3.0.0 flask-cors-4.0.0
```

**✅ If you see "Successfully installed" - you're good to go!**

**❌ If you see an error:**
- Try: `python -m pip install -r requirements.txt`
- Or: `py -m pip install -r requirements.txt`

---

## ✅ Step 4: Start the Server

**In the terminal, type:**
```
python app.py
```
**Press `Enter`**

**What you'll see:**
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

**✅ SUCCESS! The server is now running!**

**⚠️ IMPORTANT:**
- **Keep this terminal window open!**
- **Don't close it** - the server must keep running
- You'll see the server logs here

---

## ✅ Step 5: Open Your Web Browser

1. **Open any web browser** (Chrome, Firefox, Edge, etc.)

2. **Click on the address bar** (at the top)

3. **Type exactly:**
   ```
   http://localhost:5000
   ```

4. **Press `Enter`**

---

## ✅ Step 6: You Should See the Web Interface

**You'll see:**
- Purple gradient background
- White card with "File Encryption/Decryption Tool"
- A dropdown menu (Encrypt File / Decrypt File)
- A "Choose File" button
- An "Encryption Key" input box
- A blue "Process File" button

**✅ If you see this - everything is working!**

---

## 🔐 How to Encrypt a File

### Step 1: Select Operation
- The dropdown should already say "Encrypt File"
- If not, click it and select "Encrypt File"

### Step 2: Choose File
- Click the **"Choose File"** button
- Navigate to any file on your computer
- Click on the file
- Click **"Open"**
- The file name will appear next to the button

### Step 3: Enter Key
- Click in the **"Encryption Key"** box
- Type a number between **1 and 255**
- Example: `5`, `10`, `25`, `100`
- **⚠️ Remember this number!** You'll need it to decrypt

### Step 4: Process
- Click the blue **"Process File"** button
- Wait a few seconds
- Button will show "Processing..."

### Step 5: Download
- The encrypted file will **automatically download**
- Check your **Downloads folder**
- File name: `encrypted_[your_filename]`

---

## 🔓 How to Decrypt a File

### Step 1: Select Operation
- Click the dropdown menu
- Select **"Decrypt File"**

### Step 2: Choose Encrypted File
- Click **"Choose File"**
- Select the **encrypted file** (the one you just encrypted)
- Click **"Open"**

### Step 3: Enter the SAME Key
- Click in the **"Encryption Key"** box
- Type the **EXACT SAME NUMBER** you used for encryption
- **⚠️ Must be the same number!**

### Step 4: Process
- Click the blue **"Process File"** button
- Wait for processing

### Step 5: Download
- The decrypted file will **automatically download**
- Check your **Downloads folder**
- File name: `decrypted_[your_filename]`

---

## 🛑 How to Stop the Server

**When you're done using the program:**

1. **Go back to the VS Code terminal** (where you see "Running on http://127.0.0.1:5000")

2. **Press `Ctrl + C`**
   - You may need to press it twice

3. **You'll see:**
   ```
   ^C
   KeyboardInterrupt
   ```

4. **Server stopped!** You can now close the terminal.

---

## ❌ Troubleshooting

### Problem: "python is not recognized"
**Solution:** Try `py app.py` instead of `python app.py`

### Problem: "pip is not recognized"
**Solution:** Try `python -m pip install -r requirements.txt`

### Problem: "Port 5000 is already in use"
**Solution:** 
- Close other programs using port 5000
- Or change port in `app.py` line 100 to `port=5001`
- Then use `http://localhost:5001`

### Problem: Browser shows "This site can't be reached"
**Solutions:**
1. Make sure the server is running (check terminal)
2. Make sure you typed: `http://localhost:5000` (not https)
3. Try: `http://127.0.0.1:5000`

### Problem: File doesn't download
**Solutions:**
1. Check your browser's download folder
2. Check browser settings (some block auto-downloads)
3. Try a different browser

---

## 📋 Quick Command Reference

| Action | Command |
|--------|---------|
| Install dependencies | `pip install -r requirements.txt` |
| Start server | `python app.py` |
| Stop server | `Ctrl + C` |
| Browser URL | `http://localhost:5000` |

---

## ✅ Checklist Before Running

- [ ] Terminal is open in VS Code
- [ ] You're in the `F:\operating system` folder
- [ ] Dependencies are installed (`pip install -r requirements.txt`)
- [ ] Server is running (`python app.py`)
- [ ] Browser is open to `http://localhost:5000`
- [ ] You see the web interface

---

## 🎯 Example: Complete Workflow

1. **Open terminal:** Press `` ` `` in VS Code
2. **Install:** Type `pip install -r requirements.txt` → Press Enter
3. **Start:** Type `python app.py` → Press Enter
4. **Open browser:** Go to `http://localhost:5000`
5. **Encrypt:**
   - Select "Encrypt File"
   - Choose a file
   - Enter key: `25`
   - Click "Process File"
6. **Decrypt:**
   - Select "Decrypt File"
   - Choose the encrypted file
   - Enter key: `25` (same!)
   - Click "Process File"
7. **Stop:** Press `Ctrl + C` in terminal

---

**That's it! You're ready to encrypt and decrypt files! 🔐**

