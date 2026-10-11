# Ad Soyad: Tayfur Tatar
# Öğrenci No: 20253006029

"""Ödev kurallarının otomatik denetimi: global yok, tip ipucu ve docstring var."""

import ast
from pathlib import Path

import pytest

PAKET = Path(__file__).resolve().parent.parent / "uzay_oyunu"
DOSYALAR = sorted(PAKET.glob("*.py"))


def agac(dosya: Path) -> ast.Module:
    return ast.parse(dosya.read_text(encoding="utf-8"))


@pytest.mark.parametrize("dosya", DOSYALAR, ids=lambda d: d.name)
def test_global_anahtar_kelimesi_kullanilmamis(dosya):
    assert not [d for d in ast.walk(agac(dosya)) if isinstance(d, ast.Global)]


@pytest.mark.parametrize("dosya", DOSYALAR, ids=lambda d: d.name)
def test_ust_duzey_fonksiyonlarda_docstring_ve_tip_ipucu_var(dosya):
    for dugum in agac(dosya).body:
        if not isinstance(dugum, ast.FunctionDef):
            continue
        assert ast.get_docstring(dugum), f"{dugum.name}: docstring yok"
        assert dugum.returns is not None, f"{dugum.name}: dönüş tipi yok"
        tum_argumanlar = (
            dugum.args.posonlyargs
            + dugum.args.args
            + dugum.args.kwonlyargs
            + [a for a in (dugum.args.vararg, dugum.args.kwarg) if a]
        )
        for arguman in tum_argumanlar:
            assert arguman.annotation is not None, f"{dugum.name}({arguman.arg}): tip yok"
