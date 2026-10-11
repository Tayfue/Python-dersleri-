# Ad Soyad: Tayfur Tatar
# Öğrenci No: 20253006029

"""Görev 5: hamle_sayaci() ve en_bagli_gezegenler() testleri (önce yazıldı)."""

from uzay_oyunu.araclar import en_bagli_gezegenler, hamle_sayaci
from uzay_oyunu.oyun import galaksi_kur, galaksi_yukle


def test_sayac_her_cagrida_bir_artar():
    sayac = hamle_sayaci()
    assert [sayac(), sayac(), sayac()] == [1, 2, 3]


def test_sayaclar_birbirinden_bagimsiz():
    a = hamle_sayaci()
    b = hamle_sayaci()
    a()
    a()
    assert b() == 1
    assert a() == 3


def test_en_bagli_gezegenler_ornek():
    g = galaksi_kur(**galaksi_yukle())
    assert en_bagli_gezegenler(g) == ["sirius", "centauri", "dünya", "orion", "kara_delik"]


def test_esitlikte_alfabetik_sira():
    g = galaksi_kur(["c", "a", "b"], {"c": ["a"], "a": ["b"], "b": ["c", "a"]}, "a")
    assert en_bagli_gezegenler(g) == ["b", "a", "c"]


def test_baglantisiz_gezegenler_sona_gider():
    g = galaksi_kur(["x", "y"], {"x": [], "y": ["x"]}, "x")
    assert en_bagli_gezegenler(g) == ["y", "x"]


def test_en_bagli_gezegenler_galaksiyi_degistirmez():
    g = galaksi_kur(**galaksi_yukle())
    once = list(g["gezegenler"])
    en_bagli_gezegenler(g)
    assert g["gezegenler"] == once
