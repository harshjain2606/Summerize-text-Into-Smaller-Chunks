from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader
from langchain import OpenAI
import streamlit as st
import tempfile
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
print("key="+os.getenv("OPENAI_API_KEY"))
llm = OpenAI(temperature=0)

def summarize_combined_pdfs(pdfs_folder):
    combined_docs = []
# Each uploaded PDF file is written to a temporary file to facilitate reading and processing.
# Each temp_file is used to temporarily hold the content of a single PDF file at a time
    for pdf_file in pdfs_folder:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(pdf_file.read())

# PyPDFLoader reads and splits the PDF content into manageable chunks.
        loader = PyPDFLoader(temp_path)
        docs = loader.load_and_split()
        combined_docs.extend(docs)  # Combine docs from each PDF
# The result is the list of documents (docs), where each entry in the list represents a part of the PDF file. 
        
        # Delete the temporary file
        os.remove(temp_path)

# Summarize the combined documents
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(combined_docs)    
    return summary

# Streamlit App
st.title("Combined PDF Summarizer")

# Allow user to upload PDF files
pdf_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if pdf_files:
    # Generate summaries when the "Generate Summary" button is clicked
    if st.button("Generate Summary"):
        st.write("Combined summary:")
        combined_summary = summarize_combined_pdfs(pdf_files)
        st.write(combined_summary)