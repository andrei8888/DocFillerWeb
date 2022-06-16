import os
import re
from datetime import datetime
from difflib import SequenceMatcher

import process
import pytesseract
import informations

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'


def clear_string(text):
    text = os.linesep.join([s for s in text.splitlines() if s])
    text = "\n".join([ll.rstrip() for ll in text.splitlines() if ll.strip()])
    return text


def get_scanned_string(path):
    image = process.open_and_preproc(path)
    image = process.crop_to_infos(image)
    image = process.resize_with_scale(image, 160)
    return clear_string(pytesseract.image_to_string(image, lang='ron'))


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


PAT_serie_nr = re.compile(r"^.* [A-Z]{2} .* \d{6} .*$")
PAT_serie = re.compile(" (B|[A-Z]{2}) ")
PAT_nr = re.compile(" \d{6} ")
PAT_cnp_line = re.compile("(.* [1-8]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d)")
PAT_cnp = re.compile("[1-8]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d")
SIM_nume = "Nume/Nom/Last name"
SIM_prenume = "Prenume/Prenom/First name"
SIM_cetatenie = "Cetatenie/Nationalite/Nationality"
SIM_locNastere = "Loc nastere/Lieu de naissance/Place of birth Sex/Sexe/Sex"
SIM_domiciliu = "Domiciliu/Adresse/Adress"
SIM_emis_line = "Emisa de/Deliveree par/Issued by"
PAT_dataEliberare = re.compile(" ([\d. ]*-)")
PAT_dataNastere = re.compile("-((([0-2]\d)|(3[0-1]))\.((0[1-9])|(1[0-2]))\.((19\d\d)|(20[0-2]\d)))")
PAT_data_line = re.compile("(( (([0-2]\d)|(3[0-1]))\.((0[1-9])|(1[0-2]))\.(\d\d)|([0-2]\d))-((([0-2]\d)|(3[0-1]))\.((0[1-9])|(1[0-2]))\.((19\d\d)|(20[0-2]\d))))")
PAT_emis = re.compile("[-a-zăîșțâA-ZĂÎȘȚÂ ]*")

def get_infos_from_string(text):
    text_as_array = text.splitlines()
    ind_line = enumerate(text_as_array)
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
    for index, line in ind_line:
        if PAT_serie_nr.match(line):
            if PAT_serie.search(line):
                person_informations["seria"] = PAT_serie.search(line).group().strip()
            if PAT_nr.search(line):
                person_informations["nr"] = PAT_nr.search(line).group().strip()
            continue
        if PAT_cnp_line.match(line):
            person_informations["cnp"] = PAT_cnp.search(line).group().strip()
            if person_informations["cnp"][0] in ("1", "3", "5", "7"):
                person_informations["sex"] = "Masculin"
            else:
                person_informations["sex"] = "Feminin"
            person_informations["dataNastere"] = datetime.strptime(person_informations["cnp"][1:7], "%y%m%d").strftime("%d.%m.%Y")
            continue
        if similar(line, SIM_nume) > 0.7:
            person_informations["nume"] = text_as_array[index+1].strip()
            continue
        if similar(line, SIM_prenume) > 0.7:
            person_informations["prenume"] = text_as_array[index+1].strip()
            continue
        if similar(line, SIM_cetatenie) > 0.4:
            person_informations["cetatenie"] = text_as_array[index+1].strip()
            continue
        if similar(line, SIM_locNastere) > 0.7:
            person_informations["locNastere"] = text_as_array[index+1].strip()
            continue
        if similar(line, SIM_domiciliu) > 0.7:
            person_informations["domiciliu"] = text_as_array[index+1].strip() + '\n' + text_as_array[index+2].strip()
            continue
        if similar(line, SIM_emis_line) > 0.5:
            person_informations["emis"] = PAT_emis.search(text_as_array[index+1]).group()
            person_informations["dataEliberare"] = PAT_dataEliberare.search(text_as_array[index+1]).group().strip()[:-1]
            continue
    return person_informations


def set_infos_from_image(path):
    informations.set_informations(get_infos_from_string(get_scanned_string("static/uploads/" + path.filename)))
