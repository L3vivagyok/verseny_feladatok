import re

# A választék
menu = {
    'pizzák': {
        'margherita': 1000,
        'sonkás': 1200,
        'gombás': 1100,
    },
    'plusz feltétek': {
        'kukorica': 100,
        'hagyma': 150,
        'olívabogyó': 200,
    },
    'innivalók': {
        'kóla': 300,
        'ásványvíz': 200,
        'narancslé': 250,
    }
}

# Rendelési állomány inicializálása
rendeles = {
    'pizzák': [],
    'plusz feltétek': [],
    'innivalók': [],
    'vegosszeg': 0
}


# Felhasználói interakció és rendelés felvétele
def rendeles_felvetel():
    print("Online rendelés Asszisztens: Üdvözlöm! A mai nap én fogok segíteni magának megrendelni a pizzáját.")
    print("A választható pizzák:")
    for pizza in menu['pizzák']:
        print("- " + pizza)
    print("A választható plusz feltétek:")
    for feltet in menu['plusz feltétek']:
        print("- " + feltet)
    print("A választható innivalók:")
    for ital in menu['innivalók']:
        print("- " + ital)
    print("Mit szeretne rendelni?")

    # Pizza kiválasztása
    while True:
        user_input = input("FELHASZNÁLÓ: ").lower()

        # Keresés a választékban
        for kategoria, elemek in menu.items():
            for elem, ar in elemek.items():
                if re.search(fr'\b{elem}\b', user_input):
                    rendeles[kategoria].append(elem)
                    rendeles['vegosszeg'] += ar
                    print(f"Online rendelés Asszisztens: Hozzáadva a rendeléshez: {elem}")
                    break
            else:
                continue  # Külső for ciklus következő iterációja
            break  # Belső for ciklus megszakítása

        if rendeles['pizzák']:  # Ellenőrizzük, hogy van-e kiválasztott pizza
            break  # Kilépünk a while ciklusból, ha van kiválasztott pizza

    # Feltét kiválasztása (ha van pizza kiválasztva)
    if rendeles['pizzák']:
        for pizza in rendeles['pizzák']:
            valaszt = input(
                f"Online rendelés Asszisztens: Szeretne plusz feltétet a(z) {pizza} pizzájára? (igen/nem): ").lower()
            if valaszt == "igen":
                print("Online rendelés Asszisztens: Milyen plusz feltétet szeretne?")
                print("A választható plusz feltétek:")
                for feltet in menu['plusz feltétek']:
                    print("- " + feltet)
                user_input = input("FELHASZNÁLÓ: ").lower()
                for elem, ar in menu['plusz feltétek'].items():
                    if re.search(fr'\b{elem}\b', user_input):
                        rendeles['plusz feltétek'].append(elem)
                        rendeles['vegosszeg'] += ar
                        print(f"Online rendelés Asszisztens: Hozzáadva a rendeléshez: {elem}")

    # Üdítő kiválasztása (ha van pizza kiválasztva)
    if rendeles['pizzák']:
        print("Online rendelés Asszisztens: Rendben, milyen üdítőt szeretne?")
        print("A választható innivalók:")
        for ital in menu['innivalók']:
            print("- " + ital)
        while True:
            user_input = input("FELHASZNÁLÓ: ").lower()

            for elem, ar in menu['innivalók'].items():
                if re.search(fr'\b{elem}\b', user_input):
                    rendeles['innivalók'].append(elem)
                    rendeles['vegosszeg'] += ar
                    print(f"Online rendelés Asszisztens: Hozzáadva a rendeléshez: {elem}")
                    break
            else:
                print(
                    "Online rendelés Asszisztens: Sajnálom, de az adott üdítő nincs a választékban. Kérlek, válassz újat.")
                continue  # Kilépünk a while ciklus jelenlegi iterációjából és újra kérdezzük az üdítőt
            break  # Kilépünk a while ciklusból, ha sikerült választ adni az üdítőre

    # Rendelési állomány kiíratása
    print("Online rendelés Asszisztens: A rendelési állomány:")
    for kategoria, elemek in rendeles.items():
        if kategoria != 'vegosszeg' and elemek:
            print(kategoria.capitalize() + ":")
            for elem in elemek:
                print(f"- {elem}")
    print("Végösszeg: " + str(rendeles['vegosszeg']) + " Ft")
    print("Online rendelés Asszisztens: Köszönjük a rendelést!")

    # További rendelés
    valaszt = input("Online rendelés Asszisztens: Szeretne még valamit rendelni? (igen/nem): ").lower()
    if valaszt == "igen":
        rendeles_felvetel()
    else:
        print("Rendben, a rendelése felvéve, köszönöm, hogy minket választott!")


# Rendelés felvétele
rendeles_felvetel()
