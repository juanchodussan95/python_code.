trupilantes = ['sergio','david','eider','lina']

trupilantes_dict = {tripulante : '5' for tripulante in trupilantes }
trupilantes_dict = dict.fromkeys(trupilantes, 5)
trupilantes_dict = dict(zip(trupilantes, range(0,len(trupilantes))))

print(trupilantes_dict)