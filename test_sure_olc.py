# Ad Soyad: Tayfur Tatar
# Öğrenci No: 20253006029

"""Bonus: sure_olc() sarmalayıcısının testleri (önce yazıldı)."""

import pytest

from uzay_oyunu.araclar import en_bagli_gezegenler, sure_olc
from uzay_oyunu.oyun import galaksi_kur, galaksi_yukle


def test_sonucu_aynen_dondurur():
    topla = sure_olc(lambda a, b: a + b)
    assert topla(2, 3) == 5


def test_konumsal_ve_adli_argumanlari_iletir():
    def birlestir(*parcalar, ayirac="-"):
        return ayirac.join(parcalar)

    sarili = sure_olc(birlestir)
    assert sarili("a", "b", "c", ayirac="+") == "a+b+c"


def test_sureyi_yazar(capsys):
    def hizli():
        return 1

    sure_olc(hizli)()
    cikti = capsys.readouterr().out
    assert "hizli" in cikti
    assert "sn" in cikti


def test_fonksiyon_adi_ve_docstring_korunur():
    def ornek():
        """Örnek belge."""

    sarili = sure_olc(ornek)
    assert sarili.__name__ == "ornek"
    assert sarili.__doc__ == "Örnek belge."


def test_en_bagli_gezegenler_ile_deneme(capsys):
    olculu = sure_olc(en_bagli_gezegenler)
    g = galaksi_kur(**galaksi_yukle())
    assert olculu(g) == ["sirius", "centauri", "dünya", "orion", "kara_delik"]
    assert "en_bagli_gezegenler" in capsys.readouterr().out


def test_istisna_yine_de_yukselir():
    def hata():
        raise ValueError("kasıtlı")

    with pytest.raises(ValueError, match="kasıtlı"):
        sure_olc(hata)()
