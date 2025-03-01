from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

embeddings = OpenAIEmbeddings()

# Example dummy documents for each CDP
documents = [
    {"platform": "Segment", "content": "To set up a new source in Segment, go to Sources > Add Source > Select Source Type."},
    {"platform": "mParticle", "content": "To create a user profile in mParticle, navigate to Users > Create Profile > Enter User Information."},
    {"platform": "Lytics", "content": "To build an audience segment in Lytics, go to Audiences > Create Audience > Set Audience Criteria."},
    {"platform": "Zeotap", "content": "To integrate your data with Zeotap, go to Integrations > Add Integration > Configure API Key."}
]

# Convert documents into text chunks and store in FAISS Vector Database
def load_vectorstore():
    texts = [doc['content'] for doc in documents]
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    split_texts = text_splitter.split_documents(texts)
    vectorstore = FAISS.from_documents(split_texts, embeddings)
    return vectorstore
