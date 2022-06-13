class MinhaClasse:
  n = 10

meuObjeto1 = MinhaClasse()
print(meuObjeto1.n)

meuObjeto2 = MinhaClasse()
print(meuObjeto2.n)

meuObjeto2.n = 5
print(meuObjeto2.n)
print(meuObjeto1.n)

del meuObjeto1
print(meuObjeto1.n)