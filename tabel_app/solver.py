"""Inti algoritma Metode Tabel (tanpa ketergantungan GUI).

Langkah:
  1. Hitung h = (x_atas - x_bawah) / N.
  2. Untuk i = 0..N hitung x_i = x_bawah + i.h dan y_i = f(x_i).
  3. Untuk i = 0..N periksa:
       - f(x_i) = 0                -> x_i adalah penyelesaian.
       - f(x_i).f(x_i+1) < 0       -> bila |f(x_i)| < |f(x_i+1)| maka x_i
                                      penyelesaian, bila tidak maka x_i+1.
"""

from dataclasses import dataclass, field
from typing import List, Optional

import numpy as np

from .formatting import tanda


@dataclass
class BarisTabel:
    """Satu baris pada tabel perhitungan."""
    i: int
    x: float
    fx: float
    tanda: str
    kali: float          # f(x_i) * f(x_i+1), NaN bila tidak dihitung
    keterangan: str
    jenis: str           # "normal" atau "ubah" (tanda berubah)


@dataclass
class HasilTabel:
    """Hasil lengkap perhitungan Metode Tabel."""
    h: float
    xs: np.ndarray
    ys: np.ndarray
    baris: List[BarisTabel] = field(default_factory=list)
    solusi: List[int] = field(default_factory=list)   # indeks titik penyelesaian

    @property
    def ada_solusi(self) -> bool:
        return len(self.solusi) > 0

    @property
    def indeks_akar(self) -> Optional[int]:
        """Indeks penyelesaian pertama yang ditemukan (None bila tidak ada)."""
        return self.solusi[0] if self.solusi else None

    @property
    def akar(self) -> Optional[float]:
        return None if self.indeks_akar is None else float(self.xs[self.indeks_akar])

    @property
    def f_akar(self) -> Optional[float]:
        return None if self.indeks_akar is None else float(self.ys[self.indeks_akar])


def metode_tabel(f, xbawah, xatas, N) -> HasilTabel:
    """Jalankan Metode Tabel pada f(x) di interval [xbawah, xatas] dengan N pembagian."""
    if N < 1 or int(N) != N:
        raise ValueError("N harus bilangan bulat >= 1.")
    if xbawah >= xatas:
        raise ValueError("Batas bawah harus lebih kecil daripada batas atas.")
    N = int(N)

    h = (xatas - xbawah) / N                         # step pembagi
    xs = xbawah + np.arange(N + 1) * h               # x_i = x_bawah + i.h
    ys = np.asarray(f(xs), dtype=float)              # y_i = f(x_i)

    baris, solusi = [], []
    for i in range(N + 1):
        kali, jenis = np.nan, "normal"
        ket = "Tanda sama → bukan penyelesaian"
        if np.isnan(ys[i]):
            ket = "f(x_i) tidak terdefinisi"
        elif ys[i] == 0:
            ket = "f(x_i) = 0 → x_i penyelesaian"
            solusi.append(i)
        elif i == N:
            ket = "Titik terakhir (tidak ada x_i+1)"
        elif np.isnan(ys[i + 1]):
            ket = "f(x_i+1) tidak terdefinisi"
        else:
            kali = ys[i] * ys[i + 1]
            if kali < 0:
                jenis = "ubah"
                if abs(ys[i]) < abs(ys[i + 1]):
                    ket = "Tanda berubah, |f(x_i)| < |f(x_i+1)| → x_i penyelesaian"
                    solusi.append(i)
                else:
                    ket = "Tanda berubah, |f(x_i)| ≥ |f(x_i+1)| → x_i+1 penyelesaian"
                    solusi.append(i + 1)
        baris.append(BarisTabel(i, float(xs[i]), float(ys[i]), tanda(ys[i]),
                                float(kali), ket, jenis))

    return HasilTabel(h=h, xs=xs, ys=ys, baris=baris, solusi=sorted(set(solusi)))
