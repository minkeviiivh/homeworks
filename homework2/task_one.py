import math
x1 = float(input("Введите координату х: "))
y1 = float(input("Введите координату y: "))
x2 = float(input("Введите координату х1: "))
y2 = float(input("Введите координату y1: "))
result = math.sqrt((x2-x1)**2+(y2-y1)**2)
print('Расстояние мужду точками:', '{:.2f}'.format(result))
