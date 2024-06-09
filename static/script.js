document.addEventListener('DOMContentLoaded', () => {
    // Scrape form submission
    document.getElementById('scrape-form').addEventListener('submit', async (event) => {
        event.preventDefault();
        const url = document.getElementById('url-input').value;
        const resultDiv = document.getElementById('scrape-result');
        resultDiv.innerHTML = 'Scraping...';

        try {
            const response = await fetch('/scrape', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ url })
            });
            const data = await response.json();
            resultDiv.innerHTML = `<p>${data.content}</p>`;

            // After scraping, scroll to the summarize section
            window.location.href = '#summarize';
        } catch (error) {
            resultDiv.innerHTML = '<p>An error occurred while scraping the website.</p>';
        }
    });

    // Summarize button click
    document.getElementById('summarize-button').addEventListener('click', async () => {
        const text = document.getElementById('scrape-result').textContent;
        const resultDiv = document.getElementById('summarize-result');
        resultDiv.innerHTML = 'Summarizing...';

        try {
            const response = await fetch('/summarize', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text })
            });
            const data = await response.json();
            resultDiv.innerHTML = `<p>${data.summary}</p>`;
        } catch (error) {
            resultDiv.innerHTML = '<p>An error occurred while summarizing the text.</p>';
        }
    });

    // Outreach button click
    document.getElementById('outreach-button').addEventListener('click', async () => {
        const summary = document.getElementById('summarize-result').textContent;
        const resultDiv = document.getElementById('outreach-result');
        resultDiv.innerHTML = 'Generating outreach message...';

        try {
            const response = await fetch('/outreach', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ summary })
            });
            const data = await response.json();
            resultDiv.innerHTML = `<p>${data.message}</p>`;
        } catch (error) {
            resultDiv.innerHTML = '<p>An error occurred while generating the outreach message.</p>';
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const outreachButton = document.getElementById('outreach-button');
    const outreachResult = document.getElementById('outreach-result');

    outreachButton.addEventListener('click', async function() {
        const name = document.getElementById('name-input').value;
        const company = document.getElementById('company-input').value;
        const product = document.getElementById('product-input').value;
        const summary = document.getElementById('summarize-result').textContent;

        if (!name || !company || !product || !summary) {
            alert('Please fill out all fields and generate a summary first.');
            return;
        }

        try {
            const response = await fetch('/generate_outreach_message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, company, product, summary })
            });

            const data = await response.json();

            if (response.ok) {
                outreachResult.textContent = data.message;
            } else {
                outreachResult.textContent = `Error: ${data.error}`;
            }
        } catch (error) {
            outreachResult.textContent = `Error: ${error.message}`;
        }
    });
});
