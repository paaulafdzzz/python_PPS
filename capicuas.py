def es_capicua(numero):
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

def generar_capicuas(inicio, fin):
    capicuas = []
    for num in range(inicio, fin + 1):
        if es_capicua(num):
            capicuas.append(num)
    return capicuas

numero = int(input("Ingrese un número: "))

if es_capicua(numero):
    print(f"El número {numero} es capicúa.")
else:
    print(f"El número {numero} no es capicúa.")

inicio = int(input("Ingrese el número inicial del rango: "))
fin = int(input("Ingrese el número final del rango: "))

capicuas_en_rango = generar_capicuas(inicio, fin)
print(f"Números capicúas entre {inicio} y {fin}: {capicuas_en_rango}")

