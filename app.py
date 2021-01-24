from flask import Flask, render_template, redirect, url_for, request, send_from_directory
import os
from faceblur import process_video


app = Flask(__name__)

pwd = os.getcwd()
app.config['UPLOAD_FOLDER'] = os.path.join(pwd, 'uploads')
app.config['DOWNLOAD'] =  os.path.join(pwd, 'finished')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'video' not in request.files:
            return redirect(request.url)
        file = request.files['video']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            temp_path = os.path.join(pwd, 'temp')
            out_path =  os.path.join(pwd, 'finished', 'out.mp4')
            process_video(input_path, out_path, temp_path)
            return send_from_directory(app.config['DOWNLOAD'], filename="out.mp4", as_attachment=True)
    return  render_template('/pages/upload.html')


