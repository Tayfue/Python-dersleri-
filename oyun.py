# Ad Soyad: Tayfur Tatar
# Öğrenci No: 20253006029

"""Uzay oyunu."""

import json
from pathlib import Path
from typing import Any

from uzay_oyunu.araclar import hamle_sayaci

GALAKSI_DOSYASI = Path(__file__).with_name("galaksi.json")


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Oyuncunun sahip olduğu eşyaları anlatan metni döndürür.

    Hiç eşya yoksa boş metin döndürür. Fonksiyon ekrana yazmaz.

    >>> envanter_metni(True, False, True)
    'Sende: bol kredi, yetenekli bir pilot'
    >>> envanter_metni(False, False, False)
    ''
    """
    parcalar = []
    if credits:
        parcalar.append("bol kredi")
    if engines:
        parcalar.append("güçlü motorlar")
    if copilot:
        parcalar.append("yetenekli bir pilot")
    if not parcalar:
        return ""
    return "Sende: " + ", ".join(parcalar)


def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek hedefleri numaralı menü metni olarak döndürür.

    Fonksiyon ekrana yazmaz ve verilen listeyi değiştirmez.

    >>> print(hedef_menusu(["centauri", "sirius"]))
    Nereye gitmek istersin?
    [1] centauri
    [2] sirius
    """
    satirlar = ["Nereye gitmek istersin?"]
    for sira, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{sira}] {hedef}")
    return "\n".join(satirlar)


def yakit_ekle(miktar: int, depo: list[int] | None = None) -> list[int]:
    """Depoya yakıt miktarı ekler ve depoyu döndürür.

    Depo verilmezse her çağrıda yeni bir liste açılır. Varsayılan argüman
    olarak [] yazmak, listenin tüm çağrılar arasında paylaşılmasına yol açardı.

    >>> yakit_ekle(10)
    [10]
    >>> yakit_ekle(20)
    [20]
    """
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def galaksi_yukle(yol: Path | str = GALAKSI_DOSYASI) -> dict[str, Any]:
    """Galaksi verisini JSON dosyasından okuyup sözlük olarak döndürür."""
    with open(yol, encoding="utf-8") as dosya:
        return json.load(dosya)


def galaksi_kur(
    gezegenler: list[str],
    baglantilar: dict[str, list[str]],
    baslangic: str,
    **kwargs: int,
) -> dict[str, Any]:
    """Galaksi verisinden oyunun başlangıç durumunu kurar.

    Args:
        gezegenler: Haritadaki gezegenlerin listesi.
        baglantilar: Her gezegenden gidilebilecek yerler (sıra korunur).
        baslangic: Oyuncunun başladığı gezegen; gezegenler içinde olmalı.
        **kwargs: Yalnızca "yakit" kullanılır (verilmezse 50); diğerleri yok sayılır.

    Raises:
        ValueError: Başlangıç gezegeni gezegenler listesinde yoksa.

    >>> g = galaksi_kur(["mars"], {"mars": []}, "mars")
    >>> g["konum"], g["yakit"]
    ('mars', 50)
    """
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni listede yok: {baslangic}")
    return {
        "gezegenler": list(gezegenler),
        "baglantilar": {gezegen: list(hedef) for gezegen, hedef in baglantilar.items()},
        "konum": baslangic,
        "yakit": kwargs.get("yakit", 50),
    }


def travel(galaksi: dict[str, Any] | None = None) -> None:
    """Oyunu başlatır: oyuncu gezegenler arasında yolculuk eder.

    Args:
        galaksi: galaksi_kur() çıktısı. Verilmezse galaksi.json dosyasından kurulur.
    """
    if galaksi is None:
        galaksi = galaksi_kur(**galaksi_yukle())
    location = galaksi["konum"]
    fuel = galaksi["yakit"]
    sayac = hamle_sayaci()
    hamle = 0
    credits = False
    engines = False
    copilot = False

    while True:
        print("Konum: " + location + " | Yakıt: " + str(fuel))

        # Envanter: sahip olunan eşyaları yaz
        envanter = envanter_metni(credits, engines, copilot)
        if envanter:
            print(envanter)

        # Bulunulan gezegenden gidilebilecek yerler galaksi verisinden gelir
        destinations = galaksi["baglantilar"][location]

        if not destinations:
            print("Kara deliğe düştün! Oyun bitti.")
            break

        # Hedef menüsü
        print(hedef_menusu(destinations))

        choice = input("> ")
        try:
            index = int(choice) - 1
        except ValueError:
            index = -1
        if index < 0 or index >= len(destinations):
            print("Geçersiz seçim.")
            continue

        location = destinations[index]
        fuel = fuel - 10
        hamle = sayac()

        # Gezegene varınca eşya kazan
        if location == "sirius":
            credits = True
        elif location == "centauri":
            copilot = True
        elif location == "orion":
            engines = True

        if location != "kara_delik" and fuel <= 0:
            print("Yakıtın bitti! Oyun bitti.")
            break

    print(f"Oyunu {hamle} hamlede bitirdin!")


if __name__ == "__main__":
    travel()
