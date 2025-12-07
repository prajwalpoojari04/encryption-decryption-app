document.getElementById('encryptForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const form = e.target;
    const formData = new FormData(form);
    const submitBtn = document.getElementById('submitBtn');
    const btnText = document.getElementById('btnText');
    const btnSpinner = document.getElementById('btnSpinner');
    const alertContainer = document.getElementById('alertContainer');
    
    // Clear previous alerts
    alertContainer.innerHTML = '';
    
    // Disable button and show spinner
    submitBtn.disabled = true;
    btnText.textContent = 'Processing...';
    btnSpinner.classList.remove('d-none');
    
    try {
        const response = await fetch('http://localhost:5000/encrypt-decrypt', {
            method: 'POST',
            body: formData
        });
        
        if (response.ok) {
            // Get the filename from response headers or use a default
            const contentDisposition = response.headers.get('Content-Disposition');
            let filename = 'processed_file';
            if (contentDisposition) {
                const filenameMatch = contentDisposition.match(/filename="?(.+)"?/);
                if (filenameMatch) {
                    filename = filenameMatch[1];
                }
            }
            
            // Download the file
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
            
            // Show success message
            const operation = formData.get('operation');
            alertContainer.innerHTML = `
                <div class="alert alert-success alert-dismissible fade show" role="alert">
                    <strong>Success!</strong> File ${operation === 'encrypt' ? 'encrypted' : 'decrypted'} successfully. Download started automatically.
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            `;
            
            // Reset form
            form.reset();
        } else {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to process file');
        }
    } catch (error) {
        alertContainer.innerHTML = `
            <div class="alert alert-danger alert-dismissible fade show" role="alert">
                <strong>Error!</strong> ${error.message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
        `;
    } finally {
        // Re-enable button and hide spinner
        submitBtn.disabled = false;
        btnText.textContent = 'Process File';
        btnSpinner.classList.add('d-none');
    }
});

