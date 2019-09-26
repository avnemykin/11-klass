# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 10000)                                  # от -5 до 2 сделать 100 точек
y1 = x**3-np.cos(x)                                                 # y1 - объявление функции


fig, ax = plt.subplots()                                            # будет 1 график, на нем:
ax.plot(x, y1, color="blue", label="x^3-cos(x)")      # функция y1(x), синий, надпись y(x)

ax.plot([-2,2],[0,0], color='green')                            # псевод ось X

ax.plot([0,0],[-8,8], color='green')                            # псевод ось Y

plt.text(2, -1, 'X', fontsize=12)                                 # подпись оси X

plt.text(-0.1, 8, 'Y', fontsize=12)                              # подпись оси Y

ax.legend()                                                             # показывать легенду

plt.show()                                                                # показать рисунок

