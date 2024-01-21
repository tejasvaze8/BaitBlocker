from flask import Flask, request
import requests
from bs4 import BeautifulSoup
import tempfile
from pymongo import MongoClient
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from flask_cors import CORS
# Import other necessary libraries and classes

app = Flask(__name__)
CORS(app, resources={"/process_link": {"origins": "*"}})  # Allow any origin


os.environ["OPENAI_API_KEY"] = "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"
MONGO_URI = "mongodb+srv://tvaze:gmjg94r0F7Y8fMWW@cluster0.koafm.mongodb.net/?retryWrites=true&w=majority"
# initialize MongoDB python client
client = MongoClient(MONGO_URI)
DB_NAME = "BaitBlocker"
COLLECTION_NAME = "QandAvectorStore"

ATLAS_VECTOR_SEARCH_INDEX_NAME = "vector_index"


MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]

@app.route('/process_link', methods=['POST'])
def process_link():
    print("Processing link")
    content = request.json

    link = content.get('url')
    print(link)
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    article_content = '\n'.join([p.text.strip() for p in paragraphs])

    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as temp_file:
        # Write text to the temporary file
        temp_file.write(article_content)
        # Get the name of the file
        temp_file_name = temp_file.name

    loader = TextLoader(temp_file_name)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = text_splitter.split_documents(data)
    vector_search = MongoDBAtlasVectorSearch.from_documents(
        documents=docs,
        embedding=OpenAIEmbeddings(disallowed_special=()),
        collection=MONGODB_COLLECTION,
        index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    )

    # Perform a similarity search between the embedding of the query and the embeddings of the documents
    query = "test?"
    results = vector_search.similarity_search(query)
    payload = {'status': 'success'}
    return payload  # Indicates success but no content to return


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
