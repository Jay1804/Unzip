import streamlit as st
import zipfile
import io

# Function to extract zip contents in memory
def extract_zip(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # Create a dictionary to hold the extracted files
        extracted_files = {}
        for file_name in zip_ref.namelist():
            with zip_ref.open(file_name) as file:
                extracted_files[file_name] = file.read()
        return extracted_files

# Streamlit app layout
st.title('Upload and Extract Multiple ZIP Files')

# Upload zip files
uploaded_files = st.file_uploader("Choose ZIP files", type="zip", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.write(f"Uploaded file: {uploaded_file.name}")
        
        # Extract the contents of the uploaded zip file
        extracted_files = extract_zip(uploaded_file)
        
        # Show the extracted file names and allow the user to download them
        for file_name, file_content in extracted_files.items():
            st.write(f"File: {file_name}")
            
            # Allow user to download the file
            st.download_button(
                label="Download " + file_name,
                data=file_content,
                file_name=file_name,
                mime="application/octet-stream"
            )
