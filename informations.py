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
    for tipInfo in infos.keys():
        person_informations[tipInfo] = infos[tipInfo]


def reset():
    for tipInfo in person_informations.keys():
        person_informations[tipInfo] = ""


JSON_FILE = "static/uploads/saved_infos/infos.json"


def save_json():
    with open(JSON_FILE, 'w') as fp:
        json.dump(person_informations, fp)


signature_file = ""
