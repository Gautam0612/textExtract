from flask import Flask,jsonify,request
import os
from PIL import Image
from pytesseract import pytesseract

app = Flask(__name__)

@app.route('/',methods=["POST"])
def imageProcess():
    try:
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        image_file = request.files['image']
        temp_image_path = 'temp_image.png'
        image_file.save(temp_image_path)
        img = Image.open(temp_image_path)
        pytesseract.tesseract_cmd = path_to_tesseract

        text = pytesseract.image_to_string(img)
        os.remove(temp_image_path)
        return jsonify({"message":text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        
        
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
