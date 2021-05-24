# lê uma string com três partes
import math
a, b, c = input().split()

# converte strings em números
a = float(a)
b = float(b)
c = float(c)

# termine esse programa aqui...
if abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b:

	if a**2+b**2 == c**2 or a**2+c**2 == b**2 or b**2+c**2 == a**2:
	    print("retângulo")
	elif a**2+b**2<c**2 or a**2+c**2<b**2 or b**2+c**2<a**2:
	    print("obtusângulo")
	elif a**2+b**2>c**2 or a**2+c**2>b**2 or b**2+c**2>a**2:
	    print("acutângulo")
else:
	print("não forma triângulo")