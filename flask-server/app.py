from flask import Flask, request, jsonify, send_from_directory
import os
import sys
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_video():
    file = request.files['video']
    language = request.form['language']
    filename = file.filename
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    output_filename = filename.rsplit('.', 1)[0] + '_dubbed.mp4'
    output_path = os.path.join(PROCESSED_FOLDER, output_filename)

    file.save(input_path)

    try:
        subprocess.run([
            sys.executable,  # ensures the subprocess uses the current Python from run-env
            'dubber.py', input_path, output_path, language
        ], check=True)

    except subprocess.CalledProcessError:
        return jsonify({'error': 'Dubbing failed'}), 500

    return jsonify({'processed_filename': output_filename})

@app.route('/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory(PROCESSED_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
