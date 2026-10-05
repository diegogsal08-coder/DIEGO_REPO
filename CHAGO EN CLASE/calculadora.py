import math


def formatear_resultado(valor):
    """Devuelve un número con formato legible para consola."""
    if isinstance(valor, float) and valor.is_integer():
        return str(int(valor))
    return str(valor)


def calculadora():
    """Calculadora científica de consola."""
    print("Calculadora científica.")
    print("Operaciones disponibles: +, -, *, /, ^, %, sin, cos, tan, asin, acos, atan, sqrt, log, ln, exp, pow.")
    print("Escribe 'salir' para terminar o 'ayuda' para ver ejemplos.")

    while True:
        entrada = input("Operación: ").strip().lower()
        if entrada in ("salir", "exit", "quit"):
            print("Hasta luego.")
            break

        if entrada in ("ayuda", "help", "?"):
            print("Ejemplos:")
            print("  8 + 2")
            print("  2 ^ 5")
            print("  sin 30")
            print("  cos 60")
            print("  sqrt 16")
            print("  log 100")
            print("  ln 2.7182818")
            print("  pow 2 8")
            continue

        entrada = entrada.replace("×", " * ").replace("÷", " / ")
        entrada = entrada.replace("^", " ^ ")
        entrada = entrada.replace("(", " ").replace(")", " ")
        partes = entrada.split()

        if not partes:
            continue

        try:
            if len(partes) == 2 and partes[0] in {"sin", "cos", "tan", "asin", "acos", "atan", "sqrt", "log", "ln", "exp", "abs"}:
                a = float(partes[1])
                operador = partes[0]
                if operador == "sin":
                    resultado = math.sin(math.radians(a))
                elif operador == "cos":
                    resultado = math.cos(math.radians(a))
                elif operador == "tan":
                    resultado = math.tan(math.radians(a))
                elif operador == "asin":
                    resultado = math.degrees(math.asin(a))
                elif operador == "acos":
                    resultado = math.degrees(math.acos(a))
                elif operador == "atan":
                    resultado = math.degrees(math.atan(a))
                elif operador == "sqrt":
                    if a < 0:
                        print("La raíz cuadrada de un número negativo no está definida en los reales.")
                        continue
                    resultado = math.sqrt(a)
                elif operador == "log":
                    if a <= 0:
                        print("El logaritmo solo está definido para números positivos.")
                        continue
                    resultado = math.log10(a)
                elif operador == "ln":
                    if a <= 0:
                        print("El logaritmo natural solo está definido para números positivos.")
                        continue
                    resultado = math.log(a)
                elif operador == "exp":
                    resultado = math.exp(a)
                elif operador == "abs":
                    resultado = abs(a)

            elif len(partes) == 3 and partes[0] in {"pow"}:
                operador = partes[0]
                a = float(partes[1])
                b = float(partes[2])
                if operador == "pow":
                    resultado = a ** b

            elif len(partes) == 3:
                a = float(partes[0])
                operador = partes[1]
                b = float(partes[2])

                if operador == "+":
                    resultado = a + b
                elif operador == "-":
                    resultado = a - b
                elif operador == "*":
                    resultado = a * b
                elif operador == "/":
                    if b == 0:
                        print("No se puede dividir entre cero.")
                        continue
                    resultado = a / b
                elif operador == "%":
                    resultado = a % b
                elif operador == "^":
                    resultado = a ** b
                else:
                    print("Operador no válido. Usa +, -, *, /, %, ^ o funciones científicas.")
                    continue

            else:
                print("Formato no válido. Ejemplo: 8 + 2, sin 30, sqrt 16, pow 2 8")
                continue

        except ValueError:
            print("Introduce números válidos.")
            continue

        print(f"Resultado: {formatear_resultado(resultado)}")


if __name__ == "__main__":
    calculadora()