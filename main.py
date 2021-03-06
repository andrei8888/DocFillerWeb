import os
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

import fetch_docs
import informations
import scan_for_infos

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    informations.reset()
    informations.save_json()
    return render_template('home.html')


@app.route('/doc')
def doc():
    docs, docs_number = fetch_docs.fetch_titles_and_number()
    return render_template('doc.html', len=docs_number, docs=docs)


@app.route('/down')
def down():
    return render_template('down.html')


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
    scan_for_infos.set_infos_from_image(uploaded_file)
    informations.save_json()
    return render_template('home.html')


@app.route('/home/info', methods=['POST'])
def get_info_from_web():
    infos = request.json
    informations.set_informations(infos)
    informations.save_json()
    return render_template('home.html')


@app.route('/home/photoSignature', methods=['POST'])
def get_sign_from_web():
    uploaded_signature = request.files['imageSignature']
    if uploaded_signature.filename != '':
        uploaded_signature.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_signature.filename))
    informations.signature_file = uploaded_signature.filename
    return render_template('home.html')


@app.route('/doc/next', methods=['POST'])
def prepare_docs():
    fetch_docs.clean_docs_completed()
    docs = request.get_json()
    fetch_docs.manage_documents(docs)
    return redirect(url_for("down"))


if __name__ == '__main__':
    app.run(debug=True)
