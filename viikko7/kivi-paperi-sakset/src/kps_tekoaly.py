from kivi_paperi_sakset import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tekoaly):
        super().__init__()
        self.tekoaly = tekoaly
        self.tokan_siirto = ""

    def _toisen_siirto(self):
        self.tokan_siirto = self.tekoaly.anna_siirto()
        return self.tokan_siirto

    def _tulosta(self, tuomari):
        print(f"Tietokone valitsi: {self.tokan_siirto}")
        print(tuomari)