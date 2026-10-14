"""Panel input (kiri): fungsi f(x), batas, N, serta tombol aksi."""

import tkinter as tk
from tkinter import ttk

from .. import config as C


class InputPanel(tk.Frame):
    def __init__(self, master, on_hitung):
        super().__init__(master, bg=C.PANEL, padx=18, pady=16)
        self.on_hitung = on_hitung
        self._bangun()

    # ----- tata letak -----
    def _bangun(self):
        tk.Label(self, text="⚙  PANEL INPUT", bg=C.PANEL, fg=C.TEXT,
                 font=C.FONT_H).pack(anchor="w")
        tk.Frame(self, bg=C.ACCENT, height=3).pack(fill="x", pady=(6, 12))

        tk.Label(self, text="Contoh fungsi", bg=C.PANEL, fg=C.MUTED,
                 font=C.FONT).pack(anchor="w")
        self.cb_preset = ttk.Combobox(self, values=list(C.PRESET.keys()),
                                      state="readonly", width=30)
        self.cb_preset.current(0)
        self.cb_preset.pack(fill="x", pady=(2, 10))
        self.cb_preset.bind("<<ComboboxSelected>>", self._pilih_preset)

        fx, a, b, n = C.DEFAULT_INPUT
        self.e_fx = self._input(self, "Fungsi f(x)", fx)

        baris = tk.Frame(self, bg=C.PANEL)
        baris.pack(fill="x")
        kiri = tk.Frame(baris, bg=C.PANEL)
        kiri.pack(side="left", fill="x", expand=True, padx=(0, 6))
        kanan = tk.Frame(baris, bg=C.PANEL)
        kanan.pack(side="left", fill="x", expand=True, padx=(6, 0))
        self.e_a = self._input(kiri, "Batas bawah (x bawah)", a)
        self.e_b = self._input(kanan, "Batas atas (x atas)", b)
        self.e_n = self._input(self, "Jumlah pembagian (N)", n)

        tk.Button(self, text="🚀  HITUNG AKAR", command=self.on_hitung, bg=C.ACCENT,
                  fg="white", activebackground=C.PINK, activeforeground="white",
                  font=C.FONT_H, relief="flat", cursor="hand2",
                  pady=10).pack(fill="x", pady=(14, 6))
        tk.Button(self, text="↺  Reset", command=self.reset, bg=C.PANEL, fg=C.MUTED,
                  activebackground=C.BORDER, activeforeground=C.TEXT, font=C.FONT,
                  relief="flat", cursor="hand2", pady=6, highlightthickness=1,
                  highlightbackground=C.BORDER).pack(fill="x")

        tk.Label(self, text="Mendukung: + − * / ^   sin cos tan exp\n"
                            "ln log sqrt abs   pi  e\n"
                            "Perkalian implisit: 2x, 3sin(x)",
                 bg=C.PANEL, fg=C.MUTED, font=C.FONT_KECIL,
                 justify="left").pack(anchor="w", pady=(14, 0))

    @staticmethod
    def _input(parent, label, nilai):
        tk.Label(parent, text=label, bg=C.PANEL, fg=C.MUTED, font=C.FONT).pack(anchor="w")
        e = tk.Entry(parent, bg=C.ENTRY_BG, fg=C.TEXT, insertbackground="white",
                     relief="flat", font=("Consolas", 11), highlightthickness=1,
                     highlightbackground=C.BORDER, highlightcolor=C.ACCENT, width=14)
        e.insert(0, nilai)
        e.pack(fill="x", pady=(2, 10), ipady=5)
        return e

    # ----- aksi -----
    def _isi(self, entry, nilai):
        entry.delete(0, "end")
        entry.insert(0, nilai)

    def _pilih_preset(self, _event=None):
        p = C.PRESET[self.cb_preset.get()]
        if p:
            for e, v in zip((self.e_fx, self.e_a, self.e_b), p):
                self._isi(e, v)
            self.on_hitung()

    def reset(self):
        self.cb_preset.current(0)
        for e, v in zip((self.e_fx, self.e_a, self.e_b, self.e_n), C.DEFAULT_INPUT):
            self._isi(e, v)
        self.on_hitung()

    @staticmethod
    def _angka(entry, nama):
        try:
            return float(entry.get().strip().replace(",", "."))
        except ValueError:
            raise ValueError(f"Nilai '{nama}' harus berupa angka.") from None

    def ambil_input(self):
        """Baca dan validasi input. Mengembalikan (teks_fungsi, a, b, N).

        Melempar ValueError dengan pesan yang ramah pengguna bila tidak valid.
        """
        teks = self.e_fx.get().strip()
        if not teks:
            raise ValueError("Fungsi f(x) belum diisi.")
        a = self._angka(self.e_a, "batas bawah")
        b = self._angka(self.e_b, "batas atas")
        n = self._angka(self.e_n, "N")
        if a >= b:
            raise ValueError("Batas bawah harus lebih kecil daripada batas atas.")
        if n < 1 or int(n) != n:
            raise ValueError("N harus bilangan bulat ≥ 1.")
        if n > C.N_MAKS:
            raise ValueError(f"N maksimum {C.N_MAKS:,} agar tabel tetap lancar.".replace(",", "."))
        return teks, a, b, int(n)
