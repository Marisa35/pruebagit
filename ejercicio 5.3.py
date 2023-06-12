
#Ingresar las edades y el sexo de 15 personas y determinar cuántas son
#mujeres, cuántos varones, cuántos mayores de edad y cuántos
#menores de edad.

c_mujeres = 0
c_varones = 0
c_mayores = 0
c_menores = 0

for i in range(15):
    print("Ingrese la edad de la persona: "  )
    edad = int(input())
    print("Ingrese el sexo de la persona:", "(M/F)")
    sexo = input()

    if sexo == "F":
        c_mujeres += 1
    else:
        c_varones += 1

    if edad >= 18:
        c_mayores += 1
    else:
        c_menores += 1

print("Hay", c_mujeres, "mujeres y", c_varones, "varones.")
print("Hay", c_mayores, "personas mayores de edad y", c_menores, "personas menores de edad.")
