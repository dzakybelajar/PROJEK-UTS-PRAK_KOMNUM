"""Tab Tabel Perhitungan: Treeview dengan penyorotan baris."""

import tkinter as tk
from tkinter import ttk

from .. import config as C
from ..formatting import fmt


class TableView(tk.Frame):
    KOLOM = ("i", "x_i", "f_x", "tanda", "kali", "cek", "sol")
    JUDUL = {"i": ("i", 55, "center"), "x_i": ("x_i", 160, "e"),
             "f_x": ("f(x_i)", 170, "e"), "tanda": ("Tanda", 60, "center"),
             "kali": ("f(x_i)·f(x_i+1)", 170, "e"),
             "cek": ("Pengecekan", 430, "w"), "sol": ("Solusi", 70, "center")}

    def __init__(self, master):
        super().__init__(master, bg=C.BG)
        self.lbl_h = tk.Label(self, text="", bg=C.BG, fg=C.MUTED, font=C.FONT,
                              anchor="w", justify="left")
        self.lbl_h.pack(fill="x", padx=6, pady=(8, 6))

        wrap = tk.Frame(self, bg=C.BG)
        wrap.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(wrap, columns=self.KOLOM, show="headings",
                                 selectmode="browse")
        for k in self.KOLOM:
            teks, lebar, rata = self.JUDUL[k]
            self.tree.heading(k, text=teks)
            self.tree.column(k, width=lebar, anchor=rata, stretch=(k == "cek"))

        sb_y = ttk.Scrollbar(wrap, orient="vertical", command=self.tree.yview)
        sb_x = ttk.Scrollbar(wrap, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=sb_y.set, xscrollcommand=sb_x.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        sb_y.grid(row=0, column=1, sticky="ns")
        sb_x.grid(row=1, column=0, sticky="ew")
        wrap.rowconfigure(0, weight=1)
        wrap.columnconfigure(0, weight=1)

        self.tree.tag_configure("solusi", background="#065f46", foreground="white")
        self.tree.tag_configure("ubah", background="#78350f", foreground="white")

    def isi(self, hasil, a, b, N):
        """Tampilkan seluruh baris tabel dari objek HasilTabel."""
        self.lbl_h.config(
            text=f"Step  h = (x atas − x bawah) / N = ({fmt(b, 10)} − {fmt(a, 10)}) / {N} "
                 f"= {fmt(hasil.h, 12)}     |     baris hijau = penyelesaian, "
                 f"baris cokelat = tanda berubah")
        self.tree.delete(*self.tree.get_children())
        solusi = set(hasil.solusi)
        pertama = None
        for br in hasil.baris:
            tag = "solusi" if br.i in solusi else ("ubah" if br.jenis == "ubah" else "")
            iid = self.tree.insert(
                "", "end", tags=(tag,) if tag else (),
                values=(br.i, fmt(br.x, 12), fmt(br.fx, 12), br.tanda,
                        fmt(br.kali, 12), br.keterangan,
                        "✔" if br.i in solusi else ""))
            if pertama is None and br.i in solusi:
                pertama = iid
        if pertama:
            self.tree.see(pertama)
