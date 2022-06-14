import json

person_informations = {
    "nume": "",
    "prenume": "",
    "cetatenie": "",
    "locNastere": "",
    "domiciliu": "",
    "emis": "",
    "seria": "",
    "nr": "",
    "cnp": "",
    "sex": "",
    "dataNastere": "",
    "dataEliberare": ""
}


def set_informations(infos):
    person_informations['nume'] = infos['nume']
    person_informations['prenume'] = infos['prenume']
    person_informations['cetatenie'] = infos['cetatenie']
    person_informations['locNastere'] = infos['locNastere']
    person_informations['domiciliu'] = infos['domiciliu']
    person_informations['emis'] = infos['emis']
    person_informations['seria'] = infos['seria']
    person_informations['nr'] = infos['nr']
    person_informations['cnp'] = infos['cnp']
    person_informations['sex'] = infos['sex']
    person_informations['dataNastere'] = infos['dataNastere']


def reset():
    person_informations['nume'] = ""
    person_informations['prenume'] = ""
    person_informations['cetatenie'] = ""
    person_informations['locNastere'] = ""
    person_informations['domiciliu'] = ""
    person_informations['emis'] = ""
    person_informations['seria'] = ""
    person_informations['nr'] = ""
    person_informations['cnp'] = ""
    person_informations['sex'] = ""
    person_informations['dataNastere'] = ""


other_infos = {
    "": ""
}

JSON_FILE = "static/uploads/saved_infos/infos.json"


def save_json():
    with open(JSON_FILE, 'w') as fp:
        json.dump(person_informations, fp)
