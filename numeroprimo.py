numero = int(input("Ingrese un número: "))

if numero <= 1:
    print(f"{numero} no es un número primo.")
else:
    es_primo = True

    for i in range(2,numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")