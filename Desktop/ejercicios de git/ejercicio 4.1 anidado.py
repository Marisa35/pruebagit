

#Introducir los lados de un triangulo y visualizar por pantalla si dicho triangulo es equilatero, isosceles
#o escaleno

lado_a= float(input("Ingrese el lado 1 del triangulo:  "))
lado_b= float(input("Ingrese el lado 2 del triangulo:  "))
lado_c= float(input("Ingrese el lado 3 del triangulo:  "))

if lado_a == lado_b == lado_c:
    print("Es un triangulo equilatero")
elif lado_a == lado_b != lado_c:
    print("El triangulo es un Isosceles")
else:
    print("Es un Escaleno")