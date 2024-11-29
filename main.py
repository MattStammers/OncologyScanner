# Flask app
from flask import Flask, render_template, request, redirect, url_for
from extract_text_from_pdf import extract_text_from_pdf 
#from analyse_text import analyse_text

# Set environment variables in script
import os

#from sparknlp.pretrained import PretrainedPipeline
#from pyspark.sql import SparkSession

#import sparknlp

# Flask object
app = Flask(__name__)

# Folder to save uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Make sure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Route to render form
@app.route('/')
def home():
    return render_template('form.html')

# Route to handle form submission
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file.'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No file selected.'
    
    if file and file.filename.endswith('.pdf'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Extract text from PDF
        text = extract_text_from_pdf(file_path)
        
        # Analyse text with spark-nlp
        #extracted_info = analyse_text(text)
        
        # For now, we just display the extracted text
        #return render_template('display_extracted_info.html', extracted_info=extracted_info)
        return render_template('display_text.html', extracted_text=text)
        #return f'File "{file.filename}" uploaded.'
    
    return 'Invalid file format. Please upload PDF.'
    
if __name__ == '__main__':
    app.run()
