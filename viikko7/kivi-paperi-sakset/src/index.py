from pelitehdas import Pelitehdas

def main():
    tehdas = Pelitehdas()
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        peli = tehdas.luo_peli(vastaus)

        if not peli:
            break
        
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        peli.pelaa()


if __name__ == "__main__":
    main()
