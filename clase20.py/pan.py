import pandas as pd
from pandas.core import frame 

serie_1 = pd.Series([5,8,9])
serie_2 = pd.Series({10:50, 20:80, 30:40})
serie_2 = pd.Series({'10':50, '20':80, '30':40})

frame_1 = pd.DataFrame({10:[15, 34, 15],20:[24,36,20],30:[28,32,19]})
frame_2 = pd.DataFrame([[15, 34, 15],[24,36,20],[28,32,19]],columns=[10,'hola',30])

print(frame_1)
print(frame_2)

devs = [{'cc': 1540, 'nombre': 'Miguel', 'salario': 2600000,'years':5},
        {'cc': 1556, 'nombre': 'Cristian', 'salario': 2500000,'years':2},
        {'cc': 2556, 'nombre': 'Juan Ignacio', 'salario': 2500000,'years':3},
        {'cc': 1340, 'nombre': 'Nicolas', 'salario': 2400000,'years':4},
        {'cc': 1526, 'nombre': 'Sendy', 'salario': 2400000,'years':5},
        {'cc': 2516, 'nombre': 'Santiago', 'salario': 2600000,'years':5},
        {'cc': 1547, 'nombre': 'David', 'salario': 2500000,'years':3},
        {'cc': 5556, 'nombre': 'Milton', 'salario': 2800000,'years':6},
        {'cc': 5586, 'nombre': 'Jinneth', 'salario': 2800000,'years':2},
        {'cc': 3556, 'nombre': 'Alejandro', 'salario': 2700000,'years':1}] 