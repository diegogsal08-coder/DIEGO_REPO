import math
print("Dame el número n1: ")
n1 = float(input())
print("Dame el número n2: ")
n2 = float(input())
print("Dame el número n3: ")
n3 = float(input())
if n1 <= 0 or n2 <= 0 or n3 <= 0:
    print("Alguno o varios de los números no son positivos")
else:
    s1 = math.trunc(n1) + round((n1 - math.trunc(n1)) * 10000)
    s2 = math.trunc(n2) + round((n2 - math.trunc(n2)) * 10000)
    s3 = math.trunc(n3) + round((n3 - math.trunc(n3)) * 10000)
    print("La suma resultante de n1 = " + str(s1))
    print("La suma resultante de n2 = " + str(s2))
    print("La suma resultante de n3 = " + str(s3))
    mayor = max(max(s1, s2), s3)
    print("El valor mayor de las sumas es " + str(mayor))