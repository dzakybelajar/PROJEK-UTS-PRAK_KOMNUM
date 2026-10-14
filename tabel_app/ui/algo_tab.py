"""Tab Algoritma: penjelasan singkat Metode Tabel."""

import tkinter as tk

from .. import config as C

TEKS = (
    "ALGORITMA METODE TABEL\n\n"
    "1. Definisikan fungsi f(x).\n"
    "2. Tentukan batas bawah x_bawah dan batas atas x_atas.\n"
    "3. Tentukan jumlah pembagian N.\n"
    "4. Hitung step h = (x_atas − x_bawah) / N.\n"
    "5. Untuk i = 0 s/d N hitung:  x_i = x_bawah + i·h   dan   y_i = f(x_i).\n"
    "6. Untuk i = 0 s/d N periksa:\n"
    "     • Bila f(x_i) = 0  →  x_i adalah penyelesaian.\n"
    "     • Bila f(x_i)·f(x_i+1) < 0  →\n"
    "           bila |f(x_i)| < |f(x_i+1)|  maka x_i adalah penyelesaian,\n"
    "           bila tidak maka x_i+1 adalah penyelesaian.\n\n"
    "KETERANGAN\n"
    "Penyelesaian dipilih dari dua titik di sekitar perubahan tanda, yaitu titik yang\n"
    "nilai |f(x)|-nya lebih dekat ke nol. Perbesar N agar tabel lebih rapat dan hasil\n"
    "lebih akurat.\n\n"
    "CATATAN\n"
    "• Akar kembar (mis. x²) tidak menyebabkan perubahan tanda sehingga tidak terdeteksi.\n"
    "• Titik diskontinu seperti 1/x atau tan(x) dapat memberi perubahan tanda palsu.\n"
)


class AlgoTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=C.BG)
        tk.Label(self, text=TEKS, bg=C.BG, fg=C.TEXT, font=("Consolas", 11),
                 justify="left", anchor="nw").pack(fill="both", expand=True,
                                                   padx=18, pady=16)
