import numpy as np
import scipy
from scipy.interpolate import RBFInterpolator

X = np.array([100, 100, 300, 500, 500, 500, 300, 300, 300, 600, 100], dtype=float)
Y = np.array([10, 500, 200, 12, 500, 200, 300, 10, 500, 200, 200], dtype=float)
Z = np.array([2462, 2163, 2153, 2835, 2319, 2210, 2255, 2790, 2350, 2347, 2165], dtype=float)

points = np.column_stack((X, Y))

# thin_plate_spline — хорошо работает для гладких поверхностей
# smoothing=0 — точная интерполяция (ошибка в точках = 0)
rbf = RBFInterpolator(points, Z, kernel='thin_plate_spline', smoothing=0)

# Проверка ошибок в известных точках
Z_pred = rbf(points)
print("Макс. ошибка в известных точках:", np.max(np.abs(Z - Z_pred)))

# Предсказание в новой точке внутри области
new_pt = np.array([[400, 300]])
print("Предсказание в (400, 300):", rbf(new_pt)[0])
