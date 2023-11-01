import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_liikaa_ottaminen_ottaa_kaiken(self):
        self.varasto.lisaa_varastoon(8)

        # varastossa pitäisi olla saatavilla kahdeksan yksikköä tavaraa
        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 8)

    def test_negatiivisen_lisaaminen_ei_vahenna(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivisen_ottaminen_ottaa_nolla(self):
        self.varasto.lisaa_varastoon(5)
        saatu_maara = self.varasto.ota_varastosta(-3)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_negatiivisen_ottaminen_ei_lisaa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-3)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_liikaa_lisaaminen_hukkaa_ylimaaraiset(self):
        self.varasto.lisaa_varastoon(77)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_merkkijonoesitys_vastaa_totuutta(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_negatiivinen_tila_ei_mahdollinen(self):
        nega_varasto = Varasto(-7)
        self.assertAlmostEqual(nega_varasto.tilavuus, 0)

    def test_negatiivinen_tila__ja_saldo_ei_mahdollinen(self):
        nega_varasto = Varasto(-7,-3)
        self.assertAlmostEqual(nega_varasto.paljonko_mahtuu(), 0)
        self.assertAlmostEqual(nega_varasto.saldo, 0)

    def test_negatiivinen_alkusaldo_ei_lisaa_tilavuutta(self):
        monttu_varasto = Varasto(10,-5)
        self.assertAlmostEqual(monttu_varasto.paljonko_mahtuu(), 10)

    def test_ylisuuri_alkusaldo_menee_roskikseen(self):
        self.assertAlmostEqual(Varasto(10,100).saldo, 10)

    def test_negatiivinen_alkusaldo_tarkoittaa_tyhjaa(self):
        self.assertAlmostEqual(Varasto(10,-10).saldo, 0)
