# Function to load and extract text from a PDF file using PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
import tempfile

    # Guardar temporalmente el archiv
def load_pdf(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        tmp_file.write(file.getvalue())
        temp_path = tmp_file.name
    try:
        return PyPDFLoader(temp_path)
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None

def extract_text_from_pdf(file):
    # Load the PDF document
    loader = load_pdf(file)

    doc = loader.load()
    content = "".join(char.page_content for char in doc)
    return content

