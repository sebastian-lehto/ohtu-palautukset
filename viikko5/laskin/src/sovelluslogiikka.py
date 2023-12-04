class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = 0

    def arvo(self):
        return self.tulos

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def edellinen(self):
        return self.edellinen
    
    def aseta_edellinen(self, arvo):
        self.edellinen = arvo