from flask import Flask, render_template, request, jsonify
import pyttsx3
import pytesseract
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.json.get('text')
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return jsonify({'status': 'success'})

@app.route('/image-to-speech', methods=['POST'])
def image_to_speech():
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'No file'}), 400
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    text = pytesseract.image_to_string(Image.open(filepath))
    return jsonify({'text': text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
