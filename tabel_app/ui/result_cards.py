"""Bagian hasil: tampilan f(x), empat kartu hasil, dan pesan status."""

import tkinter as tk

import sympy as sp

from .. import config as C
from ..formatting import fmt


class ResultCards(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=C.BG)
        self.columnconfigure(0, weight=1)

        self.lbl_fx = tk.Label(self, text="", bg=C.BG, fg=C.TEXT,
                               font=("Consolas", 12, "bold"), anchor="w")
        self.lbl_fx.grid(row=0, column=0, sticky="ew", pady=(0, 8))

        kartu = tk.Frame(self, bg=C.BG)
        kartu.grid(row=1, column=0, sticky="ew")
        for k in range(4):
            kartu.columnconfigure(k, weight=1, uniform="kartu")
        self.v_akar = self._kartu(kartu, 0, "AKAR (x)")
        self.v_fakar = self._kartu(kartu, 1, "f(AKAR)")
        self.v_step = self._kartu(kartu, 2, "STEP h")
        self.v_idx = self._kartu(kartu, 3, "TITIK KE-i")

        self.lbl_status = tk.Label(self, text="", bg=C.BG, fg=C.GREEN, font=C.FONT_B,
                                   anchor="w", justify="left", wraplength=900)
        self.lbl_status.grid(row=2, column=0, sticky="ew", pady=(8, 8))
        self.bind("<Configure>",
                  lambda e: self.lbl_status.config(wraplength=max(e.width - 10, 200)))

    @staticmethod
    def _kartu(parent, kolom, judul):
        warna = C.WARNA_KARTU[kolom]
        fr = tk.Frame(parent, bg=warna, padx=14, pady=10)
        fr.grid(row=0, column=kolom, sticky="nsew",
                padx=(0 if kolom == 0 else 6, 0 if kolom == 3 else 6))
        tk.Label(fr, text=judul, bg=warna, fg="white",
                 font=("Segoe UI", 8, "bold")).pack(anchor="w")
        v = tk.Label(fr, text="—", bg=warna, fg="white", font=("Consolas", 13, "bold"),
                     anchor="w", justify="left", wraplength=220)
        v.pack(anchor="w", pady=(4, 0))
        return v

    # ----- pembaruan tampilan -----
    def set_fungsi(self, expr):
        self.lbl_fx.config(text="f(x) = " + sp.sstr(expr))

    def tampilkan(self, hasil):
        """Isi kartu dan status dari objek HasilTabel."""
        self.v_step.config(text=fmt(hasil.h, 12))
        if not hasil.ada_solusi:
            for v in (self.v_akar, self.v_fakar, self.v_idx):
                v.config(text="—")
            self.lbl_status.config(
                fg=C.AMBER,
                text="⚠ Tidak ditemukan penyelesaian: tidak ada f(x_i) = 0 maupun "
                     "perubahan tanda. Coba perlebar batas, perbesar N, atau periksa fungsi.")
            return

        i = hasil.indeks_akar
        self.v_akar.config(text=fmt(hasil.akar, 12))
        self.v_fakar.config(text=fmt(hasil.f_akar, 12))
        self.v_idx.config(text=str(i))

        if hasil.f_akar == 0:
            msg = f"✔ Akar ditemukan: f(x_{i}) = 0, sehingga x_{i} adalah penyelesaian."
        else:
            msg = (f"✔ Akar ditemukan di titik ke-{i}: terjadi perubahan tanda dan "
                   f"titik ini paling dekat ke nol.")
        if len(hasil.solusi) > 1:
            lain = ", ".join(fmt(hasil.xs[k], 8) for k in hasil.solusi[1:])
            msg += (f"\nAda {len(hasil.solusi)} titik penyelesaian. "
                    f"Hasil di atas adalah yang pertama; lainnya: x = {lain}")
        self.lbl_status.config(text=msg, fg=C.GREEN)
