
#realice un programa que cambie pesos a dolares. Mejorelo, añadiendo el cambio de dolares a pesos y que sea el usuario
#quien decida que tipo de cambio quiere, si de dolares a pesos o viceversa

tipo_camb = input("¿Qué tipo de cambio desea realizar? (1 para pesos a dólares, 2 para dólares a pesos): ")

cant_moneda = float(input("Ingrese la cantidad : "))


if tipo_camb == "1":
    resultado = cant_moneda / 245.0
    print (cant_moneda, "dolares son", resultado, "dolares" )
    
else:
    tipo_camb == "2"
    resultado = cant_moneda * 245.0
    print(cant_moneda, "pesos son", resultado, "dólares")
