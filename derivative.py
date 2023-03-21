def derivative(func, x):
    epsilon = 0.000000001
    return (func(x) + func(x + epsilon)) / 2
