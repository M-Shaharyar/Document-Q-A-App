# Import necessary libraries
import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API keys for GROQ and Google Generative AI
groq_api_key = os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Set the title of the Streamlit application
st.title("Document Q&A")

# Initialize the language model with GROQ API key and a specific model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Define the prompt template for answering questions based on context
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question.
    <context>
    {context}
    <context>
    Questions: {input}
    """
)

# Function to perform vector embedding
def vector_embedding():
    # Check if vector embeddings have already been created in the current session
    if "vectors" not in st.session_state:
        # Initialize embeddings model
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        
        # Load PDF documents from a specific directory
        st.session_state.loader = PyPDFDirectoryLoader("./us_census")
        st.session_state.docs = st.session_state.loader.load()
        
        # Split documents into chunks with specific size and overlap
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:20])
        
        # Create a vector store using FAISS for the document embeddings
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

# Input field for user to enter a question related to the documents
prompt1 = st.text_input("Enter Your Question From Documents")

# Button to trigger document embedding
if st.button("Documents Embedding"):
    vector_embedding()
    st.write("Vector Store DB Is Ready")


# If the user has entered a question
if prompt1:
    # Create a document retrieval chain with the language model and the prompt template
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    # The retrieval and answer generation
    response = retrieval_chain.invoke({'input': prompt1})
    
    # Display the answer to the user's question
    st.write(response['answer'])

    # With a Streamlit expander, display similar document content
    with st.expander("Document Similarity Search"):
        # Loop through each relevant document chunk in the response
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")
