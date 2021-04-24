import numpy as np
import math
# zad 1
# a = np.arange(3)
# b = np.array([3, 4, 5])
# print(a * b)
# zad 2
# a = np.arange(9).reshape(3, 3)
# b = np.arange(16). reshape(4, 4)
# print(a)
# print(b)
# for x in a:
#     liczba = np.amin(x)
#     print(liczba)
# print("")
# for c in b:
#     liczba = np.amin(c)
#     print(liczba)
# cos = a.min(axis=1)
# print(cos)
# cos1 = b.min(axis=0)
# print(cos1)

# zad 3
# a = np.arange(3)
# b = np.array([3, 4, 5])
# print(a)
# print(b)
# print(np.dot(a, b))

# zad 4
# a = np.arange(3, dtype='int32')
# print(a)
# b = np.random.rand(1, 3)
# print(b)
# print(a * b)

# zad5
# mac1 = np.random.rand(6).reshape(2, 3)
# a = np.sin(mac1)
# print(a)

# zad6
# mac2 = np.random.rand(6).reshape(2, 3)
# b = np.cos(mac2)
# print(b)

# zad 7
# c = np.add(a, b)
# print(c)

# zad 8
# mac1 = np.arange(9).reshape(3, 3)
# for line in mac1:
#     print(line)

# zad 9
# mac1 = np.arange(9).reshape(3, 3)
# for el in mac1.flat:
#     print(el)

# zad 10
# mac1 = np.arange(81).reshape(9, 9)
# mac1.reshape(3, 27)
# mac1.reshape(1, 81)
#jezeli podzielimy 81 przez jakas liczbe, to musi wyjsc wynik calkowity. Tylko wtedy istnieje szansa stworzenia macierzy. Wtedy mamy liczbe przez ktora dzielilismy, oraz wynik z tego dzielenia, i to oznacza nasz wymiar

# zad 11
mac = np.arange(12)
print(mac.reshape(3, 4).ravel())
print(mac.reshape(4, 3).ravel())
print(mac.reshape(2, 6).ravel())
# macierze sa takie same.