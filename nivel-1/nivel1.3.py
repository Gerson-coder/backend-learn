"""
 Intercambio de variables: tenés a = 5 y b = 10. Intercambialos sin usar una tercera variable.(Pista: Python tiene
  una forma elegante de hacerlo).

"""

a = 5
b = 10
temp = a
a = b
b = temp

print (a)
print (b)

# forma hacerlo con tuplas

a = 5
b = 10
a,b = b,a

print(a)
print(b)