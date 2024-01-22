function validateFormat() {
    let form = document.getElementById('validate-form');
    let formData = new FormData(form);

    fetch('/validate', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        displayResult(data.result);
    });
}

// Add similar functions for other functionalities

function displayResult(result) {
    let resultContainer = document.getElementById('result-container');
    resultContainer.innerHTML = '<h2>Result:</h2><pre>' + result + '</pre>';
}
