import numpy as np

def my_bisection(f, a, b, e):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    m = (a + b)/2
    if np.abs(f(m)) < e:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, e)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, e)

f2 = lambda x: np.exp(x) - x

r2 = my_bisection(f2, -1, 1, 0.001)
print("r2 =", r2)
print("f(r2) =", f2(r2))