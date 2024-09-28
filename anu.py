import pytesseract
import easyocr
from PIL import Image
import streamlit as st
import re
import numpy as np

reader = easyocr.Reader(['en', 'hi'])  # Specify the languages

# Function to extract text using Tesseract
def extract_text_from_image(image):
    try:
         image_np = np.array(image)
        extracted_text = reader.readtext(image_np)
        text = " ".join([result[1] for result in extracted_text])
        return text
    except Exception as e:
        return f"Error occurred while extracting text: {str(e)}"

# Function to search for keywords in the extracted text
def search_in_text(extracted_text, keyword):
    matches = re.finditer(keyword, extracted_text, re.IGNORECASE)
    highlighted_text = extracted_text
    
    for match in matches:
        start, end = match.span()
        highlighted_text = (highlighted_text[:start] + f"<mark>{highlighted_text[start:end]}</mark>" + highlighted_text[end:])
    
    if "<mark>" in highlighted_text:
        return highlighted_text
    return None

# Main app with Streamlit
def main():
    st.title("OCR for Hindi and English Text")
    
    st.write("""
    Upload an image that contains both Hindi and English text, and this app will extract the text using OCR.
    You can also search for specific keywords in the extracted text.
    """)

    # File upload
    uploaded_image = st.file_uploader("Upload an image", type=['jpeg', 'png', 'jpg'])
    
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        # Extract text from the image
        extracted_text = extract_text_from_image(image)
        st.subheader("Extracted Text:")
        st.text(extracted_text)
        
        # Keyword Search
        search_keyword = st.text_input("Enter a keyword to search within the text")
        
        if search_keyword:
            search_results = search_in_text(extracted_text, search_keyword)
            if search_results:
                st.subheader(f"Search Results for '{search_keyword}':")
                st.markdown(search_results, unsafe_allow_html=True)
            else:
                st.write(f"No matches found for '{search_keyword}'.")

if __name__ == "__main__":
    main()
