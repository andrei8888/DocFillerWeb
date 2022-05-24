person_informations = {
    "nume": "",
    "prenume": "",
    "cetatenie": "",
    "domiciliu": "",
    "emis": "",
    "seria": "",
    "nr": "",
    "cnp": "",
    "sex": "",
    "dataNastere": ""
}


def set_informations(infos):
    person_informations['nume'] = infos['nume']
    person_informations['prenume'] = infos['prenume']
    person_informations['cetatenie'] = infos['cetatenie']
    person_informations['emis'] = infos['emis']
    person_informations['seria'] = infos['seria']
    person_informations['nr'] = infos['nr']
    person_informations['cnp'] = infos['cnp']
    person_informations['sex'] = infos['sex']
    person_informations['dataNastere'] = infos['dataNastere']
