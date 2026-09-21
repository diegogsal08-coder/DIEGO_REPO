x = float(input("teclee argumento x:"))
if x <= -1 or x >= 1:
    print("X fuera de rango")
else:
    print("hasta cuantos terminos de la serie?")
    n = int(input())
    suma = 0
    for i in range(1, n + 1, 1):
        termino = -1 * i - 1 / i * x * i
        suma = suma + termino
    print("in(1+x):" + str(suma))