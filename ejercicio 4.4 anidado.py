
#confeccione un programa que pida un numero del 1 al 7 y diga el dia de la semana que corresponde

num= int(input("Ingrese un numero del 1 al 7: "))

if num == 1:
    print("El dia de la semana es Lunes")
elif num == 2:
    print("El dia de la semana es Martes")
elif num == 3:
    print("El dia de la semana es Miercoles")
elif num == 4:
    print("El dia de la semana es Jueves")
elif num == 5:
    print("El dia de la semana es Viernes")
elif num == 6:
    print("El dia de la semana es Sabado")
elif num == 7:
    print("El dia de la semana es Domingo")
else:
    print("No ingreso el numero correspondiente")