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
    for pdf_file in pdfs_folder:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(pdf_file.read())


        loader = PyPDFLoader(temp_path)
        docs = loader.load_and_split()
        combined_docs.extend(docs)  

        os.remove(temp_path)


    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(combined_docs)    
    return summary


st.title("Summerize-text-Into-Smaller-Chunks")


pdf_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if pdf_files:
   
    if st.button("Generate Summary"):
        st.write("Combined summary:")
        combined_summary = summarize_combined_pdfs(pdf_files)
        st.write(combined_summary)
