from abc import ABC, abstractmethod
from datetime import datetime
class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def tulajdonsag(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, dohanyzo):
        super().__init__(ar, szobaszam)
        self.dohanyzo = dohanyzo

    def tulajdonsag(self):
        print(f"Egyágyas szoba: Szobaszám: {self.szobaszam}, Ár: {self.ar} Ft, Dohányzó: {self.dohanyzo}")

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, kilatas):
        super().__init__(ar, szobaszam)
        self.kilatas = kilatas

    def tulajdonsag(self):
        print(f"Egyágyas szoba: Szobaszám: {self.szobaszam}, Ár: {self.ar} Ft, Kilátás: {self.kilatas}")

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def __add__(self, szoba):
        self.szobak.append(szoba)

    #def list_szobak(self):
    #    for szoba in self.szobak:
    #        szoba.tulajdonsag()

    def foglalasok(self, szoba, datum, szam):
        if not self.szoba_szabad(szoba, datum):
            print("A kiválasztott szoba nem elérhető. Kérjük válasszon másikat.")
            return None

        foglalasok = Foglalas(szoba, datum, szam)
        self.foglalasok.append(foglalasok)
        print("Sikeres foglalás!")
        return foglalasok

    def szoba_szabad(self, szoba, datum):
        for foglalasok in self.foglalasok:
            if foglalasok.szoba == szoba and foglalasok.datum == datum:
                return False
            return True

    def lemondas(self, foglalasok):
        if foglalasok in self.foglalasok:
            self.foglalasok.remove(foglalasok)
            print(f"Foglalés törölve!")
        else:
            print("Nincs ilyen foglalás.")

    def list_foglalasok(self):
        print(f"A {self.nev} nevű szálloda foglalásai:")
        for foglalasok in self.foglalasok:
            print(f"Szobaszám: {foglalasok.szoba.szobaszam}, Ár: {self.foglalasok.szoba.ar} FT, Dátum: {foglalasok.szoba.datum}, Foglalási azonosító: {self.foglalasok.szam}")
class Foglalas:
    def __init__(self, szobaszam, datum, szam):
        self.szobaszam = szobaszam
        self.datum = datum
        self.foglalasok.szam = szam

sz1 = EgyagyasSzoba(5000, 102, True)
sz2 = KetagyasSzoba(8000, 110, False)
sz3 = EgyagyasSzoba(2700, 108, False)

szalloda = Szalloda("Elmeny es SPA Resort")
szalloda.add_szoba(sz1)
szalloda.add_szoba(sz2)
szalloda.add_szoba(sz3)

f1 = szalloda.foglalasok((sz1, ))
f2 = szalloda.foglalasok(sz2)
f3 = szalloda.foglalasok(sz3)
f4 = szalloda.foglalasok(sz1)
f5 = szalloda.foglalasok(sz3)

foglalas_egyagyas = szalloda.foglalasok(EgyagyasSzoba, (2023, 11, 30))
foglalas_ketagyas = szalloda.foglalasok(KetagyasSzoba, (2023, 12, 1))

szalloda.list_foglalasok()
szalloda.lemondas()
szalloda.list_foglalasok()

while True:
    print("Válasszon: ")
    print("1. Foglalás ")
    print("2. Lemondás ")
    print("3. Listázás ")

    muvelet = input("1-4: ")

    if muvelet == "1":
        szalloda.list_foglalasok()
        szobaszam = input("Válasszon egy szobát: ")
        datum = input("Adjon meg egy dátumot: ")

        datum = datetime.datetime()
        ma = datetime.today()

        if szobaszam and datum not in szalloda.list_foglalasok() and datum >= ma:
            print("Sikeres foglalás!")
        else:
            print("Ez a szoba nem elérhető az Ön által választott időpontban. Kérjük válasszson másik szobát/időpontot.")

    elif muvelet == "2":
        szalloda.list_foglalasok()
        szalloda.list_foglalasok()
        szam = input("Adja meg a foglalási azonosítót: ")

        if szam in szalloda.list_foglalasok():
            print("Törölni szeretné a foglalást? ")
        else:
            print("Nincs ilyen foglalás a rendszerben.")

    elif muvelet == "3":
        szalloda.list_foglalasok()

    else:
        raise ValueError ("Kérjük válasszon a lehetséges műveletek közük.")