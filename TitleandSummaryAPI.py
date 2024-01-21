from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import openai

app = Flask(__name__)
CORS(app, resources={r"/generate_summary": {"origins": "*"}})  # Allow any origin

#openai.api_key = #Insert API Key

def is_article(soup):
    # Check if the page seems to be an article (customize these conditions based on the structure)
    return soup.find('title') is not None and soup.find_all('p')

def scrape_and_generate_summary(url):
    # Fetch HTML content from the provided URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        if is_article(soup):
            # It seems to be an article, proceed with extracting information

            # Find the article title
            article_title = soup.find('title').text.strip()

            # Find the article content
            paragraphs = soup.find_all('p')
            article_content = '\n'.join([p.text.strip() for p in paragraphs])

            # Generate a simple summary (you might want to use more advanced techniques)
            summary = article_content[:3500] + '...' 
            
            # Use the article title and summary to generate a new title
            prompt = f"Title: {article_title}, First 3500 characters: {summary}, In 50 characters or less, \\nplease take the given article title and the given summary\\nand generate a new article title that serves as a summary of the article."
            prompt2 = f"""Title: {article_title}, First 3500 characters: {summary}, In 1000 characters or less, please also generate a revised summary that summarizes the key points of the article."""
            
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=1000
            )
            
            response2 = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=prompt2,
                max_tokens=1000
            )
            
            revised_title = response['choices'][0]['text'].strip()
            revised_summary = response2['choices'][0]['text'].strip()

            # Return the result as a dictionary
            return {'Original_title': article_title, 'Original_summary': summary, 'Revised_title': revised_title, 'Revised_summary': revised_summary}

        else:
            return {'error': 'The provided URL does not seem to be an article. Please check your URL to make sure it is a valid link!'}

    else:
        return {'error': f'Failed to fetch content. Status code: {response.status_code}'}

@app.route('/generate_summary', methods=['POST', 'OPTIONS'])
def handle_generate_summary():
    if request.method == 'OPTIONS':
        # Respond to the preflight request
        response = app.make_default_options_response()
    else:
        # Handle the actual POST request
        data = request.json
        url_to_scrape = data.get('url')

        if url_to_scrape:
            result = scrape_and_generate_summary(url_to_scrape)
            return jsonify(result)

        response = jsonify({'error': 'Invalid request. Please provide a valid URL in the request payload.'}), 400

    # Allow the required headers for CORS
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Max-Age'] = '3600'  # Cache preflight response for 1 hour

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
