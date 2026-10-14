# 📐 Kalkulator Metode Tabel (Tabulasi) — Komputasi Numerik

Aplikasi GUI desktop (Python + Tkinter) untuk mencari akar persamaan non-linear
`f(x) = 0` dengan **Metode Tabel**, lengkap dengan tabel perhitungan dan grafik.

## Fitur

- Input fungsi bebas `f(x)` (parser SymPy, mendukung `2x`, `x^3`, `sin`, `cos`, `exp`, `ln`, `sqrt`, `pi`, `e`, dll.).
- Input batas bawah, batas atas, dan jumlah pembagian `N`.
- Tabel perhitungan: `i`, `x_i`, `f(x_i)`, tanda, `f(x_i)·f(x_i+1)`, pengecekan, dan penanda solusi.
- Akar dipilih dari titik yang **lebih dekat ke nol** di antara `|f(x_i)|` dan `|f(x_i+1)|`.
- Grafik `f(x)` pada interval beserta titik tabel dan titik akar (matplotlib).
- Semua angka tampil sebagai desimal biasa (tanpa notasi ilmiah / simbol `e`).

## Menjalankan

```bash
pip install -r requirements.txt
python main.py
```

> Linux: bila Tkinter belum ada, jalankan `sudo apt install python3-tk`.

## Menjalankan unit test

```bash
python -m unittest discover -s tests -t . -v
```

## Struktur proyek

```
kalkulator_metode_tabel/
├── main.py                  # titik masuk aplikasi
├── requirements.txt
├── docs/algoritma.md        # penjelasan algoritma + contoh
├── tabel_app/
│   ├── config.py            # tema warna, font, contoh fungsi, batas input
│   ├── formatting.py        # format angka tanpa notasi ilmiah, penanda tanda
│   ├── parser.py            # parser f(x) berbasis SymPy
│   ├── solver.py            # inti algoritma Metode Tabel (tanpa GUI)
│   └── ui/
│       ├── styles.py        # tema gelap ttk + utilitas warna
│       ├── header.py        # header gradien
│       ├── input_panel.py   # panel input + validasi
│       ├── result_cards.py  # kartu hasil + status
│       ├── table_view.py    # tab tabel perhitungan
│       ├── plot_view.py     # tab grafik
│       ├── algo_tab.py      # tab algoritma
│       └── app.py           # jendela utama (perakit komponen)
└── tests/                   # unit test parser, format, solver
```

## Pembagian tugas kelompok

| Anggota | Peran | Modul yang dikerjakan |
|---------|-------|------------------------|
| Anggota 1 | Ketua / integrasi | struktur proyek, `config.py`, `ui/app.py`, `main.py`, README |
| Anggota 2 | Parser & format | `parser.py`, `formatting.py`, `tests/test_parser.py`, `tests/test_formatting.py` |
| Anggota 3 | Algoritma inti | `solver.py`, `tests/test_solver.py`, `docs/algoritma.md` |
| Anggota 4 | UI input, hasil, tabel | `ui/styles.py`, `ui/input_panel.py`, `ui/result_cards.py`, `ui/table_view.py` |
| Anggota 5 | UI grafik & tampilan | `ui/header.py`, `ui/plot_view.py`, `ui/algo_tab.py` |

## Konvensi commit

Format pesan: `jenis(modul): deskripsi singkat` — contoh `feat(solver): algoritma metode tabel`.
Jenis yang dipakai: `feat`, `test`, `docs`, `chore`.
