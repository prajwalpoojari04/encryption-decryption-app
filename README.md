# 🔐 File Encryption/Decryption Web Application

A simple and elegant web-based file encryption/decryption tool built with Flask and modern web technologies.

## ✨ Features

- 🔒 **Encrypt files** with a numeric key
- 🔓 **Decrypt files** using the same key
- 🌐 **Web-based interface** - no command line needed
- 🎨 **Modern UI** with Bootstrap and custom styling
- 📁 **Supports any file type** (images, videos, documents, etc.)
- ⚡ **Fast and efficient** byte-level encryption

## 🛠️ Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Framework:** Bootstrap 5
- **Original:** C program (included)

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Modern web browser

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/encryption-decryption-app.git
   cd encryption-decryption-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 How to Run

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Open your browser:**
   - Navigate to: `http://localhost:5000`

3. **Use the interface:**
   - Select **Encrypt** or **Decrypt**
   - Choose a file
   - Enter a key (1-255)
   - Click **Process File**
   - Download will start automatically

## 📖 Usage Guide

### Encrypting a File

1. Select **"Encrypt File"** from the dropdown
2. Click **"Choose File"** and select your file
3. Enter an encryption key (number between 1-255)
4. Click **"Process File"**
5. The encrypted file will download automatically

### Decrypting a File

1. Select **"Decrypt File"** from the dropdown
2. Click **"Choose File"** and select the encrypted file
3. Enter the **SAME key** used for encryption
4. Click **"Process File"**
5. The decrypted file will download automatically

⚠️ **Important:** You must use the **exact same key** for decryption that you used for encryption!

## 📁 Project Structure

```
encryption-decryption-app/
├── app.py                 # Flask backend server
├── index.html             # Frontend HTML
├── style.css              # Custom styling
├── script.js              # Frontend JavaScript
├── requirements.txt       # Python dependencies
├── encrypt_decrypt.c      # Original C program
├── STEP_BY_STEP_GUIDE.md  # Detailed guide
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🔧 Configuration

The server runs on `http://localhost:5000` by default. To change the port, edit `app.py`:

```python
app.run(debug=True, port=5000)  # Change port number here
```

## 🐛 Troubleshooting

### Port Already in Use
If port 5000 is busy, change it in `app.py` or stop the process using the port:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID [PID] /F
```

### Python Not Found
Try using `py` instead of `python`:
```bash
py app.py
```

### Dependencies Not Installing
Use:
```bash
python -m pip install -r requirements.txt
```

## 🔒 Security Note

This is a simple encryption tool for educational purposes. For production use, consider stronger encryption algorithms (AES, RSA, etc.).

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

Your Name

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⭐ Show Your Support

Give a ⭐ if you like this project!

---

**Made with ❤️ using Flask and Bootstrap**

