# OCR Web Application with Hindi and English Text Extraction

This web application allows users to upload images containing text in both Hindi and English. The app extracts text using OCR and provides a keyword search functionality to search within the extracted text.

## Features:
- Upload an image (JPEG, PNG).
- Extract text from images using Tesseract OCR.
- Search for specific keywords in the extracted text.

## How to Run Locally:

1. Clone this repository: git clone <repository-url>

2. Install the required Python packages: pip install -r requirements.txt
 
3. Install Tesseract OCR:
- On Ubuntu:
  ```
  sudo apt-get install tesseract-ocr
  ```
- On Windows, download and install [Tesseract](https://github.com/tesseract-ocr/tesseract/wiki).
4. Install required dependencies and libraries.
  
  ```pip install pytesseract```
 
  ```pip instal Pillow```
  
  ```pip install streamlit```
  
  ```pip install torch```
  
  ```pip install transformers```

5. Run the application: streamlit run app.py

## Deployment:

This app is deployed and can be accessed at: **[https://bookish-goggles-vxw6xjgxpx7266v4-8501.app.github.dev/]**

## License:
This project is licensed under the MIT License.
