import numpy as np
import matplotlib.pyplot as plt

# Fungsi penyelesaian dengan metode Bagi Dua
def my_bisection(f, a, b, e, max_iter=1000):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    m = (a + b) / 2
    if np.abs(f(m)) < e:
        return m
    elif max_iter == 0:
        raise Exception('Maksimum iterasi tercapai')
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, e, max_iter-1)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, e, max_iter-1)

# No. 1a: f(x) = x^3 - 2x + 1
f1 = lambda x: x**3 - 2*x + 1
r1 = my_bisection(f1, -2, 2, 0.001)
print("r1 =", r1)
print("f(r1) =", f1(r1))

# No. 1b: f(x) = e^x - x
f2 = lambda x: np.exp(x) - x
r2 = my_bisection(f2, -1, 1, 0.001)
print("r2 =", r2)
print("f(r2) =", f2(r2))

# Modifikasi 2.1: Program berhenti setelah n iterasi
def my_bisection_max_iter(f, a, b, e, max_iter=1000):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    m = (a + b) / 2
    if np.abs(f(m)) < e or max_iter == 0:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection_max_iter(f, m, b, e, max_iter-1)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection_max_iter(f, a, m, e, max_iter-1)

# Modifikasi 2.2: User dapat menginputkan fungsi, batas, dan galat
def user_input_bisection():
    f_input = input("Masukkan fungsi (gunakan x sebagai variabel): ")
    a = float(input("Masukkan batas a: "))
    b = float(input("Masukkan batas b: "))
    e = float(input("Masukkan galat (e): "))
    result = my_bisection_max_iter(lambda x: eval(f_input), a, b, e)
    print("Hasil akar:", result)

# Modifikasi 2.3: Akar ditampilkan dalam grafik
def plot_function(f, a, b, root=None):
    x = np.linspace(a, b, 100)
    y = f(x)
    plt.plot(x, y, label='f(x)')
    if root is not None:
        plt.plot(root, f(root), 'ro', label='Root')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()

# Gabungkan semua modifikasi
user_input_bisection()