# Ad Soyad: Tayfur Tatar
# Öğrenci No: 20253006029

"""Görev 3: galaksi.json ve galaksi_kur() testleri (testler koddan önce yazıldı)."""

import ast
import json
from pathlib import Path

import pytest

from uzay_oyunu.oyun import galaksi_kur, galaksi_yukle, travel

OYUN_DOSYASI = Path(__file__).resolve().parent.parent / "uzay_oyunu" / "oyun.py"
JSON_DOSYASI = OYUN_DOSYASI.with_name("galaksi.json")


def veriyi_oku():
    with open(JSON_DOSYASI, encoding="utf-8") as dosya:
        return json.load(dosya)


def test_ornek_konum_ve_yakit():
    g = galaksi_kur(**veriyi_oku())
    assert (g["konum"], g["yakit"]) == ("dünya", 100)


def test_yakit_verilmezse_varsayilan_elli():
    assert galaksi_kur(["mars"], {"mars": []}, "mars")["yakit"] == 50


def test_yakit_adli_argumanla_verilebilir():
    assert galaksi_kur(["mars"], {"mars": []}, "mars", yakit=7)["yakit"] == 7


def test_baslangic_listede_yoksa_value_error():
    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "venüs")


def test_baglanti_sirasi_eskisiyle_ayni():
    baglantilar = galaksi_kur(**veriyi_oku())["baglantilar"]
    assert baglantilar["dünya"] == ["centauri", "sirius"]
    assert baglantilar["centauri"] == ["dünya", "sirius"]
    assert baglantilar["sirius"] == ["dünya", "centauri", "orion"]
    assert baglantilar["orion"] == ["kara_delik"]
    assert baglantilar["kara_delik"] == []


def test_json_tutarli():
    veri = veriyi_oku()
    gezegenler = set(veri["gezegenler"])
    assert set(veri["baglantilar"]) == gezegenler
    for hedefler in veri["baglantilar"].values():
        assert set(hedefler) <= gezegenler


def test_galaksi_kur_girdiyi_degistirmez():
    gezegenler = ["a", "b"]
    baglantilar = {"a": ["b"], "b": []}
    g = galaksi_kur(gezegenler, baglantilar, "a")
    g["baglantilar"]["a"].append("a")
    assert baglantilar == {"a": ["b"], "b": []}


def test_galaksi_yukle_json_dosyasini_okur():
    assert galaksi_yukle() == veriyi_oku()


def test_travel_hedefleri_galaksiden_alir(monkeypatch, capsys):
    kucuk = galaksi_kur(["a", "b"], {"a": ["b"], "b": []}, "a", yakit=30)
    girdiler = iter(["1"])
    monkeypatch.setattr("builtins.input", lambda _="": next(girdiler))
    travel(kucuk)
    cikti = capsys.readouterr().out
    assert "[1] b" in cikti
    assert "Yakıt: 30" in cikti
    assert "Yakıt: 20" in cikti
    assert "Oyun bitti." in cikti


def test_travel_icinde_elle_yazilmis_destinations_yok():
    agac = ast.parse(OYUN_DOSYASI.read_text(encoding="utf-8"))
    travel_fonksiyonu = next(
        dugum
        for dugum in ast.walk(agac)
        if isinstance(dugum, ast.FunctionDef) and dugum.name == "travel"
    )
    for dugum in ast.walk(travel_fonksiyonu):
        if isinstance(dugum, ast.Assign) and isinstance(dugum.value, ast.List):
            hedefler = [h.id for h in dugum.targets if isinstance(h, ast.Name)]
            assert "destinations" not in hedefler
