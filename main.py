import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import datetime


def CreateFile(plik):
    if plik == "wydatki.csv":
        with open(os.path.join("./dane", plik), "w") as fp:
            fp.write("data,kategoria,kwota\n")
    elif plik == "przychod.csv":
        with open(os.path.join("./dane", plik), "w") as fp:
            fp.write("data,zrodlo,kwota\n")
    elif plik == "test.csv":
        with open(os.path.join("./dane", plik), "w") as fp:
            fp.write("data,zrodlo,kategoria,kwota\n")


def FileAppend(plik, data_dict):
    df_istniejace = pd.read_csv(f"dane/{plik}")
    NowaLinia = pd.DataFrame([data_dict])
    df = pd.concat([df_istniejace, NowaLinia], ignore_index=True)
    df.to_csv(f"dane/{plik}", index=False)


def NowyWydatek():
    print(
        "Prosze podac date wykonania tego wydatku \n(W przypadku nie wybrania daty, data zostanie ustalona na dzisiejszy dzien)"
    )
    data_wyd = input("[YYYY-MM-DD]: ")
    if data_wyd == "" or data_wyd.isspace():
        dzis = datetime.date.today()
        data_wyd = f"{dzis.year}-{dzis.month}-{dzis.day}"
    kategoria = ""
    while kategoria.isspace() or kategoria.lower() == "exit":
        print(
            'Prosze podac kategorie \n(Aby opuscic dodawanie wydatku prosze napisac "exit")'
        )
        kategoria = input()
    if kategoria.lower() == "exit":
        return
    kwota = ""
    while kwota.isspace() or kwota.lower() == "exit":
        print(
            'Prosze podać kwote \n(Aby opuscic dodawanie kwoty prosze napisac "exit")'
        )
        kwota = input()
        if kwota.lower() == "exit":
            return
        if not kwota.isnumeric():
            kwota = ""
    kwota = int(kwota)

    data_dict = {"data": data_wyd, "kategoria": kategoria, "kwota": kwota}

    FileAppend("wydatki.csv", data_dict)


def NowtPrzychod():
    print(
        "Prosze podac date nowego przychodu \n (W przypadku nie wybrania daty, data zostanie ustalona na dzisiejszy dzien)"
    )
    data_przy = input("[YYYY-MM-DD]: ")
    if data_przy == "" or data_przy.isspace():
        dzis = datetime.date.today()
        data_przy = f"{dzis.year}-{dzis.month}-{dzis.day}"
    zrodlo = ""
    while zrodlo.isspace() or zrodlo.lower() == "exit":
        print(
            'Prosze podac zrodlo \n(Aby opuscic dodawanie przychodu prosze napisac "exit")'
        )
        zrodlo = input
    if zrodlo.lower() == "exit":
        return
    kwota = ""
    while kwota.isspace() or kwota.lower() == "exit":
        print(
            'Prosze podac kwote \n (Aby opuscic dodawanie kwoty prosze napisac "exit")'
        )
        kwota = input()
        if kwota.lower() == "exit":
            return
        if not kwota.isnumeric():
            kwota = ""
    kwota = int(kwota)

    data_dict = {"data": data_przy, "zrodlo": zrodlo, "kwota": kwota}

    FileAppend("przychod.csv", data_dict)


if not os.path.isdir("dane"):
    os.makedirs("dane")

if not os.path.isfile("dane/wydatki.csv"):
    print("Plik wydatki.csv nie istnieje \nCzy stworzyć ten plik?")
    OdpNowyPlik = input("[T/n]: ")
    if OdpNowyPlik.lower() != "n":
        CreateFile("wydatki.csv")
    else:
        pass

if not os.path.isfile("dane/przychod.csv"):
    print("Plik przychod.csv nie istnieje \n Czy stworzyć ten plik?")
    OdpNowyPlik = input("[T/n]: ")
    if OdpNowyPlik.lower() != "n":
        CreateFile("przychod.csv")
    else:
        pass

dane_wydatkow = pd.read_csv("dane/wydatki.csv", index_col=None, na_values=("NA"))
dane_przychodu = pd.read_csv("dane/przychod.csv", index_col=None, na_values=("NA"))

while True:
    print("""Witam w Programie do wizualizacji wydatkow i przycjodow
Prosze wybrac jedna z podanych opcji:
1. Dodanie nowego wydatku
2. Dodanie nowego przychodu 
3. wizualizacja wydatkow i przychodu
4. Opuszczenie programu 
""")

    dzialanie = input("[1-4]")

    if dzialanie == "4":
        print("dziekujemy za korzystanie z programu")
        break
    elif dzialanie == "1":  # nowy wydatek
        NowyWydatek()
    elif dzialanie == "2":  # nowy przychod
        pass
