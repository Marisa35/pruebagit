

#realizar un programa que permita ingresar "f" o "m" y determinar si vota en mesa femenina o masculina

sexo = input("Ingrese su sexo (f/m): ")

if sexo == "f":
    print("Usted vota en mesa femenina.")
elif sexo == "m":
    print("Usted vota en mesa masculina.")
else:
    print("Sexo ingresado no válido.")