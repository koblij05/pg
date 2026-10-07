def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100

    cislo = int(cislo)

    if cislo < 0 or cislo > 100:
        return "Číslo mimo rozsah"

    if cislo == 0:
        return "nula"

    if cislo == 100:
        return "sto"

    if cislo >= 10 and cislo < 20:
        texty = {
            10: "deset",
            11: "jedenáct",
            12: "dvanáct",
            13: "třináct",
            14: "čtrnáct",
            15: "patnáct",
            16: "šestnáct",
            17: "sedmnáct",
            18: "osmnáct",
            19: "devatenáct"
        }
        return texty[cislo] 

    texty = {
        1: "jedna",
        2: "dva",
        3: "tři",
        4: "čtyři",
        5: "pět",
        6: "šest",
        7: "sedm",
        8: "osm",
        9: "devět"
    }
    
    if cislo >= 0 and cislo < 10:
        return texty[cislo]
    
    texty.update({
        20: "dvacet",
        30: "třicet",
        40: "čtyřicet",
        50: "padesát",
        60: "šedesát",
        70: "sedmdesát",
        80: "osmdesát",
        90: "devadesát"
    })

    desitky = cislo // 10 * 10
    zbytek = cislo % 10

    if zbytek == 0:
        return texty[desitky]
    else:
        return f"{texty[desitky]} {texty[zbytek]}"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)