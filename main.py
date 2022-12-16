import os
data = {
    "1": {
        "imie": "Jan",
        "nazwisko": "Nowak",
        "nr_konta": "001",
        "saldo": 1457.23
    },

    "2": {
        "imie": "Agnieszka",
        "nazwisko": "Kowalska",
        "nr_konta": "002",
        "saldo": 3600.18
    },

    "3": {
        "imie": "Robert",
        "nazwisko": "Lewandowski",
        "nr_konta": "003",
        "saldo": 2745.03
    },

    "4": {
        "imie": "Zofia",
        "nazwisko": "Plucińska",
        "nr_konta": "004",
        "saldo": 7344.00
    },

    "5": {
        "imie": "Grzegorz",
        "nazwisko": "Braun",
        "nr_konta": "005",
        "saldo": 455.38
    }

}


# ----------------- CLEAR ---------------- #
def clear():
    os.system('cls')


# ----------- WYSWIETLA BAZE ------------ #
def show_database(do_clear):
    if do_clear:
        clear()
    print("ID | IMIĘ I NAZWISKO | NR KONTA | SALDO")
    for i in range(1, len(data)+1):
        i = str(i)
        imie = data[i]['imie']
        nazwisko = data[i]['nazwisko']
        nr_konta = data[i]['nr_konta']
        saldo = str(data[i]['saldo'])
        print(i + " | " + imie + " " + nazwisko + " | " + nr_konta + " | " + saldo + " zł")


# ---------- LOGOWANIE ----------- #
def login():
    clear()
    id = input("ZALOGUJ SIĘ WYBIERAJĄC ID KLIENTA: ")
    clear()
    if id not in data:
        return print("LOGOWANIE NIEUDANE")
    if id in data:
        imie = data[id]['imie']
        nazwisko = data[id]['nazwisko']
        nr_konta = data[id]['nr_konta']
        saldo = data[id]['saldo']
        print("ZALOGOWANY KLIENT")
        print(f"ID: {id}")
        print(f"IMIĘ I NAZWISKO: {imie} {nazwisko}")
        print(f"NR KONTA: {nr_konta}")
        print(f"SALDO: {saldo} zł")
        przelew_na = input("WPISZ NUMER KONTA NA KTÓRY CHCESZ WYKONAĆ PRZELEW (00x): ")
        nr_kont = []
        for konto in data:
            nr_kont.append((data[str(konto)]['nr_konta']))
        if przelew_na not in nr_kont:
            clear()
            return print("NIEPRAWIDŁOWY NUMER KONTA")
        if przelew_na == nr_konta:
            clear()
            return print('NIE MOŻESZ ZROBIĆ PRZELEWU NA WŁASNE KONTO.')
    clear()
    kwota_przelewu = float(input("PODAJ KWOTĘ PRZELEWU: "))
    if kwota_przelewu > saldo:
        clear()
        return print("NIEWYSTARCZAJĄCE ŚRODKI NA RACHUNKU")
    else:
        clear()
        stare_saldo = float(data[przelew_na.strip('0')]['saldo'])
        data[przelew_na.strip('0')]['saldo'] = stare_saldo + kwota_przelewu
        print("PRZELEW ZOSTAŁ WYKONANY")
        nowe_saldo = saldo - kwota_przelewu
        data[id]['saldo'] = nowe_saldo
        show_database(False)



is_sending = True
while is_sending:
    print("WYBIERZ OPCJĘ:")
    print("1 => LISTA WSZYSTKICH KLIENTÓW BANKU")
    print("2 => LOGOWANIE")
    print("3 => ZAKOŃCZ PROGRAM")
    wybor = int(input("WYBIERZ 1, 2 LUB 3: "))
    if wybor == 1:
        show_database(True)
    if wybor == 2:
        login()
        is_sending = False
    if wybor == 3:
        is_sending = False

# Created by Jakub Szpytka
