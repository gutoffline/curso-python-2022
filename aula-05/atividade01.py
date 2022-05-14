"""
Operadores Lógicos

not --> não 
or --> ou 
and --> e 

"""

# not --> negação, se um resultado é true ele transforma em false=, se for false ele transforma em true

print('====NOT====')
print(10>5)
print(not 10>5)
print(10<5)
print(not 10<5)

# and --> e , todos os resultados devem ser true para a operação retornar true. se um resultado for false, o retorno da operação será false

print("\n\n")
print("====AND====")
print(10>3)
print(100>10)
print(10>3 and 100>10)
print("---------")
print(10==3 and 100>10)
print(10>3 and 100 > 10 and 50==3)

# or --> ou, apenas um resultado precisa ser true para a expressão retornar true. Para retornar false todas as expressões devem ser false
print("\n\n")
print("====OR====")
print(10 > 3 or 15 == 10) #true
print(10 > 15 or 20 < 10) #false


