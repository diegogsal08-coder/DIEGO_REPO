a = int(input("dame un primer numero entero: "))
b = int(input("dame un segundo numero entero: "))
if a <= b:
    menor = a
    mayor = b
else:
    menor = b
    mayor = a
suma = 0
for i in range(menor, mayor + 1, 1):
    if i % 2 != 0:
        suma = suma + i
print("la suma de los menores impares entre los menores imapres que me diste son" + str(suma))