import unittest

import numpy as np

from tabel_app.parser import parse_fungsi
from tabel_app.solver import metode_tabel


class TestSolver(unittest.TestCase):
    def test_pilih_titik_lebih_dekat_ke_nol_xi(self):
        # f(1.5) = -0.125, f(1.6) = 0.496 -> x_i (1.5) lebih dekat ke nol
        _, f = parse_fungsi("x^3 - x - 2")
        hasil = metode_tabel(f, 1, 2, 10)
        self.assertEqual(hasil.indeks_akar, 5)
        self.assertAlmostEqual(hasil.akar, 1.5)

    def test_pilih_titik_lebih_dekat_ke_nol_xi_berikutnya(self):
        # f(0) = -0.9, f(1) = 0.1 -> x_i+1 (1) lebih dekat ke nol
        hasil = metode_tabel(lambda x: x - 0.9, 0, 2, 2)
        self.assertEqual(hasil.indeks_akar, 1)
        self.assertAlmostEqual(hasil.akar, 1.0)

    def test_akar_tepat(self):
        _, f = parse_fungsi("x^2 - 4")
        hasil = metode_tabel(f, 0, 5, 10)
        self.assertEqual(hasil.solusi, [4])
        self.assertEqual(hasil.f_akar, 0.0)

    def test_banyak_akar(self):
        _, f = parse_fungsi("x^3 - 6x^2 + 11x - 6")
        hasil = metode_tabel(f, 0, 4, 8)
        np.testing.assert_allclose(hasil.xs[hasil.solusi], [1.0, 2.0, 3.0])

    def test_tanpa_solusi(self):
        _, f = parse_fungsi("x^2 + 1")
        hasil = metode_tabel(f, -2, 2, 10)
        self.assertFalse(hasil.ada_solusi)
        self.assertIsNone(hasil.akar)

    def test_step_dan_jumlah_baris(self):
        _, f = parse_fungsi("x")
        hasil = metode_tabel(f, 0, 1, 4)
        self.assertAlmostEqual(hasil.h, 0.25)
        self.assertEqual(len(hasil.baris), 5)

    def test_nilai_tak_terdefinisi_tidak_jadi_solusi(self):
        _, f = parse_fungsi("1/x")
        hasil = metode_tabel(f, -1, 1, 2)   # x = -1, 0, 1 -> f(0) = NaN
        self.assertFalse(hasil.ada_solusi)

    def test_input_tidak_valid(self):
        _, f = parse_fungsi("x")
        with self.assertRaises(ValueError):
            metode_tabel(f, 0, 1, 0)
        with self.assertRaises(ValueError):
            metode_tabel(f, 2, 1, 5)


if __name__ == "__main__":
    unittest.main()
