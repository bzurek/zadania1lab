import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


wiek = pd.ExcelFile('imiona.xlsx')
wykres = pd.read_excel(wiek, header=0)
lindzieci = wykres.groupby(['Rok']).agg({'Liczba': ['sum']})
print(lindzieci)
lindzieci.plot()
plt.xticks(np.arange(2000, 2018, step=1))
plt.xticks(rotation=100)
plt.show()
slupdzieci = wykres.groupby(['Plec']).agg({'Liczba': ['sum']})
slupdzieci.plot.bar()
plt.show()
print(slupdzieci)