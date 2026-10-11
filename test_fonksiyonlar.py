# Ad Soyad: Tayfur Tatar
# Öğrenci No: 20253006029

"""Görev 1: saf fonksiyonların testleri (testler koddan önce yazıldı)."""

from uzay_oyunu.oyun import envanter_metni, hedef_menusu


def test_envanter_metni_kredi_ve_pilot():
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"


def test_envanter_metni_bos():
    assert envanter_metni(False, False, False) == ""


def test_envanter_metni_tek_esya():
    assert envanter_metni(False, True, False) == "Sende: güçlü motorlar"


def test_envanter_metni_hepsi():
    beklenen = "Sende: bol kredi, güçlü motorlar, yetenekli bir pilot"
    assert envanter_metni(True, True, True) == beklenen


def test_hedef_menusu():
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(["centauri", "sirius"]) == beklenen


def test_hedef_menusu_bos_liste():
    assert hedef_menusu([]) == "Nereye gitmek istersin?"


def test_hedef_menusu_listeyi_degistirmez():
    hedefler = ["centauri", "sirius"]
    hedef_menusu(hedefler)
    assert hedefler == ["centauri", "sirius"]


def test_fonksiyonlar_saf_print_etmez(capsys):
    envanter_metni(True, True, True)
    hedef_menusu(["centauri", "sirius"])
    assert capsys.readouterr().out == ""
