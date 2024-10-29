import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from utils import extract_text_from_pdf
import requests
import json
from _settings import BILL_AI_URL

st.title("Drag and Drop PDF File")

# Create a column for the file uploader
file_uploader_column = st.columns(1)[0]

with file_uploader_column:
    uploaded_file = st.file_uploader(
        "Upload a PDF file",
        type="pdf",
        accept_multiple_files=False,
        key="pdf_uploader"
    )
if uploaded_file is not None:
    # Process the uploaded file
    pdf_text = extract_text_from_pdf(uploaded_file)
    pdf_viewer(uploaded_file.getvalue())
    payload = {
    "bill_str": pdf_text
    }


import streamlit as st
import requests
import json


if st.button("Process"):
    with st.spinner("Doing Science..."):
        response = requests.post(BILL_AI_URL, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            st.success("Proceso completado con éxito!")
            st.json(response.json())
        else:
            st.error(f"Error al procesar la solicitud: {response.status_code}")


