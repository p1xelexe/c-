def newton_raphson(x0, f, df, epsilon):
    x = x0
    while abs(f(x)) > epsilon:
        x = x - f(x) / df(x)
    return x

def f(x):
    return x**4 + 3*x - 5

def df(x):
    return 4*x**3 + 3

x0 = 1.0
epsilon = 0.0001

x = newton_raphson(x0, f, df, epsilon)
print("The solution is:", x)
