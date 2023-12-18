from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from tekoaly_parannettu import TekoalyParannettu
from tekoaly import Tekoaly

class Pelitehdas:
    
    def luo_peli(self, tyyppi):
        if tyyppi == 'a':
            return KPSPelaajaVsPelaaja()
        if tyyppi == 'b':
            tekoaly = Tekoaly()
            return KPSTekoaly(tekoaly)
        if tyyppi == 'c':
            tekoaly = TekoalyParannettu(10)
            return KPSTekoaly(tekoaly)

        return None
    
    