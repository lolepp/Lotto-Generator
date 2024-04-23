import random

def supernumber():
    return random.randint(1, 9)

def six_to_49():
    lst = []
    for _ in range(6):
        rand = random.randint(1, 49)
        while lst.__contains__(rand):
            rand = random.randint(1, 49)
        lst.append(rand)
    return sorted(lst)

def main():
    lst = six_to_49()
    lotto = ", ".join(str(num) for num in lst)
    print(f"Das sind die (korrekten) Lottozahlen:\n{lotto} mit Superzahl {supernumber()}")

if __name__ == "__main__":
    main()
