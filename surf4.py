import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RBFInterpolator

# Ваши данные
X = np.array([100, 100, 300, 500, 500, 500, 300, 300, 300, 600, 100], dtype=float)
Y = np.array([10, 500, 200, 12, 500, 200, 300, 10, 500, 200, 200], dtype=float)
Z = np.array([2462, 2163, 2153, 2835, 2319, 2210, 2255, 2790, 2350, 2347, 2165], dtype=float)

points = np.column_stack((X, Y))

# Интерполятор thin plate spline (точное прохождение через точки)
rbf = RBFInterpolator(points, Z, kernel='thin_plate_spline', smoothing=0)

# Сетка для поверхности
x_grid = np.linspace(X.min(), X.max(), 60)
y_grid = np.linspace(Y.min(), Y.max(), 60)
Xg, Yg = np.meshgrid(x_grid, y_grid)
grid_points = np.column_stack((Xg.ravel(), Yg.ravel()))
Zg = rbf(grid_points).reshape(Xg.shape)

# Построение графика
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Поверхность
surf = ax.plot_surface(Xg, Yg, Zg, cmap='viridis', alpha=0.8,
                       linewidth=0, antialiased=True, edgecolor='none')

# Исходные точки
ax.scatter(X, Y, Z, color='red', s=60, depthshade=False, label='Исходные точки')

# Настройки осей
ax.set_xlabel('X (Проток)')
ax.set_ylabel('Y (Давление)')
ax.set_zlabel('Z')
ax.set_title('Поверхность Z(X,Y) и исходные точки')

# Цветовая шкала
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Z')

# Легенда
ax.legend()

plt.tight_layout()
plt.show()
