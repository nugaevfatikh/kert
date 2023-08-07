import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def exponential_func(x, a, b):
    return a * np.exp(b * x)

def fit_exponential(x, y):
    popt, pcov = curve_fit(exponential_func, x, y)
    return popt


# Задаем значения n и h
n = 10
h = 1/n

# Создаем массивы для x и y
x = np.arange(0, n+1) * h
y = 1 - np.cos(x)

# Аппроксимируем функцию E(x) к данным (x, y)
popt = fit_exponential(x, y)
a, b = popt

# Создаем массив точек для аппроксимированной функции
x_fit = np.linspace(0, 1, 100)
y_fit = exponential_func(x_fit, a, b)

# Выводим графики для данных и аппроксимированной функции
plt.plot(x, y, 'o', label='Data')
plt.plot(x_fit, y_fit, label='Exponential fit')
plt.legend()
plt.show()
