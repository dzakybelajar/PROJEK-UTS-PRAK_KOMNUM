"""Tab Grafik: plot f(x), titik tabel, dan titik akar (matplotlib di Tkinter)."""

import tkinter as tk

import numpy as np
import sympy as sp
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from .. import config as C
from ..formatting import fmt


class PlotView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=C.BG)
        self.fig = Figure(figsize=(9, 5), dpi=100, facecolor=C.BG)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)

        toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        try:
            toolbar.config(background=C.PANEL)
            for w in toolbar.winfo_children():
                w.config(background=C.PANEL)
        except Exception:
            pass
        toolbar.pack(side="bottom", fill="x")
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def gambar(self, expr, f, a, b, N, hasil):
        ax = self.ax
        ax.clear()
        ax.set_facecolor(C.BG)

        # kurva halus f(x); sembunyikan garis penyambung di titik diskontinu
        xg = np.linspace(a, b, 3000)
        yg = f(xg)
        dy = np.abs(np.diff(yg))
        skala = np.nanpercentile(np.abs(yg), 90) if np.isfinite(yg).any() else 1
        yp = yg.copy()
        loncat = np.where(dy > 20 * max(skala, 1))[0]
        yp[loncat] = np.nan
        yp[loncat + 1] = np.nan

        ax.axhline(0, color=C.MUTED, lw=1)
        ax.fill_between(xg, 0, yp, where=~np.isnan(yp), color=C.ACCENT, alpha=.12)
        ax.plot(xg, yp, color="#a78bfa", lw=2.4, label="f(x) = " + sp.sstr(expr))

        if N <= 300:
            ax.scatter(hasil.xs, hasil.ys, s=18, color="#38bdf8", zorder=3,
                       label=f"Titik tabel (N = {N})")

        if hasil.ada_solusi:
            lain = hasil.solusi[1:]
            if lain:
                ax.scatter(hasil.xs[lain], hasil.ys[lain], s=60, marker="D",
                           facecolor="none", edgecolor="#facc15", zorder=4,
                           label="Penyelesaian lain")
            ax.scatter([hasil.akar], [hasil.f_akar], s=230, marker="*", color=C.RED,
                       edgecolor="white", zorder=5, label=f"Akar: x = {fmt(hasil.akar, 8)}")
            ax.axvline(hasil.akar, color=C.RED, ls="--", lw=1, alpha=.7)
            ax.annotate(f"x = {fmt(hasil.akar, 8)}", (hasil.akar, hasil.f_akar),
                        textcoords="offset points", xytext=(0, 18), ha="center",
                        color="#fda4af", fontsize=10, fontweight="bold")

        if np.isfinite(yp).any():
            lo, hi = np.nanpercentile(yp, [1, 99])
            pad = (hi - lo) * 0.12 or 1
            ax.set_ylim(min(lo, 0) - pad, max(hi, 0) + pad)
        try:
            ax.ticklabel_format(style="plain", useOffset=False)
        except Exception:
            pass

        ax.set_title("Grafik f(x) dan Titik Akar (Metode Tabel)", color=C.TEXT,
                     fontsize=13, fontweight="bold", pad=12)
        ax.set_xlabel("x", color=C.TEXT)
        ax.set_ylabel("f(x)", color=C.TEXT)
        ax.tick_params(colors=C.MUTED)
        for sisi in ax.spines.values():
            sisi.set_color(C.BORDER)
        ax.grid(alpha=.18, color=C.MUTED)
        leg = ax.legend(loc="best", fontsize=9, facecolor=C.PANEL, edgecolor=C.BORDER)
        for t in leg.get_texts():
            t.set_color(C.TEXT)
        self.fig.tight_layout()
        self.canvas.draw_idle()
