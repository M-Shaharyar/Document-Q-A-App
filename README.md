# Document Q&A System

 A web-based application that enables users to ask questions and retrieve answers from uploaded PDF documents using Streamlit, LangChain, FAISS, and Google Generative AI. 
 This app is ideal for document analysis, context-based Q&A, and summarization, making document navigation more efficient.

 ## 🚀 Features

*  Upload PDF Documents: Supports document ingestion by loading PDF files from a specified directory.
*  AI-Powered Document Analysis: Utilizes Google Generative AI embeddings and GROQ language models to interpret and process document content.
*  Document Embeddings: Creates vector embeddings of document content for efficient information retrieval.
*  Contextual Q&A: Allows users to ask questions and retrieve precise answers based on document context.
*  Document Similarity Search: Shows similar document sections related to the user's query for added context.
*  User-Friendly Interface: Built with Streamlit for a simple and interactive user experience.

## 🛠️ Tech Stack

*  Python: Core programming language used for development.
*  Streamlit: Framework for building the web-based interface.
*  LangChain: For text processing and document handling.
*  FAISS: For efficient vector similarity search.
*  Google Generative AI Embeddings: For embedding generation to represent document content in vector form.
*  dotenv: For securely loading environment variables.

## 📦 Installation

### Clone the Repository:
```
 git clone https://github.com/M-Shaharyar/Document-Q-A-App.git
 cd Document-Q-A-App
```

### Create a Virtual Environment:
```
python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate     # For Windows
```

### Install Required Packages:
```
pip install -r requirements.txt
```
### Set Up Environment Variables:

 1. Create a `.env` file in the project directory.
 2. Add your API keys to the `.env` file as follows:
```
 GROQ_API_KEY=your_groq_api_key
 GOOGLE_API_KEY=your_google_api_key
```
## 🖼️ Usage

### Run the Application:
```
streamlit run app.py
```
1. Load Documents: Ensure your PDF documents are saved in the `./us_census` directory for ingestion.
2. Embed Documents: Click the **Documents Embedding** button to create document embeddings in the vector database.
3. Ask a Question: Enter a question related to the document content and get precise answers based on context.
4. View Document Similarity: Use the "Document Similarity Search" option to see other document sections related to your query.

## 📝 Example Input

*  Input Prompt: "What is the total population in the report?"
*  Document: An uploaded PDF containing census data.

## 📄 Example Output

*  Response: "The total population recorded is 330 million."

# ---
## About
* A Q&A web application powered by AI to help users navigate, analyze, and retrieve information from large documents. 
* Built using Streamlit and Google Generative AI embeddings.
