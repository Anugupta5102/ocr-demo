import easyocr
from PIL import Image, ImageEnhance
import streamlit as st
import re
import numpy as np
import gc  # Import garbage collector
from spellchecker import SpellChecker

reader = easyocr.Reader(['en', 'hi'])  # Specify the languages
spell = SpellChecker()

def enhance_image(image):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(2.0)  # Increase contrast

def resize_image(image, max_size=(1024, 1024)):
    """Resize image to reduce memory usage."""
    return image.resize(max_size, Image.ANTIALIAS)

# Function to extract text using EasyOCR
def extract_text_from_image(image):
    try:
        image_np = np.array(image)
        # Use EasyOCR to read the image
        result = reader.readtext(image_np, detail=0)
        # Join the extracted words with a new line
        return "\n".join(result)  # Display each word in a new line
    except Exception as e:
        return f"Error occurred while extracting text: {str(e)}"

# Function to search for keywords in the extracted text
def search_in_text(extracted_text, keyword):
    # Normalize the text and the keyword by removing extra spaces
    normalized_text = extracted_text.strip().replace('\n', ' ').replace('  ', ' ')
    normalized_keyword = keyword.strip()
    
    # Perform the search in the normalized text
    matches = re.finditer(re.escape(normalized_keyword), normalized_text, re.IGNORECASE)
    
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

        enhanced_image = enhance_image(image)
        
        # Extract text from the image
        extracted_text = extract_text_from_image(enhanced_image)
        st.subheader("Extracted Text (Each Word on a New Line):")
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
