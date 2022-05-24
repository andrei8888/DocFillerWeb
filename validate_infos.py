import re

judete = "(AB)|(AG)|(AR)|(B)|(BC)|(BH)|(BN)|(BR)|(BT)|(BV)|(BZ)|(CJ)|(CL)|(CS)|(CT)|(CV)|(DB)|(DJ)|(GJ)|(GL)|(GR)|(HD)|(HR)|(IF)|(IL)|(IS)|(MH)|(MM)|(MS)|(NT)|(OT)|(PH)|(SB)|(SJ)|(SM)|(SV)|(TL)|(TM)|(TR)|(VL)|(VN)|(VS)"

PAT_nume = re.compile(r"^[A-Za-z ,.'-]+$")
PAT_prenume = re.compile(r"^[A-Za-z ,.'-]+$")
PAT_cetatenie = re.compile(r"^[a-z ,.'-]+$")
PAT_domiciliu = re.compile(r"^[a-z ,.'-]+$")
PAT_emis = re.compile(r"^[a-z ,.'-]+$")
PAT_seria = re.compile(r"^({})$".format(judete))
PAT_nr = re.compile(r"^\d{6}$")
PAT_cnp = re.compile(r"^[1-8]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d")
PAT_sex = re.compile(r"^[FM]$")
PAT_dataNastere = re.compile(r"^((([0-2]\d)|(3[0-1]))\.((0[1-9])|(1[0-2]))\.((19\d\d)|(20[0-2]\d)))$")


def validate(text, pattern):
    return bool(pattern.match(text))


def validate_nume(text):
    return validate(text, PAT_nume)


def validate_prenume(text):
    return validate(text, PAT_prenume)


def validate_cetatenie(text):
    return validate(text, PAT_cetatenie)


def validate_domiciliu(text):
    return validate(text, PAT_domiciliu)


def validate_emis(text):
    return validate(text, PAT_emis)


def validate_seria(text):
    return validate(text, PAT_seria)


def validate_nr(text):
    return validate(text, PAT_nr)


def validate_cnp(text):
    return validate(text, PAT_cnp)


def validate_sex(text):
    return validate(text, PAT_sex)


def validate_dataNastere(text):
    return validate(text, PAT_dataNastere)
