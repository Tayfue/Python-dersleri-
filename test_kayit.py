# Ad Soyad: Tayfur Tatar
# Öğrenci No: 20253006029

"""Görev 2: gorev_kaydi() için testler (testler koddan önce yazıldı)."""

import pytest

from uzay_oyunu.kayit import gorev_kaydi

BEKLENEN = (
    "[YÜKSEK] Kara deliğe atla\n"
    "  1. Kredi kazan\n"
    "  2. Pilot bul\n"
    "  3. Hiperdrive al\n"
    "  sorumlu: Ayşe"
)


def test_dogrudan_cagri():
    sonuc = gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="yüksek",
        sorumlu="Ayşe",
    )
    assert sonuc == BEKLENEN


def test_liste_ve_sozluk_acilarak_cagri():
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ayarlar = {"oncelik": "yüksek", "sorumlu": "Ayşe"}
    assert gorev_kaydi("Kara deliğe atla", *adimlar, **ayarlar) == BEKLENEN


def test_oncelik_varsayilani_normal():
    assert gorev_kaydi("Yakıt al") == "[NORMAL] Yakıt al"


def test_adimsiz_ve_eklersiz():
    assert gorev_kaydi("Dinlen", oncelik="düşük") == "[DÜŞÜK] Dinlen"


def test_oncelik_yalnizca_adiyla_verilebilir():
    # Konumsal verilen "yüksek", öncelik değil bir adım olarak sayılır.
    sonuc = gorev_kaydi("Görev", "yüksek")
    assert sonuc == "[NORMAL] Görev\n  1. yüksek"


def test_ekler_verilis_sirasiyla_yazilir():
    sonuc = gorev_kaydi("Görev", sorumlu="Ayşe", tarih="yarın")
    assert sonuc.splitlines()[1:] == ["  sorumlu: Ayşe", "  tarih: yarın"]


def test_turkce_buyuk_harf_i():
    assert gorev_kaydi("Görev", oncelik="kritik") == "[KRİTİK] Görev"


def test_baslik_zorunlu():
    with pytest.raises(TypeError):
        gorev_kaydi()  # başlık zorunlu


def test_saf_fonksiyon_print_etmez(capsys):
    gorev_kaydi("Görev", "adım", oncelik="yüksek", sorumlu="Ayşe")
    assert capsys.readouterr().out == ""
