# %%
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
class E(B, C): pass

# 1. Ромб + еще один родитель
class F(D, E): pass  

# 2. Еще более хитрый порядок
class G(E, D): pass  

# %%
print("MRO для F:", [c.__name__ for c in F.__mro__])
print("MRO для G:", [c.__name__ for c in G.__mro__])