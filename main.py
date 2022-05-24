import os

from flask import Flask, render_template, request, flash, url_for, jsonify, json
from werkzeug.utils import redirect, secure_filename

app = Flask(__name__)


@app.route('/')
def go_to_home():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/doc')
def doc():
    return render_template('doc.html')


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/home/photoUpload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['image_file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
    return render_template('home.html')


@app.route('/home/info', methods=['POST'])
def get_info():
    infos = request.json
    app.logger.info(infos)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
