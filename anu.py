import easyocr
from PIL import Image, ImageEnhance, ImageOps
import streamlit as st
import re
import numpy as np
import gc  # Import garbage collector
from spellchecker import SpellChecker

# Function to enhance and resize the image to reduce memory usage
def preprocess_image(image, max_size=(1024, 1024)):
    try:
        # Convert to grayscale to reduce memory usage
        image = ImageOps.grayscale(image)
        # Resize the image to a smaller size using LANCZOS
        image = image.resize(max_size, Image.LANCZOS)
        return image
    except Exception as e:
        return None  # Return None in case of error

# Function to extract text using EasyOCR
def extract_text_from_image(image):
    try:
        reader = easyocr.Reader(['en', 'hi'], gpu=False)  # Load OCR reader only when needed
        image_np = np.array(image)
        # Use EasyOCR to read the image
        result = reader.readtext(image_np, detail=0)
        # Free up memory after OCR processing
        gc.collect()
        return "\n".join(result)  # Display each word on a new line
    except Exception as e:
        return f"Error occurred while extracting text: {str(e)}"

# Function to search for keywords in the extracted text
def search_in_text(extracted_text, keyword):
    normalized_text = extracted_text.strip().replace('\n', ' ').replace('  ', ' ')
    normalized_keyword = keyword.strip()
    
    # Perform the search
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
    st.title("Optimized OCR for Hindi and English Text")
    
    st.write("""
    Upload an image that contains both Hindi and English text, and this app will extract the text using OCR.
    You can also search for specific keywords in the extracted text.
    """)

    # File upload
    uploaded_image = st.file_uploader("Upload an image", type=['jpeg', 'png', 'jpg'])
    
    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Preprocess the image (resize and convert to grayscale)
        preprocessed_image = preprocess_image(image)
        
        if preprocessed_image is not None:  # Check if preprocessing was successful
            # Extract text from the image
            extracted_text = extract_text_from_image(preprocessed_image)
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
        else:
            st.error("Error processing image. Please upload a valid image.")

        # Free up memory after the process
        del image, preprocessed_image
        gc.collect()

if __name__ == "__main__":
    main()


