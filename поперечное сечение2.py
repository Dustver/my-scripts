""" 
Нахождение поперечного сечения
исходя из диаметра.
Нахождение диаметра из сечения.
"""
from math import pi, sqrt

def transverse_section(d):
    r = d / 2
    ts = pi * r ** 2
    return ts
    
def diametr(s):
    d = 2 * sqrt(s / pi)
    return d
    
d,s = 0,0
while True:
    sel1 = int(input("Введите, что вы хотите вычислить:\n\
1)диаметр исходя из сечения\n\
2)сечение исходя из диаметра\n> "))
    if sel1 == 1:
        while True:
            s = input("Введите величину сечения(мм): ")
            if s.isdigit():
                s = int(s)
                break
        print(diametr(s))
        break
    elif sel1 == 2:
        while True:
            d = input("Введите диаметр(мм): ")
            if d.isdigit():
                d = int(d)
                break
        print(transverse_section(d))
        break
    else:
        print ("Ошибка ввода. Попробуйте ещё раз.")