import numpy as np

# Ваши данные
X = np.array([100, 100, 300, 500, 500, 500, 300, 300, 300, 600, 100], dtype=float)
Y = np.array([10, 500, 200, 12, 500, 200, 300, 10, 500, 200, 200], dtype=float)
Z = np.array(
    [2462, 2163, 2153, 2835, 2319, 2210, 2255, 2790, 2350, 2347, 2165], dtype=float
)

N = len(X)
points = np.column_stack((X, Y))


# Функция phi(r) = r^2 * ln(r)
def phi(r):
    return np.where(r == 0, 0.0, r**2 * np.log(r))


# Матрица K (N x N)
K = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        r = np.linalg.norm(points[i] - points[j])
        K[i, j] = phi(r)

# Матрица P (N x 3): [1, X, Y]
P = np.column_stack((np.ones(N), X, Y))

# Собираем блочную матрицу (N+3)x(N+3)
A = np.zeros((N + 3, N + 3))
A[:N, :N] = K
A[:N, N:] = P
A[N:, :N] = P.T
# правый нижний блок 3x3 остаётся нулевым

# Правая часть: Z и три нуля
b = np.concatenate([Z, np.zeros(3)])

# Решаем систему
sol = np.linalg.solve(A, b)

w = sol[:N]  # веса w_i
a0, a1, a2 = sol[N:]  # полиномиальные коэффициенты

print("a0 =", a0)
print("a1 =", a1)
print("a2 =", a2)
print("w =", w)
