from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from langchain.prompts import PromptTemplate
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"/ask_question": {"origins": "*"}})  # Allow any origin

DB_NAME = "BaitBlocker"
COLLECTION_NAME = "QandAvectorStore"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "vector_index"
MONGO_URI = "mongodb+srv://tvaze:gmjg94r0F7Y8fMWW@cluster0.koafm.mongodb.net/?retryWrites=true&w=majority"
openai_api_key = "add api key"
os.environ["OPENAI_API_KEY"] = "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"

@app.route('/ask_question', methods=['POST'])
def ask_question():
    try:
        content = request.json
        question = content.get('question')

        vector_search = MongoDBAtlasVectorSearch.from_connection_string(
            MONGO_URI,
            DB_NAME + "." + COLLECTION_NAME,
            OpenAIEmbeddings(disallowed_special=()),
            index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
        )

        qa_retriever = vector_search.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 25},
        )

        prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

        {context}

        Question: {question}
        """
        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )

        qa = RetrievalQA.from_chain_type(
            llm=OpenAI(),
            chain_type="stuff",
            retriever=qa_retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": PROMPT},
        )

        docs = qa({"query": question})

        print(docs["result"])

        # Assuming docs["result"] and docs["source_documents"] are what you want to return
        return jsonify({"result": docs["result"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
