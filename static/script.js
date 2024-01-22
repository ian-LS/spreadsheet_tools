function validateFormat() {
    let form = document.getElementById('validate-form');
    let formData = new FormData(form);

    fetch('/validate', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        displayResult('validate-result-container', data.result);
    });
}

function mergeFiles() {
    let form = document.getElementById('merge-form');
    let formData = new FormData(form);

    fetch('/merge', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        displayResult('merge-result-container', data.result);
    });
}

function displayResult(containerId, result) {
    let resultContainer = document.getElementById(containerId);
    resultContainer.innerHTML = '<h2>Result:</h2><pre>' + result + '</pre>';
}
