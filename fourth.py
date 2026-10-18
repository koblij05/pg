def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Implementace pravidel pohybu pro různé figury zde.

    x, y = cilova_pozice

    # cíl mimo šachovnici
    if x < 1 or x > 8 or y < 1 or y > 8:
        print("Debug: je mimo")
        return False
    
    # cíl je obsazený
    if (x, y) in obsazene_pozice:
        print("Debug: obsazeno")
        return False

    # tah není přípustný
    dx = cilova_pozice[0] - figurka["pozice"][0]
    dy = cilova_pozice[1] - figurka["pozice"][1]
    print("Debug: pohyb o", dx, dy)
    if dx == 0 and dy == 0:
        print("Debug: bez pohybu")
        return False
    if figurka["typ"] == "pěšec":
        if not ((dx == 1 or (dx == 2 and figurka["pozice"][0] == 2)) and dy == 0):
            print("Debug: nepřípustný tah pěšcem")
            return False
    if figurka["typ"] == "jezdec":
        if not ((abs(dx) == 1 and abs(dy) == 2) or (abs(dx) == 2 and abs(dy) == 1)):
            print("Debug: nepřípustný tah jezdcem")
            return False
    if figurka["typ"] == "věž":
        if not (dx == 0 or dy == 0):
            print("Debug: nepřípustný tah věže")
            return False
    if figurka["typ"] == "střelec":
        if not (abs(dx) == abs(dy)):
            print("Debug: nepřípustný tah střelce")
            return False
    if figurka["typ"] == "dáma":
        if not (dx == 0 or dy == 0 or abs(dx) == abs(dy)):
            print("Debug: nepřípustný tah dámy")
            return False
    if figurka["typ"] == "král":
        if not ((dx == 0 or dy == 0 or abs(dx) == abs(dy)) and (abs(dx) <= 1 and abs(dy) <= 1)):
            print("Debug: nepřípustný tah krále")
            return False

    # něco je v cestě
    if figurka["typ"] == "pěšec" and dx == 2:
        if (figurka["pozice"][0] + 1, figurka["pozice"][1]) in obsazene_pozice:
            print("Debug: cesta pěšce obsazená")
            return False
    if figurka["typ"] in ("věž", "střelec", "dáma"):
        _x, _y = figurka["pozice"]
        pocet_kroku = max(abs(dx), abs(dy))
        for i in range(1, pocet_kroku):
            if dx > 0:
                _x += 1
            elif dx < 0:
                _x -= 1
            if dy > 0:
                _y += 1
            elif dy < 0:
                _y -= 1
            if (_x, _y) in obsazene_pozice:
                print(F"Debug: cesta {figurka["typ"]} obsazená")
                return False

    return True

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True