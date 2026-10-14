"""Header aplikasi dengan latar gradien."""

import tkinter as tk

from .. import config as C
from .styles import lerp_warna


class Header(tk.Canvas):
    TINGGI = 92

    def __init__(self, master):
        super().__init__(master, height=self.TINGGI, bg=C.BG, highlightthickness=0)
        self.bind("<Configure>", self._gambar)

    def _gambar(self, _event=None):
        self.delete("all")
        w = max(self.winfo_width(), 2)
        for x in range(0, w, 3):
            t = x / w
            if t < .5:
                warna = lerp_warna("#4f46e5", "#7c3aed", t * 2)
            else:
                warna = lerp_warna("#7c3aed", "#ec4899", (t - .5) * 2)
            self.create_rectangle(x, 0, x + 3, self.TINGGI, fill=warna, outline=warna)

        self.create_text(28, 34, anchor="w", text="📐  Kalkulator Metode Tabel",
                         fill="white", font=("Segoe UI", 22, "bold"))
        self.create_text(30, 66, anchor="w", fill="#f1f5f9", font=("Segoe UI", 10),
                         text="Cari akar persamaan non-linear f(x) = 0 lewat tabulasi "
                              "dan deteksi perubahan tanda")
        # tanda air "f(x) = 0" di sisi kanan (lebih terang dari latar gradien)
        self.create_text(w - 24, 52, anchor="e", text="f(x) = 0",
                         fill=lerp_warna("#ec4899", "#ffffff", .18),
                         font=("Consolas", 40, "bold"))
