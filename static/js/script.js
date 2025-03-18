// Fetch internal API data
function fetchInternalData() {
    fetch('/api/internal')
    .then(response => response.json())
    .then(data => {
        document.getElementById('internal-data').textContent = data.message;
    })
    .catch(error => console.error('Error:', error));
}

// Fetch GitHub API data
function fetchExternalData() {
    fetch('/api/github')
    .then(response => response.json())
    .then(data => {
        let output = "GitHub Repositories:<br>";
        data.forEach(repo => {
            output += `<p><a href="${repo.html_url}" target="_blank">${repo.name}</a></p>`;
        });
        document.getElementById('external-data').innerHTML = output;
    })
    .catch(error => console.error('Error:', error));
}
