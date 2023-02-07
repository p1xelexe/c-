def f(x):
    return x**4 + 3*x - 5

def binary_search(a, b):
    while abs(b - a) > 0.0001:
        mid = (a + b) / 2
        if f(mid) > 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2

a = 0
b = 100
x = binary_search(a, b)
print(x)#решение
