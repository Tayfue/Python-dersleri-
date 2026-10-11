# Ad Soyad: Tayfur Tatar
# Öğrenci No: 20253006029

"""Görev kaydı: esnek parametreli (*args, **kwargs) fonksiyon örneği."""


def _buyuk_harf(metin: str) -> str:
    """Metni Türkçe kurallarına uygun büyük harfe çevirir (i -> İ)."""
    return metin.replace("i", "İ").upper()


def gorev_kaydi(
    baslik: str,
    *adimlar: str,
    oncelik: str = "normal",
    **ekler: str,
) -> str:
    """Bir görevi başlık, numaralı adımlar ve ek bilgilerle metne döker.

    Args:
        baslik: Görevin başlığı.
        *adimlar: Görevin adımları; istenildiği kadar verilebilir.
        oncelik: Öncelik. Yalnızca adıyla (oncelik="yüksek") verilebilir.
        **ekler: "anahtar: değer" satırı olarak yazılan ek bilgiler.

    Returns:
        Çok satırlı kayıt metni. Fonksiyon ekrana yazmaz.

    >>> print(gorev_kaydi("Yakıt al", "Depoya git", oncelik="yüksek", sorumlu="Ayşe"))
    [YÜKSEK] Yakıt al
      1. Depoya git
      sorumlu: Ayşe
    """
    satirlar = [f"[{_buyuk_harf(oncelik)}] {baslik}"]
    for sira, adim in enumerate(adimlar, start=1):
        satirlar.append(f"  {sira}. {adim}")
    for anahtar, deger in ekler.items():
        satirlar.append(f"  {anahtar}: {deger}")
    return "\n".join(satirlar)


if __name__ == "__main__":
    # 1) Doğrudan çağrı: adımlar ve ekler tek tek yazılır.
    print(
        gorev_kaydi(
            "Kara deliğe atla",
            "Kredi kazan",
            "Pilot bul",
            "Hiperdrive al",
            oncelik="yüksek",
            sorumlu="Ayşe",
        )
    )

    print()

    # 2) Açarak çağrı: liste * ile adımlara, sözlük ** ile adlı argümanlara açılır.
    adim_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ayarlar = {"oncelik": "yüksek", "sorumlu": "Ayşe"}
    print(gorev_kaydi("Kara deliğe atla", *adim_listesi, **ayarlar))
