import requests
from bs4 import BeautifulSoup
import openai

openai.api_key = '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'

def scrape_and_generate_summary(url):
    # Fetch HTML content from the provided URL
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the article title
        article_title = soup.find('title').text.strip()

        # Find the article content (assuming the content is in paragraphs)
        paragraphs = soup.find_all('p')
        article_content = '\n'.join([p.text.strip() for p in paragraphs])

        # Generate a simple summary (you might want to use more advanced techniques)
        summary = article_content[:500] + '...'  # Just taking the first 500 characters as an example
        
        prompt2 = f"""Title: {article_title}, First 500 characters: {summary}, In 50 characters or less, \\n
        please take the given article title and the given summary
         \\n and generate a new article title that serves as a de facto tl;dr."""
        response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Choose the engine you want to use
        prompt= prompt2, 
        max_tokens=50  # Set the maximum number of tokens in the response
    )
        print(response['choices'][0]['text'])

    else:
        print(f"Failed to fetch content. Status code: {response.status_code}")

# Example usage
url_to_scrape = input("Enter the URL of the article: ")
scrape_and_generate_summary(url_to_scrape)

