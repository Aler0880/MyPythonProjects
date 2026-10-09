import numpy as np

# Все 10 точек

# Проток
X = np.array(
    [100.0, 100.0, 300.0, 500.0, 500.0, 500.0, 300.0, 300.0, 300.0, 600.0, 100.0]
)

# Давление
Y = np.array(
    [10.00, 500.0, 200.0, 12.00, 500.0, 200.0, 300.0, 10.00, 500.0, 200.0, 200.0]
)

# Попугаи
Z = np.array(
    [2462.0, 2163.0, 2153, 2835.0, 2319, 2210, 2255.0, 2790, 2350.0, 2347, 2165]
)

# Матрица признаков: [1, X, Y, X^2, Y^2, X*Y]
A = np.column_stack((np.ones(len(X)), X, Y, X**2, Y**2, X * Y))

# Решение МНК
coeffs, residuals, rank, s = np.linalg.lstsq(A, Z, rcond=None)

a, b, c, d, e, f = coeffs
print(f"Z = {a:.4f} + {b:.4f}*X + {c:.4f}*Y + {d:.6f}*X^2 + {e:.6f}*Y^2 + {f:.6f}*X*Y")
print("(Проток, Давление)")

# Предсказанные значения и ошибки
Z_pred = A @ coeffs
for i in range(len(X)):
    print(
        f"({X[i]}, {Y[i]}): {Z[i]-Z_pred[i]:.1f}, факт={Z[i]}, прогноз={Z_pred[i]:.1f}"
    )
