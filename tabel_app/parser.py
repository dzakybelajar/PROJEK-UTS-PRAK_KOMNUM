"""Parser fungsi f(x) berbasis SymPy -> fungsi numpy yang aman (vektor)."""

import numpy as np
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

X = sp.Symbol("x")
TRANSFORMS = standard_transformations + (implicit_multiplication_application, convert_xor)
LOCAL_DICT = {
    "x": X, "e": sp.E, "pi": sp.pi,
    "sin": sp.sin, "cos": sp.cos, "tan": sp.tan,
    "asin": sp.asin, "acos": sp.acos, "atan": sp.atan,
    "sinh": sp.sinh, "cosh": sp.cosh, "tanh": sp.tanh,
    "exp": sp.exp, "ln": sp.log, "log": sp.log, "log10": lambda v: sp.log(v, 10),
    "sqrt": sp.sqrt, "abs": sp.Abs, "Abs": sp.Abs,
}


def parse_fungsi(teks):
    """Ubah teks menjadi (ekspresi SymPy, fungsi numpy).

    Fungsi numpy menerima array x dan mengembalikan array f(x); nilai yang tidak
    terdefinisi (pembagian nol, log negatif, bilangan kompleks) menjadi NaN.
    Melempar ValueError bila teks tidak valid atau memuat variabel selain x.
    """
    try:
        expr = parse_expr(teks.replace("^", "**"), local_dict=LOCAL_DICT,
                          transformations=TRANSFORMS, evaluate=True)
        expr = sp.sympify(expr)
    except Exception as ex:
        raise ValueError(f"Fungsi tidak dapat dibaca: {ex}") from ex

    extra = expr.free_symbols - {X}
    if extra:
        raise ValueError("Variabel tidak dikenal: " + ", ".join(map(str, extra)) +
                         ". Gunakan hanya variabel x.")

    lam = sp.lambdify(X, expr, modules=["numpy"])

    def f(xs):
        arr = np.atleast_1d(np.asarray(xs, dtype=float))
        with np.errstate(all="ignore"):
            y = np.asarray(lam(arr))
        y = np.broadcast_to(y, arr.shape)
        if np.iscomplexobj(y):
            y = np.where(np.abs(y.imag) < 1e-12, y.real, np.nan)
        y = y.astype(float)
        y[~np.isfinite(y)] = np.nan
        return y

    return expr, f
