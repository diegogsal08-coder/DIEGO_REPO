x = int(input("Dame un numero entero positivo: "))
suma = 0
i = 1
while i <= x:
    if x % i == 0:
        suma = suma + i
    i = i + 1
print("La suma es: " + str(suma))
