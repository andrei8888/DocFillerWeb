import pytest

import validate_infos


def test_validate_nume():
    assert (validate_infos.validate_nume("Brusli")) == True


def test_invalidate_nume():
    assert (validate_infos.validate_nume("Brusli@")) == False


def test_validate_sex1():
    assert (validate_infos.validate_sex("F")) == True


def test_validate_sex2():
    assert (validate_infos.validate_sex("M")) == True


def test_invalidate_sex3():
    assert (validate_infos.validate_sex("X")) == False


def test_validate_dataNastere():
    assert (validate_infos.validate_dataNastere("12.12.2022")) == True


def test_invalidate_dataNastere_d():
    assert (validate_infos.validate_dataNastere("33.02.2022")) == False


def test_invalidate_dataNastere_m1():
    assert (validate_infos.validate_dataNastere("30.00.2022")) == False


def test_invalidate_dataNastere_m2():
    assert (validate_infos.validate_dataNastere("30.13.2022")) == False


def test_invalidate_dataNastere_y1():
    assert (validate_infos.validate_dataNastere("30.01.1899")) == False


def test_invalidate_dataNastere_y2():
    assert (validate_infos.validate_dataNastere("30.01.0212")) == False


def test_invalidate_dataNastere_y3():
    assert (validate_infos.validate_dataNastere("30.01.2002")) == True


def test_validate_dataNastere_y4():
    assert (validate_infos.validate_dataNastere("30.01.1900")) == True


def test_invalidate_dataNastere_y5():
    assert (validate_infos.validate_dataNastere("30.01.2030")) == False
