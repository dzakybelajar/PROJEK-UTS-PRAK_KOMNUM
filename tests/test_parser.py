import unittest

import numpy as np

from tabel_app.parser import parse_fungsi


class TestParser(unittest.TestCase):
    def test_polinom(self):
        _, f = parse_fungsi("x^3 - x - 2")
        self.assertAlmostEqual(f(2.0)[0], 4.0)

    def test_perkalian_implisit(self):
        _, f = parse_fungsi("2x + 1")
        self.assertAlmostEqual(f(3.0)[0], 7.0)

    def test_fungsi_dan_konstanta(self):
        _, f = parse_fungsi("ln(e) + cos(pi)")
        self.assertAlmostEqual(f(0.0)[0], 0.0)

    def test_vektor(self):
        _, f = parse_fungsi("x^2")
        np.testing.assert_allclose(f(np.array([1.0, 2.0, 3.0])), [1.0, 4.0, 9.0])

    def test_tak_terdefinisi_menjadi_nan(self):
        _, f = parse_fungsi("1/x")
        self.assertTrue(np.isnan(f(0.0)[0]))

    def test_variabel_asing_ditolak(self):
        with self.assertRaises(ValueError):
            parse_fungsi("x + y")

    def test_sintaks_salah_ditolak(self):
        with self.assertRaises(ValueError):
            parse_fungsi("x +* 2")


if __name__ == "__main__":
    unittest.main()
