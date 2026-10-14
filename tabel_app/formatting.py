"""Fungsi bantu format angka dan penanda tanda."""

import numpy as np


def fmt(v, presisi=10):
    """Tampilkan angka sebagai desimal biasa (tanpa notasi ilmiah / simbol e).

    Nol di belakang koma dibuang. NaN / None ditampilkan sebagai '—'.
    """
    if v is None:
        return "—"
    v = float(v)
    if np.isnan(v):
        return "—"
    s = np.format_float_positional(v, precision=presisi, unique=False, trim="-")
    return "0" if s in ("-0", "") else s


def tanda(v):
    """Kembalikan penanda tanda nilai: '+', '−', '0', atau 'n/a' bila tak terdefinisi."""
    if np.isnan(v):
        return "n/a"
    return "0" if v == 0 else ("+" if v > 0 else "−")
