import os

from flask import Flask, render_template, request, flash, url_for
from werkzeug.utils import redirect, secure_filename

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


UPLOAD_FOLDER = 'C:/Users/andrei/Downloads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['image_file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
    app.logger.info(uploaded_file.filename)
    return redirect(url_for('upload_file'))


if __name__ == '__main__':
    app.run(debug=True)
