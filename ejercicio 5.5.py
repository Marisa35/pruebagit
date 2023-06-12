
#Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.

x =1
while x < 15:
    n = int(input("Ingrese un numero negativo: "))
    resultado = abs(n)
    print("El numero " , n, "en positivo es: ", resultado)
x += 1
