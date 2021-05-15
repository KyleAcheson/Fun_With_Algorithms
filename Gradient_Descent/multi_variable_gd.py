import numpy as np
import matplotlib.pyplot as plt

# Needs some work still - strange convergence behaviour

def target_function(x):
    y = (x[0]**2 + x[1]**2)
    return y


def displace(n_vars, x0, dr):
    x_new = []
    for i, var in enumerate(range(1, n_vars**2, n_vars)):
        x_pos = x0[i]+dr
        x_new.extend([x0[i], x_pos])
    return x_new


def target_gradient(func, x0, dr):
    f_vals, grads = [], []
    n_vars = len(x0)
    f0_val = target_function(x0)
    x_new = displace(n_vars, x0, dr)
    c = 0
    for i in range(n_vars, n_vars**2 + n_vars, n_vars):
        x = x_new[c: i]
        print(x)
        f = target_function(x)
        f_vals.append(f)
        c += n_vars
    for i in range(n_vars):
        grad = (f_vals[i] - f0_val)/dr
        grads.append(grad)
    return grads


def gradient_descent(x0, thresh, dr, max_iter):
    x_vals = [[] for x in range(len(x0))]
    f_vals = target_function(x0)
    grads = target_gradient(target_function, x0, dr)
    print('> STARTING POINT - x = %s, f(x) = %s, grads = %s' % (x0, f_vals, grads))
    n_iter = 0
    while max_iter > 0 :
        n_iter += 1
        max_iter -= 1
        grads = target_gradient(target_function, x0, dr)
        for i in range(len(grads)):
            x0[i] = x0[i] - (dr*grads[i])
            x_vals[i].append(x0[i])
            f_vals = target_function(x0)
        print('> ITER %s - x = %s, f(x) = %s, grads = %s' %(n_iter, x0, f_vals, grads))
    return x_vals


def plot_function(x0):
    fig = plt.figure()
    XY = []
    x = np.linspace(-20, 20, 40)
    y = np.linspace(-20, 20, 40)
    [X, Y] = np.meshgrid(x, y)
    XY.append(X)
    XY.append(Y)
    f_vals = target_function(XY)
    levels = np.arange(np.amin(f_vals), np.amax(f_vals), 2)
    cp = plt.contourf(X, Y, f_vals, levels=levels)
    plt.plot(x0[0], x0[1], 'r+')
    plt.colorbar(cp)
    plt.show()


if __name__ == "__main__":
    x0 = [7, 3]
    thresh = 0.0001
    dr = 0.05
    max_iter = 100
    x_vals = gradient_descent(x0, thresh, dr, max_iter)
    plot_function(x_vals)
