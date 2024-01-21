from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import openai

app = Flask(__name__)

#Insert API Key here

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
            summary = article_content[:500] + '...'  # Just taking the first 500 characters as an example
            
            # Use the article title and summary to generate a new title
            prompt = f"Title: {article_title}, First 500 characters: {summary}, In 50 characters or less, \\nplease take the given article title and the given summary\\nand generate a new article title that serves as a de facto tl;dr."
            
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=50
            )
            
            revised_title = response['choices'][0]['text'].strip()

            # Return the result as a dictionary
            return {'original_title': article_title, 'original_summary': summary, 'revised_title': revised_title}

        else:
            return {'error': 'The provided URL does not seem to be an article. Please check your URL to make sure it is a valid link!'}

    else:
        return {'error': f'Failed to fetch content. Status code: {response.status_code}'}

@app.route('/generate_summary', methods=['POST'])
def generate_summary():
    data = request.json
    url_to_scrape = data.get('url')

    if url_to_scrape:
        result = scrape_and_generate_summary(url_to_scrape)
        return jsonify(result)

    return jsonify({'error': 'Invalid request. Please provide a valid URL in the request payload.'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
