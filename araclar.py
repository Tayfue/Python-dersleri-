# Ad Soyad: Tayfur Tatar
# Öğrenci No: 20253006029

"""Oyun yardımcıları: closure ile sayaç ve lambda ile sıralama."""

from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def hamle_sayaci() -> Callable[[], int]:
    """Her çağrıldığında bir artan bağımsız bir sayaç fonksiyonu döndürür.

    Sayaç değeri dıştaki fonksiyonun değişkeninde tutulur (closure) ve
    ``nonlocal`` ile güncellenir.

    >>> sayac = hamle_sayaci()
    >>> sayac(), sayac(), sayac()
    (1, 2, 3)
    """
    hamle = 0

    def say() -> int:
        nonlocal hamle
        hamle += 1
        return hamle

    return say


def en_bagli_gezegenler(galaksi: dict[str, Any]) -> list[str]:
    """Gezegenleri bağlantı sayısına göre çoktan aza sıralar.

    Bağlantı sayısı eşitse gezegenler alfabetik sıradadır. Galaksi değişmez.

    >>> g = {"gezegenler": ["a", "b"], "baglantilar": {"a": [], "b": ["a"]}}
    >>> en_bagli_gezegenler(g)
    ['b', 'a']
    """
    return sorted(
        galaksi["gezegenler"],
        key=lambda gezegen: (-len(galaksi["baglantilar"][gezegen]), gezegen),
    )


def sure_olc(fonksiyon: Callable[P, R]) -> Callable[P, R]:
    """Verilen fonksiyonu çalışma süresini yazan bir sarmalayıcıya dönüştürür.

    Sarmalayıcı, aldığı tüm argümanları (*args, **kwargs) olduğu gibi asıl
    fonksiyona iletir, sonucu aynen döndürür ve süreyi saniye olarak yazar.

    >>> topla = sure_olc(lambda a, b: a + b)
    >>> topla(2, 3)  # doctest: +ELLIPSIS
    <lambda> ... sn sürdü
    5
    """

    @wraps(fonksiyon)
    def sarmalayici(*args: P.args, **kwargs: P.kwargs) -> R:
        baslangic = perf_counter()
        try:
            return fonksiyon(*args, **kwargs)
        finally:
            sure = perf_counter() - baslangic
            print(f"{fonksiyon.__name__} {sure:.6f} sn sürdü")

    return sarmalayici


if __name__ == "__main__":
    # Bonus gösterimi: en_bagli_gezegenler, sure_olc ile sarılıp denenir.
    # (oyun modülü burada içe aktarılır; böylece modüller arası döngü oluşmaz.)
    from uzay_oyunu.oyun import galaksi_kur, galaksi_yukle

    galaksi = galaksi_kur(**galaksi_yukle())
    en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)
    print(en_bagli_gezegenler(galaksi))
