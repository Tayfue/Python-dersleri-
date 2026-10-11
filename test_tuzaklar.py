# Ad Soyad: Tayfur Tatar
# Öğrenci No: 20253006029

"""Görev 4: Python tuzakları (değiştirilebilir varsayılan argüman ve kapsam)."""

import pytest

from uzay_oyunu.oyun import yakit_ekle


# ---------------------------------------------------------------- (a) varsayılan argüman


def test_yakit_ekle_her_cagrida_yeni_depo_baslar():
    ilk = yakit_ekle(10)
    ikinci = yakit_ekle(20)
    assert ilk == [10]
    assert ikinci == [20]


def test_yakit_ekle_cagrilar_ayni_listeyi_paylasmaz():
    assert yakit_ekle(1) is not yakit_ekle(2)


def test_yakit_ekle_verilen_depoya_ekler():
    depo = [5]
    sonuc = yakit_ekle(7, depo)
    assert sonuc is depo
    assert depo == [5, 7]


# ---------------------------------------------------------------- (b) kapsam
# Her örneğin çıktısı önce tahmin edildi, sonra çalıştırıldı (bkz. kapsam.md).

yakit_adi = "modül"


def ornek_1():
    yakit_adi = "yerel"
    print(yakit_adi)


def ornek_2():
    sayi = 1

    def ic():
        print(sayi)

    sayi = 2
    ic()


def ornek_3():
    for i in range(3):
        pass
    print(i)
    kareler = [j * j for j in range(3)]  # noqa: F841
    try:
        print(j)
    except NameError as hata:
        print("NameError:", hata)


depo_miktari = 100


def harca_hatali():
    depo_miktari = depo_miktari - 10
    return depo_miktari


def harca_duzgun(depo_miktari: int) -> int:
    return depo_miktari - 10


def test_kapsam_ornek_1_yerel_degisken_modulunkini_golgeler(capsys):
    ornek_1()
    print(yakit_adi)
    assert capsys.readouterr().out == "yerel\nmodül\n"


def test_kapsam_ornek_2_ic_fonksiyon_dis_degiskenin_son_degerini_gorur(capsys):
    ornek_2()
    assert capsys.readouterr().out == "2\n"


def test_kapsam_ornek_3_dongu_kapsam_acmaz_liste_ureteci_acar(capsys):
    ornek_3()
    assert capsys.readouterr().out == "2\nNameError: name 'j' is not defined\n"


def test_unbound_local_error():
    with pytest.raises(UnboundLocalError):
        harca_hatali()


def test_unbound_local_error_duzeltmesi():
    assert harca_duzgun(100) == 90
    assert depo_miktari == 100
