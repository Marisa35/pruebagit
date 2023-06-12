

#realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago: 
#contado (1): se aplica un descuento del 10% al importe
#tarjeta (2): se aplica un interes del 10%
#debito (3): se aplica un descuento del 5%
#mostar el importe, el descuento o interes y el importe total

importe= float(input("Ingrese el importe del pago: "))
pago= int(input("Ingrese su forma de pago: (1: contado, 2: tarjeta, 3: debito)"))

if pago == 1:
    descuento= importe * 0.1
    total= importe - descuento
    print("El importe es: ", importe)
    print("El descuento es: ", descuento)
    print("El total es: ", total)
elif pago == 2: 
    interes= importe *0.1
    total = importe + interes
    print("El importe es: ", importe)
    print ("El interes aplicado es: ", interes)
    print("El total es: ", total)
elif pago == 3:
    descuento = importe * 0.05
    total = importe - descuento
    print("El importe es: ", importe)
    print("El descuento es: ", descuento)
    print("El total es: ", total)

    
    