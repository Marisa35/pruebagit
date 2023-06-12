
#Leer 10 números y obtener la cantidad de mayores y la cantidad de
#menores a 100, cuál es el número máximo y cuál es el número mínimo.

numeros = []
mayores = []
menores = []

for i in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
    if numero > 100:
        mayores.append(numero)
    else:
        menores.append(numero)

print("Cantidad de números mayores a 100:", len(mayores))
print("Cantidad de números menores o iguales a 100:", len(menores))
print("Número máximo:", max(numeros))
print("Número mínimo:", min(numeros))