# python
Yazılım geliştirme python dersleri

## İleri Python Programlama – Hafta 3 Lab Ödevi (Fonksiyonlar Derinlemesine)

- **Öğrenci:** Tayfur Tatar
- **Numara:** 20253006029
- **Bölüm:** Yazılım Geliştirme
- **GitHub deposu:** https://github.com/Tayfue/python
- **Ders:** İleri Python Programlama · İstanbul Nişantaşı Üniversitesi · Dr. Öğr. Üyesi Murat Emeç · 2026–2027 Güz

### Görevler ve dosyalar

| Görev | İçerik | Dosyalar |
|-------|--------|----------|
| 1 | Saf fonksiyonlar: `envanter_metni`, `hedef_menusu` | `uzay_oyunu/oyun.py`, `tests/test_fonksiyonlar.py` |
| 2 | Esnek parametreler: `gorev_kaydi(baslik, *adimlar, oncelik, **ekler)` | `uzay_oyunu/kayit.py`, `tests/test_kayit.py` |
| 3 | Galaksi verisi: `galaksi.json`, `galaksi_kur`, `galaksi_yukle` | `uzay_oyunu/galaksi.json`, `uzay_oyunu/oyun.py`, `tests/test_galaksi.py` |
| 4 | Tuzaklar ve kapsam: `yakit_ekle`, `kapsam.md` | `tests/test_tuzaklar.py`, `kapsam.md` |
| 5 | Closure ve lambda: `hamle_sayaci`, `en_bagli_gezegenler` | `uzay_oyunu/araclar.py`, `tests/test_araclar.py`, `tests/test_travel.py` |
| Bonus | `sure_olc(fonksiyon)` sarmalayıcısı | `uzay_oyunu/araclar.py`, `tests/test_sure_olc.py` |

`tests/test_travel.py` Hafta 2'den kalan davranış testleridir; refaktör boyunca
hepsi geçmeye devam eder. `tests/test_kurallar.py` ödev kurallarını denetler
(`global` yok, fonksiyonlarda tip ipucu ve docstring var).

### Çalıştırma

```bash
uv run pytest                       # tüm testler
uv run python -m uzay_oyunu.oyun    # oyunu oyna
uv run python -m uzay_oyunu.kayit   # gorev_kaydi örnekleri
uv run python -m uzay_oyunu.araclar # bonus: sure_olc ile en_bagli_gezegenler
```

Python 3.11 veya üstü gerekir; dış paket yoktur (yalnızca test için `pytest`).

### Klasör yapısı

```
uzay_oyunu/   oyun.py  kayit.py  araclar.py  galaksi.json
tests/        test_fonksiyonlar  test_kayit  test_galaksi  test_tuzaklar
              test_araclar  test_sure_olc  test_travel  test_kurallar
kapsam.md     Görev 4(b): kapsam örnekleri
```

Her görev için testler önce yazıldı (kırmızı commit), ardından kod yazıldı
(yeşil commit); geçmiş `git log` ile görülebilir.
