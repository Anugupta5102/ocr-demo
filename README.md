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
 
  ```pip install Pillow```
  
  ```pip install streamlit```
  
  ```pip install torch```
  
  ```pip install transformers```

5. Run the application: streamlit run anu.py


## Screenshots

![English Text](Screenshots/english_text.png)
![Hindi Text](Screenshots/hindi_text.png)
![Extracted Text](Screenshots/extracted_text.png)
![Hindi Keyword](Screenshots/hindi_keyword.png)
![OCR App](Screenshots/ocr_app.png)
![Search Results](Screenshots/search_results.png)
![Words](Screenshots/words.png)



## [Check out the OCR Demo App here!](https://ocr-demo-2.streamlit.app/)


## License:
This project is licensed under the MIT License.
