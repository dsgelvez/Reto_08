# Tres funciones convertidas en lambdas

# Suma de dos números
suma = lambda a, b: a + b

# Mayor de dos números
mayor = lambda a, b: a if a > b else b

# f(x) = x^(x^(1/3)) - 1
funcion_especial = lambda x: x ** (x ** (1/3)) - 1


if __name__ == "__main__":
    print("Suma:", suma(5, 3))
    print("Mayor:", mayor(10, 20))
    print("Función especial:", funcion_especial(4))
