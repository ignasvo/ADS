def sudaryti_tvarkarasti(zaideju_skaicius):
    # Patikriname ar nelyginis, jei taip – pridedame laisvaji zaideja
    yra_nelyginis = (zaideju_skaicius % 2 != 0)
    if yra_nelyginis:
        zaideju_skaicius += 1 

    # Sukuriame zaideju sarasa
    zaidejai = list(range(1, zaideju_skaicius + 1))

    # Turu skaicius
    turu_skaicius = zaideju_skaicius - 1

    tvarkarastis = []

    for turas in range(turu_skaicius):
        poros = []

        for i in range(zaideju_skaicius // 2):
            a = zaidejai[i]
            b = zaidejai[zaideju_skaicius - 1 - i]

            # Praleidziame poras su laisvuoju zaideju
            if yra_nelyginis and (a == zaideju_skaicius or b == zaideju_skaicius):
                continue

            # Pakeiciame balta ir juoda spalvas
            if turas % 2 == 0:
                poros.append((a, b))  # a – baltais, b – juodais
            else:
                poros.append((b, a))  # b – baltais, a – juodais

        tvarkarastis.append(poros)

        # Rotacija
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