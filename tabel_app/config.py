"""Konfigurasi global: tema warna, font, contoh fungsi, dan batas input."""

# ----- Warna tema -----
BG = "#0f172a"        # latar utama
PANEL = "#1e293b"     # panel
PANEL2 = "#162033"    # isi tabel
ENTRY_BG = "#0b1220"
BORDER = "#334155"
TEXT = "#e2e8f0"
MUTED = "#94a3b8"
ACCENT = "#7c3aed"
PINK = "#ec4899"
GREEN = "#10b981"
AMBER = "#f59e0b"
RED = "#f43f5e"

# Warna empat kartu hasil: akar, f(akar), step h, titik ke-i
WARNA_KARTU = ("#0891b2", "#d97706", "#059669", "#9333ea")

# ----- Font -----
FONT = ("Segoe UI", 10)
FONT_B = ("Segoe UI", 10, "bold")
FONT_H = ("Segoe UI", 11, "bold")
FONT_KECIL = ("Segoe UI", 9)
MONO = ("Consolas", 10)

# ----- Nilai bawaan & batas input -----
DEFAULT_INPUT = ("x^3 - x - 2", "1", "2", "10")   # f(x), x bawah, x atas, N
N_MAKS = 50000                                    # batas N agar tabel tetap lancar

# ----- Contoh fungsi: nama -> (f(x), x bawah, x atas) -----
PRESET = {
    "x^3 - x - 2": ("x^3 - x - 2", "1", "2"),
    "cos(x) - x": ("cos(x) - x", "0", "1"),
    "e^x - 3x": ("exp(x) - 3x", "0", "1"),
    "x^2 - 4": ("x^2 - 4", "0", "5"),
    "ln(x) + x - 2": ("ln(x) + x - 2", "0.5", "3"),
    "Kustom": None,
}
