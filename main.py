from spillebrett import Spillebrett

def main():
    rad = int(input("Antall rader: "))
    kol = int(input("Antall kolonner: "))
    brett = Spillebrett(rad, kol)
    brett.generer()
    brett.tegnBrett()
    print("Generasjon: {} --- Antall levende celler: {}".format(brett.gen, brett.finnAntallLevende()))


    msg = ''
    while msg != 'q':
        brett.oppdatering()
        brett.tegnBrett()
        print("Generasjon: {} --- Antall levende celler: {}".format(brett.gen, brett.finnAntallLevende()))
        msg = input("Press enter to countinue to next generation, og 'q' to quit.")

main()