from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
import os
import tempfile
import shutil

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Enable CORS for frontend-backend communication

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

# Create necessary directories
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def encrypt_decrypt_file(input_path, output_path, key, operation):
    """
    Encrypt or decrypt a file using the same algorithm as the C program.
    Operation: 'encrypt' or 'decrypt'
    """
    try:
        with open(input_path, 'rb') as fin:
            with open(output_path, 'wb') as fout:
                while True:
                    ch = fin.read(1)
                    if not ch:
                        break
                    
                    byte_value = ord(ch)
                    if operation == 'encrypt':
                        new_byte = (byte_value + key) % 256
                    else:  # decrypt
                        new_byte = (byte_value - key) % 256
                    
                    fout.write(bytes([new_byte]))
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/<path:path>')
def serve_static(path):
    if path in ['style.css', 'script.js']:
        return send_from_directory('.', path)
    return send_file('index.html')

@app.route('/encrypt-decrypt', methods=['POST'])
def encrypt_decrypt():
    try:
        # Check if file is present
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Get form data
        operation = request.form.get('operation', 'encrypt')
        key = request.form.get('key', type=int)
        
        if key is None:
            return jsonify({'error': 'Key is required'}), 400
        
        # Save uploaded file
        input_filename = file.filename
        input_path = os.path.join(UPLOAD_FOLDER, input_filename)
        file.save(input_path)
        
        # Generate output filename
        output_filename = f"{operation}ed_{input_filename}"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        
        # Perform encryption/decryption
        success = encrypt_decrypt_file(input_path, output_path, key, operation)
        
        if not success:
            return jsonify({'error': 'Failed to process file'}), 500
        
        # Return the processed file
        return send_file(
            output_path,
            as_attachment=True,
            download_name=output_filename
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

