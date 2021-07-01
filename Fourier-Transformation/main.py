import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
import statistics
import cmath

points = 30000
res = 10000

x = []
y = []
f = []
dist = []

freq = 3

f1 = 3
w1 = 2 * math.pi * f1


def make_signal():
    for t in range(points):
        y.append(math.cos(w1 * t / res) + 1)


def make_complex_signal(freqence):
    for t in range(points):
        exponent = complex(-2 * cmath.pi * freqence * t / res * complex(0, 1))
        base = complex(math.cos(w1 * t / res) + 1)
        complex_number = base * cmath.exp(exponent)
        f.append(complex_number)


def create_x_axis(size):
    for j in range(size):
        x.append(j/res)


def plot_graph(x_val, y_val):
    plt.plot(x_val, y_val)
    plt.show()
    x_plot = [x_v.real for x_v in f]
    y_plot = [y_v.imag for y_v in f]
    plt.plot(x_plot, y_plot)
    plt.show()


def complex_abs():
    for frequence in range(20):
        frequence = frequence * res
        f.clear()
        for u in range(points):
            exponent = complex(-2 * cmath.pi * frequence * u / res * complex(0, 1))
            base = complex(math.cos(w1 * u / res) + 1)
            complex_number = base * cmath.exp(exponent)
            f.append(complex_number)

        real_sum = 0
        im_sum = 0
        for val in f:
            real_sum = real_sum + val.real
            im_sum = real_sum + val.imag
        dist.append(cmath.sqrt(pow(real_sum, 2) + pow(im_sum, 2)).real)


def fourier():
    make_signal()
    make_complex_signal(freq)
    create_x_axis(points)
    plot_graph(x, y)
    #print(complex_abs())
    #max_freq = dist.index(max(dist))
    #print(f"Beste Frequenz:  {max_freq}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fourier()
