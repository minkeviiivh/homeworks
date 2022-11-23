import math
coordinate_x1 = float(input("Введите координату х: "))
coordinate_y1 = float(input("Введите координату y: "))
coordinate_x2 = float(input("Введите координату х1: "))
coordinate_y2 = float(input("Введите координату y1: "))
result = math.sqrt((coordinate_x2-coordinate_x1)**2+(coordinate_y2-coordinate_y1)**2)
print('Расстояние мужду точками:','{:.2f}'.format(result))