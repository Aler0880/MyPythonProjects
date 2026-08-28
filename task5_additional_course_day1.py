# %%
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass  # Рабочий ромб


class E(C, B):
    pass  # Раскомментируйте эту строку — и получите ошибку!


# %%
print("MRO для D (рабочий):", [c.__name__ for c in D.__mro__])
# Попробуйте поменять местами B и C в определении D и посмотрите, как изменится порядок
# %%
