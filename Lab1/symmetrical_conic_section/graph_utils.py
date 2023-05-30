from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple


# def draw_implicit_function_2d(function, x_range: Tuple[float, float], y_range: Tuple[float, float]):
#     x, y = var('x y')
#     plot_implicit(Eq(function(x, y)), points=1000)


def draw_implicit_function_2d(function, x_range: Tuple[float, float], y_range: Tuple[float, float]):
    delta = 0.003
    xrange = np.arange(x_range[0], x_range[1], delta)
    yrange = np.arange(y_range[0], y_range[1], delta)
    X, Y = np.meshgrid(xrange, yrange)

    # Axis settings
    plt.axis([x_range[0], x_range[1], y_range[0], y_range[1]])
    plt.gca().set_aspect('equal', adjustable='box')

    # drawing
    n_dim_1 = len(X)
    n_dim_2 = len(X[0])

    Z = np.zeros([n_dim_1, n_dim_2])
    for i_dim_1 in range(n_dim_1):
        for i_dim_2 in range(n_dim_2):
            Z[i_dim_1][i_dim_2] = function(X[i_dim_1][i_dim_2], Y[i_dim_1][i_dim_2])

    plt.contour(X, Y, Z, [0])
    #plt.contour(X, Y, Y, [0])
    plt.show()