# Solicitar al usuario que ingrese el primer número
num1 = float(input("Ingrese el primer número: "))

# Solicitar al usuario que ingrese el segundo número
num2 = float(input("Ingrese el segundo número: "))

# Verificar si el segundo número es igual a cero (lo cual causaría una división por cero)
if num2 == 0:
    print("¡Error! No se puede dividir por cero.")
else:
    # Realizar la división y mostrar el resultado
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")

pesos=float(input("ingrese la cantidad de pesos que quiere convertir"))
eleccion=int(input("ingrese la moneda de cambio: 1. dolar, 2: euros, 3: reales: "))
if eleccion==1:
    pass
elif eleccion==2:
    pass
else:
    pass
precio_dolar = 700  # Precio fijo del dólar en pesos
precio_euro = 800  # Precio fijo del euro en pesos
precio_real = 600  # Precio fijo del real en pesos

pesos = float(input("Ingrese la cantidad de pesos que quiere convertir: "))
eleccion = int(input("Ingrese la moneda de cambio: 1. Dólar, 2. Euro, 3. Real: "))

if eleccion == 1:
    dolares = pesos / precio_dolar
    print(f"{pesos} pesos equivale a {dolares} dólares")
elif eleccion == 2:
    euros = pesos / precio_euro
    print(f"{pesos} pesos equivale a {euros} euros")
elif eleccion == 3:
    reales = pesos / precio_real
    print(f"{pesos} pesos equivale a {reales} reales")
else:
    print("Opción no válida. Por favor, seleccione una moneda válida.")

edad=int(input("Ingrese la edad del cliente: "))

    if edad<5:
        print("El cliente debe ser mayor a 5 años. No puede ingresar")
    elif edad>=5 and edad<14:
        descuento=Entrada_general*0.35
        print("El descuento es del 35% igual a: "+str(descuento))
        Entrada=Entrada_general-descuento
        print("El valor de la entrada es de: " + str(Entrada))

    elif edad>=15 and edad<24:
        descuento=Entrada_general*0.25
        print("El descuento es del 25% igual a: "+str