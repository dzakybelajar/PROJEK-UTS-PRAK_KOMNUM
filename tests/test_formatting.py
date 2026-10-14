import unittest

from tabel_app.formatting import fmt, tanda


class TestFormatting(unittest.TestCase):
    def test_angka_kecil_tanpa_notasi_ilmiah(self):
        self.assertEqual(fmt(0.000001), "0.000001")
        self.assertNotIn("e", fmt(1e-9, 12))

    def test_nol_di_belakang_dibuang(self):
        self.assertEqual(fmt(2.5), "2.5")
        self.assertEqual(fmt(100.0), "100")

    def test_nol_negatif_dan_nan(self):
        self.assertEqual(fmt(-0.0), "0")
        self.assertEqual(fmt(float("nan")), "—")
        self.assertEqual(fmt(None), "—")

    def test_tanda(self):
        self.assertEqual(tanda(3.0), "+")
        self.assertEqual(tanda(-3.0), "−")
        self.assertEqual(tanda(0.0), "0")
        self.assertEqual(tanda(float("nan")), "n/a")


if __name__ == "__main__":
    unittest.main()
