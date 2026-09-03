class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2D (x = {self.x}, y = {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)

    def distance(self, vec1, vec2):
        vec1 = Vector2D(x1, y1)
        self.vec1 = Vector2D(v.x, vec1.y)
        self.vec2 = Vector2D(vec2.x, vec2.y)

        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


v1 = Vector2D(3, 4)
v2 = Vector2D(5, 7)
v3 = v1 + v2
v4 = v2 - v1
v5 = v1 * 2
v6 = 2 * v1

print(v1, "+", v2, "=", v3)
print(v2, "-", v1, "=", v4)
print(v1, "*", 2, "=", v5)
print(2, "*", v1, "=", v6)
print(v1 == v2)
print(v5 == v6)
print(len(v1))
print()
print(repr(v1), repr(v2), repr(v3), sep="\n")
