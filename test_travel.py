# Ad Soyad: Tayfur Tatar
# Öğrenci No: 20253006029

"""travel() için davranış testleri (Hafta 2'den beri var, refaktörde bozulmamalı)."""

from uzay_oyunu.oyun import travel


def oyunu_oyna(monkeypatch, capsys, secimler):
    """travel()'ı verilen seçimlerle çalıştırır ve ekrana yazılanı döndürür."""
    girdiler = iter(secimler)
    monkeypatch.setattr("builtins.input", lambda _="": next(girdiler))
    travel()
    return capsys.readouterr().out


def test_kara_deligin_yolu_oyunu_bitirir(monkeypatch, capsys):
    # dünya -> sirius (2) -> orion (3) -> kara_delik (1)
    cikti = oyunu_oyna(monkeypatch, capsys, ["2", "3", "1"])
    assert "Kara deliğe düştün! Oyun bitti." in cikti


def test_ilk_menu_baglanti_sirasi(monkeypatch, capsys):
    cikti = oyunu_oyna(monkeypatch, capsys, ["2", "3", "1"])
    assert "Nereye gitmek istersin?\n[1] centauri\n[2] sirius" in cikti


def test_sirius_menusu_baglanti_sirasi(monkeypatch, capsys):
    cikti = oyunu_oyna(monkeypatch, capsys, ["2", "3", "1"])
    assert "[1] dünya\n[2] centauri\n[3] orion" in cikti


def test_gecersiz_secim_yakit_harcamaz(monkeypatch, capsys):
    cikti = oyunu_oyna(monkeypatch, capsys, ["x", "9", "0", "2", "3", "1"])
    assert cikti.count("Geçersiz seçim.") == 3
    assert "Yakıt: 100" in cikti
    assert "Yakıt: 70" in cikti  # üç yolculuktan sonra


def test_sirius_kredi_verir(monkeypatch, capsys):
    cikti = oyunu_oyna(monkeypatch, capsys, ["2", "3", "1"])
    assert "Sende: bol kredi" in cikti


def test_tum_esyalar_toplanir(monkeypatch, capsys):
    # dünya -> centauri (1) -> sirius (2) -> orion (3) -> kara_delik (1)
    cikti = oyunu_oyna(monkeypatch, capsys, ["1", "2", "3", "1"])
    assert "Sende: bol kredi, güçlü motorlar, yetenekli bir pilot" in cikti


def test_yakit_bitince_oyun_biter(monkeypatch, capsys):
    # dünya <-> centauri arasında gidip gelerek 10 yolculuk yap
    cikti = oyunu_oyna(monkeypatch, capsys, ["1"] * 10)
    assert "Yakıtın bitti! Oyun bitti." in cikti


def test_oyun_sonunda_toplam_hamle_yazilir(monkeypatch, capsys):
    cikti = oyunu_oyna(monkeypatch, capsys, ["2", "3", "1"])
    assert "Oyunu 3 hamlede bitirdin!" in cikti


def test_gecersiz_secimler_hamle_sayilmaz(monkeypatch, capsys):
    cikti = oyunu_oyna(monkeypatch, capsys, ["x", "9", "2", "3", "1"])
    assert "Oyunu 3 hamlede bitirdin!" in cikti


def test_yakit_bitince_de_hamle_yazilir(monkeypatch, capsys):
    cikti = oyunu_oyna(monkeypatch, capsys, ["1"] * 10)
    assert "Oyunu 10 hamlede bitirdin!" in cikti
