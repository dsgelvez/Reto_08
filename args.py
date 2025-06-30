# Tres funciones usando *args

# Suma de varios números
def suma_numeros(*args) -> int:
    return sum(args)

# Máximo de varios números
def maximo_valor(*args):
    return max(args)

# Mínimo de varios números
def minimo_valor(*args):
    return min(args)


if __name__ == "__main__":
    print("Suma:", suma_numeros(1, 2, 3, 4))
    print("Máximo:", maximo_valor(1, 8, 3, 4))
    print("Mínimo:", minimo_valor(1, 8, 3, 4))
