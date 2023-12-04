class Operaatio:
    def __init__(self, sl, arvo):
        self.sl = sl
        self.arvo = arvo

    def suorita():
        return 0

class Summa(Operaatio):
    def __init__(self, sl, arvo):
        super().__init__(sl, arvo)

    def suorita(self):
        luku = int(self.arvo())
        self.sl.aseta_edellinen(self.sl.tulos)
        self.sl.aseta_arvo(self.sl.tulos + luku)

class Erotus(Operaatio):
    def __init__(self, sl, arvo):
        super().__init__(sl, arvo)

    def suorita(self):
        luku = int(self.arvo())
        self.sl.aseta_edellinen(self.sl.tulos)
        self.sl.aseta_arvo(self.sl.tulos - luku)

class Nollaus(Operaatio):
    def __init__(self, sl, arvo):
        super().__init__(sl, arvo)

    def suorita(self):
        self.sl.aseta_edellinen(self.sl.tulos)
        self.sl.aseta_arvo(0)

class Kumoa(Operaatio):
    def __init__(self, sl, arvo):
        super().__init__(sl, arvo)

    def suorita(self):
        self.sl.aseta_arvo(self.sl.edellinen)