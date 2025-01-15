
<h1 align="center"> Automated PDF Document Summarization Using LangChain and OpenAI</h1>

**Project Overview:**  
Developed a web-based application using Streamlit, LangChain, and OpenAI's language model to automate the summarization of content across multiple PDF documents. This tool leverages advanced natural language processing techniques to efficiently extract key information from large volumes of text, making it ideal for professionals who need to digest large reports or documents quickly.

![image](https://github.com/user-attachments/assets/5f2ba44e-2488-449d-b23d-5d61b59288f4)


**Key Features:**
Multi-Document Summarization: Supports summarization of multiple PDF files simultaneously, combining the content into a cohesive summary.  
Streamlit Integration: Provides a user-friendly web interface where users can upload multiple PDF files, and with a single click, generate a combined summary.  
PDF Content Processing: Utilized PyPDFLoader to read and split PDF content into manageable chunks, ensuring accurate and efficient processing.  
OpenAI Integration: Leveraged OpenAI's API to perform the summarization task, ensuring high-quality summaries with coherent and concise outputs.  

**Technical Stack:**   
Python: Primary programming language used for the development of the application.  
LangChain: Employed to facilitate the summarization process using a chain-type "map_reduce" method.  
OpenAI: Integrated via API for language model processing.  
Streamlit: Used for building the web interface, allowing users to interact with the summarization tool directly from their browser.  
PyPDFLoader: Responsible for reading and splitting PDF documents into smaller chunks for processing.  

**Challenges Overcome:**  
Efficient PDF Handling: Managed the challenges of processing large PDF documents by implementing a method to handle files temporarily, ensuring that the application can scale to process multiple documents without memory overload.  
Accurate Summarization: Fine-tuned the summarization process to balance detail with brevity, ensuring that key information is retained in the output summary.  

**Outcome:**   
Successfully developed and deployed an application that automates the summarization of multiple PDF documents, significantly reducing the time required to analyze large text-based reports.  

**Demo link:**   
https://drive.google.com/file/d/1KzA0ZsLfSVzQddmIIYxbo1tf2bUUhSgN/view?usp=drive_link
