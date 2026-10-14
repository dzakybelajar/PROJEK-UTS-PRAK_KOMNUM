"""Jendela utama: merakit semua komponen UI dan menghubungkannya ke solver."""

import tkinter as tk
from tkinter import ttk, messagebox

from .. import config as C
from ..parser import parse_fungsi
from ..solver import metode_tabel
from .algo_tab import AlgoTab
from .header import Header
from .input_panel import InputPanel
from .plot_view import PlotView
from .result_cards import ResultCards
from .styles import terapkan_gaya
from .table_view import TableView


def _aktifkan_dpi_windows():
    """Agar tampilan tajam di layar High-DPI (hanya berpengaruh di Windows)."""
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulator Metode Tabel — Komputasi Numerik")
        self.geometry("1320x820")
        self.minsize(1100, 700)
        self.configure(bg=C.BG)
        terapkan_gaya(self)
        self._susun()
        self.bind("<Return>", lambda _e: self.hitung())
        self.hitung()

    def _susun(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        Header(self).grid(row=0, column=0, columnspan=2, sticky="ew")

        self.input_panel = InputPanel(self, on_hitung=self.hitung)
        self.input_panel.grid(row=1, column=0, sticky="ns", padx=(14, 8), pady=(10, 14))

        kanan = tk.Frame(self, bg=C.BG)
        kanan.grid(row=1, column=1, sticky="nsew", padx=(0, 14), pady=(10, 14))
        kanan.columnconfigure(0, weight=1)
        kanan.rowconfigure(1, weight=1)

        self.hasil_ui = ResultCards(kanan)
        self.hasil_ui.grid(row=0, column=0, sticky="ew")

        nb = ttk.Notebook(kanan)
        nb.grid(row=1, column=0, sticky="nsew")
        self.plot_view = PlotView(nb)
        self.table_view = TableView(nb)
        nb.add(self.plot_view, text="📈  Grafik")
        nb.add(self.table_view, text="🧾  Tabel Perhitungan")
        nb.add(AlgoTab(nb), text="📖  Algoritma")

    def hitung(self):
        try:
            teks, a, b, N = self.input_panel.ambil_input()
            expr, f = parse_fungsi(teks)
            hasil = metode_tabel(f, a, b, N)
        except Exception as ex:
            messagebox.showerror("Input tidak valid", str(ex))
            return

        self.hasil_ui.set_fungsi(expr)
        self.hasil_ui.tampilkan(hasil)
        self.table_view.isi(hasil, a, b, N)
        self.plot_view.gambar(expr, f, a, b, N, hasil)


def jalankan():
    """Titik masuk aplikasi GUI."""
    _aktifkan_dpi_windows()
    App().mainloop()
