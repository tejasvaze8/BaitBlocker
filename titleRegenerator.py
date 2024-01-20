import requests
from bs4 import BeautifulSoup
import openai

openai.api_key = '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'

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
            
            # Print the revised title based on the content
            print(f"Revised Title: {revised_title}")

        else:
            print("Error: The provided URL does not seem to be an article. Please check your URL to make sure it is a valid link!")

    else:
        print(f"Failed to fetch content. Status code: {response.status_code}")

# Example usage
url_to_scrape = input("Enter the URL of the article: ")
scrape_and_generate_summary(url_to_scrape)
