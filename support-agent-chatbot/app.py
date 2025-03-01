import os
from flask import Flask, request, jsonify
from langchain import OpenAI
from langchain.chains import ConversationalRetrievalChain
from vectorstore import load_vectorstore
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

# Initialize OpenAI API
os.environ['OPENAI_API_KEY'] = 'your_openai_api_key'
llm = OpenAI()
vectorstore = load_vectorstore()
retriever = vectorstore.as_retriever()
qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever)

@app.route('/ask', methods=['POST'])
def ask():
    """
    Ask a "How-to" Question
    ---
    tags:
      - Chatbot
    parameters:
      - name: question
        in: body
        required: true
        schema:
          type: object
          properties:
            question:
              type: string
              example: "How do I set up a new source in Segment?"
    responses:
      200:
        description: Successful response
        schema:
          type: object
          properties:
            answer:
              type: string
      400:
        description: Bad Request (Missing question)
    """
    data = request.json
    question = data.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    result = qa_chain.run(question)
    return jsonify({"answer": result})

@app.route('/')
def home():
    return "Support Agent Chatbot API is running! Use /ask endpoint to ask questions."

if __name__ == '__main__':
    app.run(debug=True)
