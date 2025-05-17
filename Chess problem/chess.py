def sudaryti_tvarkarasti(zaideju_skaicius):
    # Patikriname ar nelyginis, jei taip – pridedame "bye" (laisvas turas)
    yra_nelyginis = (zaideju_skaicius % 2 != 0)
    if yra_nelyginis:
        zaideju_skaicius += 1  # Pridedame vieną "laisvą" vietą

    # Sukuriame sąrašą žaidėjų (1...n)
    zaidejai = list(range(1, zaideju_skaicius + 1))

    # Kiek turų reikia?
    turu_skaicius = zaideju_skaicius - 1

    tvarkarastis = []

    for turas in range(turu_skaicius):
        poros = []

        for i in range(zaideju_skaicius // 2):
            a = zaidejai[i]
            b = zaidejai[zaideju_skaicius - 1 - i]

            # Praleidžiame, jei yra "laisvasis"
            if yra_nelyginis and (a == zaideju_skaicius or b == zaideju_skaicius):
                continue

            # Pakeičiame spalvas pakaitomis kiekviename ture
            if turas % 2 == 0:
                poros.append((a, b))  # a – baltais, b – juodais
            else:
                poros.append((b, a))  # b – baltais, a – juodais

        tvarkarastis.append(poros)

        # Rotacija: paliekam pirmą, likusius sukame
        zaidejai = [zaidejai[0]] + [zaidejai[-1]] + zaidejai[1:-1]

    return tvarkarastis

def spausdinti_tvarkarasti(tvarkarastis):
    for i, turas in enumerate(tvarkarastis, 1):
        print(f"{i}-as turas:")
        for baltais, juodais in turas:
            print(f"  Zaidejas {baltais} (balti) vs Zaidejas {juodais} (juodi)")
        print()

def main():
    n = int(input("Iveskite zaideju skaiciu: "))
    tvarkarastis = sudaryti_tvarkarasti(n)
    spausdinti_tvarkarasti(tvarkarastis)

if __name__ == "__main__":
    main()