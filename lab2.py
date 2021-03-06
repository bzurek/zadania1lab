# Zad 1
# filmy = ['Batman', 'Harry Potter', 'Nietykalni', 'Atlas Chmur', 'Interstellar']
# print(filmy)
# for i in reversed(filmy):
#     print(i)
# filmy.insert(5, 'Wielkie piekno')
# filmy.insert(6, 'Zjawa')
# filmy.insert(7, 'Ostatnia rodzina')
# filmy.insert(8, 'Coco')
# filmy.insert(9, 'Spider-Man')
# print(filmy)
# zad 2
# slownik = {
#     "fantasy" : 'Harry Potter',
#     "akcja" : {"Batman", "Spider-Man"},
#     "komediodramat" : "Nietykalni",
#     "fantastyka naukowa" : "Atlas Chmur",
#     "Sci-Fi" : "Interstellar",
#     "komedia" : "Wielkie piekno",
#     "film przygodowy" : "Zjawa",
#     "dramat filmowy" : "Ostatnia rodzina",
#     "animacja" : "Coco"
# }
# print(slownik)
# print(slownik["akcja"])
# zad 3
# przedmioty = {
#     "CAD" : "Komputerowe wspomaganie programowania",
#     "WD" : "Wizualizacja danych",
#     "RRiC" : "Rachunek rozniczkowy i calkowy",
#     "EMD" : "Elementy matematyki dyskretnej",
#     "PS" : "Programowanie strukturalne",
# }
# print(len(przedmioty))
# zad 4
# a= float(input('Podaj liczbe a:'))
# print((a * a))
# zad 5
# f = open('tekst.txt', 'r+')
# a = f.readline()
# print(a)
# substring = "a"
# count = a.count(substring)
# s = str(count)
# b = f.write(s)
# zad 6
# a = input("podaj a: ")
# b = input("podaj b: ")
# c = input("podaj c: ")
# if ((int (a) % 2 == 0) & (b>c)):
#     print("jest parzysta oraz b jest wieksze od c")
# else:
#     print("nie jest parzysta")
# zad 7
# lista = [5, 4, 8, 4.2, 5.1, 7.5, 7, 9, 8.4, 5.2]
# print(lista[0])
# for x in range(1, len(lista)):
#     print(lista[x] + lista[x-1])
# zad 8
# lista = []
# wyliczenie = 0
# while wyliczenie < 10:
#     a = input("podaj liczbe: ")
#     wyliczenie = wyliczenie + 1
#     try:
#         b = int(a)
#         lista.append(b)
#     except ValueError:
#         continue
# print(lista)
# zad 9
# lista = [1, 2, 3, 4, 5, 6]
# for i in lista:
#   if i==1 or i==6:
#     print('OOOOOOO')
#   else:
#     print('O     O')
# zad 10
# nb = input("podaj liczbe: ")
# try:
#   b =int(nb)
#   print(b)
# except ValueError:
#     print("To nie jest liczba")