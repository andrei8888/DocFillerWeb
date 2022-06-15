import os
import re
import shutil
from datetime import date

from docx import Document

import informations

DOCS_PATH = "static/docs/"
DOCS_TEMPLATES_PATH = DOCS_PATH + "doc_templates/"
DOCS_UPLOAD_PATH = "static/uploads/docs_completed/"
FINAL_ZIP_NAME = "Documente_completate"
FINAL_ZIP_NAME_EXT = FINAL_ZIP_NAME + ".zip"


def fetch_titles_and_number():
    list_docs = [os.path.splitext(filename)[0] for filename in os.listdir(DOCS_PATH) if
                 os.path.isfile(os.path.join(DOCS_PATH, filename))]
    # print(list_docs)
    return list_docs, len(list_docs)


def docx_replace_regex(doc_obj, regex, replace):
    for p in doc_obj.paragraphs:
        if regex.search(p.text):
            inline = p.runs
            for i in range(len(inline)):
                if regex.search(inline[i].text):
                    text = regex.sub(replace, inline[i].text)
                    inline[i].text = text


def get_current_date():
    return date.today().strftime("%d.%m.%Y")


def replace_with_infos(doc_obj, infos):
    id_char = "@"
    docx_replace_regex(doc_obj, re.compile(id_char+"nume"), infos["nume"])
    docx_replace_regex(doc_obj, re.compile(id_char+"prenume"), infos["prenume"])
    docx_replace_regex(doc_obj, re.compile(id_char+"cetatenie"), infos["cetatenie"])
    docx_replace_regex(doc_obj, re.compile(id_char+"locNastere"), infos["locNastere"])
    docx_replace_regex(doc_obj, re.compile(id_char+"domiciliu"), infos["domiciliu"].replace("\n", " "))
    docx_replace_regex(doc_obj, re.compile(id_char+"emis"), infos["emis"])
    docx_replace_regex(doc_obj, re.compile(id_char+"seria"), infos["seria"])
    docx_replace_regex(doc_obj, re.compile(id_char+"nr"), infos["nr"])
    docx_replace_regex(doc_obj, re.compile(id_char+"cnp"), infos["cnp"])
    docx_replace_regex(doc_obj, re.compile(id_char+"sex"), infos["sex"])
    docx_replace_regex(doc_obj, re.compile(id_char+"dataNastere"), infos["dataNastere"])
    docx_replace_regex(doc_obj, re.compile(id_char+"dataEliberare"), infos["dataEliberare"])
    docx_replace_regex(doc_obj, re.compile(id_char+"dataCurenta"), get_current_date())


def manage_doc_and_save(doc_name, infos):
    curr_doc = Document(DOCS_PATH + "/doc_templates/" + doc_name)
    replace_with_infos(curr_doc, infos)
    curr_doc.save(DOCS_UPLOAD_PATH + doc_name)


def make_zip():
    shutil.make_archive(FINAL_ZIP_NAME, 'zip', DOCS_UPLOAD_PATH)
    shutil.move(FINAL_ZIP_NAME_EXT, DOCS_UPLOAD_PATH + FINAL_ZIP_NAME_EXT)


def clean_docs_completed():
    for f in os.listdir(DOCS_UPLOAD_PATH):
        os.remove(os.path.join(DOCS_UPLOAD_PATH, f))


def manage_documents(docs):
    for doc_title in docs.values():
        manage_doc_and_save(doc_title + ".docx", informations.person_informations)

    make_zip()
