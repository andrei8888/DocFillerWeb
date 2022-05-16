import os

from flask import Flask, render_template, request, flash, url_for, jsonify
from werkzeug.utils import redirect, secure_filename

app = Flask(__name__)


@app.route('/')
def go_to_home():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/scan', methods=['GET', 'POST'])
def scan():
    return render_template('scan.html')


@app.route('/doc')
def doc():
    return render_template('doc.html')


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/home', methods=['POST'])
def upload_file():
    uploaded_file = request.files['image_file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
    return render_template('home.html', filePhoto='uploads/'+uploaded_file.filename)


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/background_process_test', methods=['POST'])
def background_process_test():
    app.logger.info("da")
