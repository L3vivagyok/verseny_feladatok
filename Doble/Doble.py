import sys
import itertools

def generate_dobble_deck(n):
    """
    Generates a valid Dobble deck for the given size.

    Args:
        n (int): The size of the Dobble deck.

    Returns:
        list: The generated Dobble deck.
    """
    if n < 2:
        raise ValueError("A Dobble pakli legalább 2 különböző ábrát tartalmazhat.")

    symbols = list(range(1, n * n + 1))
    deck = []

    # Első kártya mindig tartalmazza az összes szimbólumot
    first_card = symbols[:n]
    deck.append(first_card)

    # Kártyák generálása
    for i in range(1, n):
        card = [symbols[0]] + [symbols[j] + n * (i - 1) for j in range(1, n)]
        deck.append(card)

    # Párok generálása
    pairs = list(itertools.combinations(range(1, n + 1), 2))
    for pair in pairs:
        symbol = pair[0]
        offset = pair[1]
        card = [symbols[symbol]]

        for i in range(1, n):
            card.append(symbols[n + (n - 1) * (i - 1) + (offset - 1) % (n - 1)])

        deck.append(card)

    return deck

def print_dobble_deck(deck):
    """
    Prints the contents of the Dobble deck.

    Args:
        deck (list): The Dobble deck to print.
    """
    for card in deck:
        print(" ".join(str(num) for num in card))

# Paraméter beolvasása
if len(sys.argv) != 2:
    print("Használat: python Doble.py <pakli mérete>")
    sys.exit(1)

n = int(sys.argv[1])

# Dobble pakli generálása
try:
    deck = generate_dobble_deck(n)
    print_dobble_deck(deck)
except ValueError as e:
    print(e)
    sys.exit(1)
