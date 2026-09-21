x = float(input("Dame el monto a pagar: "))
if x >= 15000:
    x = x * 0.75
else:
    if x >= 7000:
        x = x * 0.85
    else:
        if x >= 1000:
            x = x * 0.9
        else:
            if x >= 500:
                x = x * 0.95
    print("El total a pagar es:$" + str(x))
