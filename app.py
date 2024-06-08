from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from scrape import scrape_website_text
from summarize import summarize_text_with_mistral
from outreach import generate_outreach_message
from database import init_db, save_to_db

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'No URL provided.'}), 400

    webpage_text = scrape_website_text(url)
    if webpage_text:
        return jsonify({'content': webpage_text})
    else:
        return jsonify({'error': 'Failed to scrape website text.'}), 500

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided.'}), 400

    summarized_text = summarize_text_with_mistral(text)
    if summarized_text:
        return jsonify({'summary': summarized_text})
    else:
        return jsonify({'error': 'Failed to summarize text with Mistral.'}), 500

@app.route('/outreach', methods=['POST'])
def outreach():
    data = request.get_json()
    summary = data.get('summary')
    if not summary:
        return jsonify({'error': 'No summary provided.'}), 400

    outreach_message = generate_outreach_message(summary)
    if outreach_message:
        return jsonify({'message': outreach_message})
    else:
        return jsonify({'error': 'Failed to generate outreach message with Mistral.'}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5001)
