

#Realice un programa que lea 4 números y diga cuántos son pares y
#cuantos impares y devuelva la sumatoria de los pares.

n = 1
par = impar = 0
suma_pares = 0

for i in range(4):
    n = int(input("Ingrese un número: "))
    if n >0:
        if n % 2 == 0:
            par += 1
            suma_pares += n
        else:
            impar += 1

print("Cantidad de números pares:", par)
print("Cantidad de numeros impares: ", impar)
print ("Cantidad total de pares: ", suma_pares)


