document.getElementById('textBox-part').addEventListener('submit', async (event) => {
    event.preventDefault();
    
    const form = event.target;
    const formData = new FormData(form);
    
    try {
        const response = await fetch('/process-form', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        const resultText = document.getElementById('resultText');
        
        if (data.result) {
            // Access the first item's second element (the response text)
            resultText.textContent = data.result[0][1];
        } else if (data.error) {
            resultText.textContent = data.error;
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('resultText').textContent = 'Error processing request';
    }
});