import random
# zad 1
# lista1 = [random.randint(1, 101) for x in range(21)]
# print(lista1)
# lista2 = [x for x in lista1 if x % 4 == 0]
# print(lista2)
# file = open("lab4zad1.txt", "w")
# string = ""
# for x in lista2:
#     string = string + str(x) + ", "
# file.write(string)
# file.close()
# zad 2
# file = open("lab4zad1.txt", "r")
# print(file.read())
# file.close()
# zad 3
# with open('lab4zad3.txt', 'r+') as file:
#     file.write('piewrwsza linijka tekstu\n')
#     file.write('druga linijka tekstu\n')
#     file.write('trzecia linijka tekstu\n')
# file1 = open("lab4zad3.txt", "r")
# print(file1.read())
# zad 4
# class NaZakupy():
#     nazwaproduktu = ""
#     ilosc = 0
#     jednostka_miary = ""
#     cena_jed = 0
#     def __init__(self, nazwaproduktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwaproduktu = nazwaproduktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#     def wyswietl_produkt(self):
#         print(self.nazwaproduktu+"\t", str(self.ilosc)+"\t", self.jednostka_miary+"\t", str(self.cena_jed))
#     def ile_produktu(self):
#         print(str(self.ilosc)+" "+self.jednostka_miary)
#     def ile_kosztuje(self):
#         print(str(self.ilosc * self.cena_jed))
#
# pomidor = NaZakupy("malinowy", 5, "szt", 2.00)
# pomidor.wyswietl_produkt()
# pomidor.ile_produktu()
# pomidor.ile_kosztuje()
# zad 5
# class ciagi_arytmetyczne():
#     elementy = []
#     def __init__(self, elementy):
#         self.elementy = elementy
#     def wyswietl_dane(self):
#         print(self.elementy)
#     def pobierz_paramentry(self, a1, r, ilosc):
#         self.elementy = []
#         for x in range(ilosc):
#             self.elementy.append((a1 + (x * r)))
#     def policz_sume(self):
#         suma = 0
#         for x in self.elementy:
#             suma += x
#         print(suma)
# ciag = ciagi_arytmetyczne([3,5,7])
# ciag.wyswietl_dane()
# ciag.pobierz_paramentry(2,2,10)
# ciag.wyswietl_dane()
# ciag.policz_sume()
# zad 6
# class robaczek():
#     x = 0
#     y = 0
#     krok = 1
#     def __init__(self, x , y, krok):
#         self.x =x
#         self.y =y
#         self.krok =krok
#     def idz_w_gore(self, ile_krokow):
#         self.y += (ile_krokow * self.krok)
#     def idz_w_dol(self, ile_krokow):
#         self.y -= (ile_krokow * self.krok)
#     def idz_w_lewo(self, ile_krokow):
#         self.x -= (ile_krokow * self.krok)
#     def idz_w_prawo(self, ile_krokow):
#         self.x += (ile_krokow * self.krok)
#     def pokaz_gdzie_jestes(self):
#         print(str(self.x)+","+str(self.y))
# robak1 = robaczek(1,2,2)
# robak1.idz_w_gore(5)
# robak1.idz_w_dol(3)
# robak1.idz_w_prawo(10)
# robak1.idz_w_lewo(4)
# robak1.pokaz_gdzie_jestes()
