import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib.animation import FuncAnimation

''' This script will animate the convolution of any function with
    a gaussian (gaussian blur). Change the function to be convoluted in
    function f1, modify the grid size and step size, as well as the
    width and height of the gaussian in function f2. '''


def f1(grid):
    ''' first function - edit to whatever. '''
    fval = signal.square(grid)
    return fval


def f2(grid, b):
    ''' Second function - Gaussian.
        Modify height and widths.
        Inputs: b = gaussian centre. '''
    a = 0.5  # peak height
    c = 1.0  # peak width
    gaussian = a*np.exp(-((grid-b)**2)/(2*c**2))
    return gaussian


def conv(grid, dt, b):
    ''' Calculates convolution integral of two functions. '''
    conv_signal = []
    for t in grid:
        product = 0
        for tt in grid:
            ft = f1(tt)  # compute convolution integral as a sum
            gt = f2(tt - t, b)
            product += ft*gt*dt  # \int f(lambda)g(lambda-t) d lambda
        conv_signal.append(product)
    return np.array(conv_signal)


def animate(i, x, y2, line, line2):
    y = f2(x - dt * i, b=min(x))   # animated gaussian must start
    line2.set_data(x[:i], y2[:i])  # at grid index 0 and not initial centre
    line.set_data(x, y)
    return line, line2


def run_convolution(grid, dt):
    conv_signal = conv(grid, dt, b=0)
    fig = plt.figure()
    ax = plt.axes(xlim=(min(grid), max(grid)), ylim=(0, 5))  # may have to edit ylim
    ft = f1(grid)
    plt.plot(grid, ft, 'r', linestyle='dashed', label='$ f(t)$')
    line, = ax.plot([], [], 'b', lw=2, label='$g(t)$')
    line2, = ax.plot([], [], 'g', lw=2, label='$ \int f(\lambda)g(\lambda-t)d\lambda$')

    anim = FuncAnimation(fig, animate, fargs=[grid, conv_signal, line, line2],
                         frames=len(grid), interval=len(grid)*2, blit=True)

    plt.legend()
    plt.xlabel('t')
    plt.ylabel('Magnitude')
    plt.title('Convolution Demo')
    plt.show()


if __name__ == "__main__":
    dt = 0.25  # step in grid
    grid = np.arange(-10, 10, dt)  # grid - modify
    run_convolution(grid, dt)
