# Algoritma Metode Tabel (Tabulasi)

Metode Tabel mencari akar f(x) = 0 dengan membagi interval menjadi N bagian
sama lebar, lalu mencari titik tabel yang nilainya paling dekat ke nol.

## Langkah

1. Definisikan fungsi f(x).
2. Tentukan batas bawah `x_bawah` dan batas atas `x_atas`.
3. Tentukan jumlah pembagian `N`.
4. Hitung step `h = (x_atas - x_bawah) / N`.
5. Untuk `i = 0 .. N` hitung `x_i = x_bawah + i.h` dan `y_i = f(x_i)`.
6. Untuk `i = 0 .. N` periksa:
   - Bila `f(x_i) = 0`, maka `x_i` adalah penyelesaian.
   - Bila `f(x_i) . f(x_i+1) < 0` (tanda berubah):
     - bila `|f(x_i)| < |f(x_i+1)|` maka `x_i` adalah penyelesaian,
     - bila tidak maka `x_i+1` adalah penyelesaian.

## Contoh

`f(x) = x^3 - x - 2`, interval `[1, 2]`, `N = 10` (`h = 0.1`):

| i | x_i | f(x_i) | Keterangan |
|---|-----|--------|------------|
| 5 | 1.5 | -0.125 | tanda berubah, `\|f(x_5)\| < \|f(x_6)\|` -> `x_5` penyelesaian |
| 6 | 1.6 | 0.496  | |

Akar sebenarnya sekitar 1.5213797; makin besar N, hasil makin akurat.

## Keterbatasan

- Akar kembar (mis. `x^2`) tidak mengubah tanda sehingga tidak terdeteksi.
- Titik diskontinu seperti `1/x` atau `tan(x)` dapat memberi perubahan tanda palsu.
- Ketelitian dibatasi oleh `h`; perkecil `h` dengan memperbesar N.
