"""Gaya (tema gelap) untuk widget ttk dan utilitas warna."""

from tkinter import ttk

from .. import config as C


def lerp_warna(c1, c2, t):
    """Interpolasi linear dua warna hex (#rrggbb) dengan t di [0, 1]."""
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(int(a[k] + (b[k] - a[k]) * t) for k in range(3))


def terapkan_gaya(root):
    """Terapkan tema gelap ke Notebook, Treeview, Combobox, dan Scrollbar."""
    s = ttk.Style(root)
    s.theme_use("clam")

    s.configure("TNotebook", background=C.BG, borderwidth=0)
    s.configure("TNotebook.Tab", background=C.PANEL, foreground=C.MUTED,
                padding=(18, 8), font=C.FONT_B, borderwidth=0)
    s.map("TNotebook.Tab", background=[("selected", C.ACCENT)],
          foreground=[("selected", "white")])

    s.configure("Treeview", background=C.PANEL2, fieldbackground=C.PANEL2,
                foreground=C.TEXT, rowheight=26, borderwidth=0, font=C.MONO)
    s.configure("Treeview.Heading", background=C.PANEL, foreground=C.TEXT,
                font=C.FONT_B, relief="flat", padding=6)
    s.map("Treeview", background=[("selected", C.ACCENT)],
          foreground=[("selected", "white")])
    s.map("Treeview.Heading", background=[("active", C.ACCENT)])

    s.configure("TCombobox", fieldbackground=C.ENTRY_BG, background=C.PANEL,
                foreground=C.TEXT, arrowcolor=C.TEXT, bordercolor=C.BORDER,
                lightcolor=C.BORDER, darkcolor=C.BORDER)
    s.map("TCombobox", fieldbackground=[("readonly", C.ENTRY_BG)],
          foreground=[("readonly", C.TEXT)])

    for arah in ("Vertical", "Horizontal"):
        s.configure(f"{arah}.TScrollbar", background=C.PANEL, troughcolor=C.BG,
                    bordercolor=C.BG, arrowcolor=C.TEXT)

    root.option_add("*TCombobox*Listbox.background", C.ENTRY_BG)
    root.option_add("*TCombobox*Listbox.foreground", C.TEXT)
    root.option_add("*TCombobox*Listbox.selectBackground", C.ACCENT)
