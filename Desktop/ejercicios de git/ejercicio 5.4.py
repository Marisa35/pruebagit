
#Leer 10 números y mostrar solamente los números positivos, y su sumatoria.

num = []

for i in range(10):
    print("Ingrese el número: ")
    num.append(int(input())) #ingrese a una lista una debajo de la otra

sumatoria = 0
for n in num:
    if n > 0:
        print(n)
        sumatoria += n

print("La sumatoria de los números positivos es", sumatoria)