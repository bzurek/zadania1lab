import random
import math
# zad1
# a = [(1 - x) for x in range(1, 11)]
# b = [4 ** i for i in range(8)]
# c = [x for x in b if x % 2 == 0]
# print(a)
# print(b)
# print(c)
# zad 2
# lista1 = [random.randint(1, 30) for x in range(10)]
# print(lista1)
# lista2 = [x for x in lista1 if x % 2 == 0]
# print(lista2)
# zad3
# slownik = {"chleb": "sztuki",
#            "ziemniaki": "kg",
#            "gruszki": "kg",
#            "mandarynki": "kg",
#            "czekolada": "sztuki",
#            "batonik": "sztuki"}
# print(slownik)
# slownik1 = {key: value for (key, value) in slownik.items() if value == "sztuki"}
# print(slownik1)
# zad 4
# def czy_prostokatny(a, b, c):
#     if a ** 2 + b ** 2 == c ** 2:
#         print("Jest to trojkat prostokatny")
#     else:
#         print("Nie jest to trojkat prostokatny")
# czy_prostokatny(3,4,5)
# zad 5
# def pole_trapezu(a = 2, b = 3, h = 4):
#     pole = ((a+b) * h) / 2
#     return pole
# print(pole_trapezu())
# zad 6
# def ciag(a=1, b =4, ile = 10):
#     elementy = [a * (b ** i) for i in range(ile)]
#     iloczyn = math.prod(elementy)
#     print(elementy)
#     return iloczyn
# print(ciag())
# zad 7
# def ciag(a=1, b =4, ile = 10):
#     elementy = [a * (b ** i) for i in range(ile)]
#     iloczyn = 1
#     print(elementy)
#     for x in elementy:
#         iloczyn *= x
#     return iloczyn
# print(ciag())
# zad 8
# slownik1 = {"chleb": 3.59,
#            "ziemniaki": 2.99,
#            "gruszki": 3.99,
#            "mandarynki": 2.59,
#            "czekolada": 3.50,
#            "batonik": 1.99}
# def suma(slownik):
#     suma = 0
#     for item in slownik.values():
#         suma += item
#     print(len(slownik))
#     return suma
# print(suma(slownik1))
