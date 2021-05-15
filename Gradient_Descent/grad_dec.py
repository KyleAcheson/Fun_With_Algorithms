import numpy as np

# Single variable problem - just alter target function 'func'

def func(x):  # Edit
    return (x+2)**2 +3*x


def grad(f_x, x0, dr):
    xp = x0+dr
    xn = x0-dr
    yp = func(xp)
    yn = func(xn)
    g = (yp-yn)/(2*dr)  # Central point finite difference
    return g


def run():
    init_guess = 20
    max_iter = 100
    dr = 0.1
    thresh = 0.0001
    func_val = func(init_guess)
    x_n = init_guess
    print('INIT: x=%s, f(x)=%s' % (x_n, func_val))
    gradient = grad(func, x_n, dr)
    n_iter = 0
    while max_iter > 0 and gradient > thresh:
        n_iter += 1
        max_iter -= 1
        gradient = grad(func, x_n, dr)
        x_n = x_n-(dr*gradient)
        func_val = func(x_n)
        print('>%s : x=%s, f(x)=%s, grad=%s' % (n_iter, x_n, func_val, gradient))

run()
