# Support Agent Chatbot

### Overview
This chatbot is designed to answer "How-to" questions for four Customer Data Platforms (**CDPs**):
- **Segment**
- **mParticle**
- **Lytics**
- **Zeotap**

It helps users by providing step-by-step instructions extracted from platform documentation.

### Features
✅ Answers "How-to" questions for each CDP.
✅ Retrieves information from documentation.
✅ Handles different question variations.
✅ Interactive API Documentation with Swagger UI

### Tech Stack
| Technology | Purpose               |
|------------|----------------------|
| Python     | Backend Development |
| Flask      | API Framework       |
| LangChain  | NLP & Question Answering |
| FAISS      | Vector Search       |
| OpenAI API | Language Model      |
| Flasgger   | Swagger API Documentation |

### Prerequisites
- **Python 3.8+**
- **OpenAI API Key**

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/support-agent-chatbot.git
   cd support-agent-chatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API Key:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   ```
4. Start the chatbot:
   ```bash
   python app.py
   ```

### How to Use
Visit Swagger UI:
```
http://localhost:5000/apidocs/
```

Make a **POST** request to the `/ask` endpoint with the following JSON body:
```json
{
  "question": "How do I set up a new source in Segment?"
}
```

Example Response:
```json
{
  "answer": "To set up a new source in Segment, go to Sources > Add Source > Select Source Type."
}
```

### License
This project is licensed under the **MIT License**.
