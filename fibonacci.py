def fibonacci(n):
    a, b = 0, 1
    resultado = []

    for _ in range(n):
        resultado.append(a)
        a, b = b, a + b

    return resultado


n = int(input("¿Cuántos términos quieres?: "))
print(fibonacci(n))