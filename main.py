
while True:

    print("ingrese que escala de temperatura desea usar:")
    print("-Celsius")
    print("-Fahrenheit")
    print("-Kelvin")

    tipo = input()

    print("Ingrese la temperatura:")

    temperatura = float(input())

    print("conversiones de temperatura a las diferentes escalas:")


    if(tipo == "celsius" or tipo == "Celsius"):

        print("Celsius:")
        print(temperatura)

        print("Fahrenheit:")
        print((1.8 * temperatura) + 32)

        print("Kelvin:")
        print(temperatura + 273.15)


    if(tipo == "fahrenheit" or tipo == "Fahrenheit"):

        print("Celsius:")
        print((temperatura - 32)/1.8)

        print("Fahrenheit:")
        (temperatura)

        print("Kelvin:")
        ((temperatura-32)*5/9 + 273.15)

    if(tipo == "kelvin" or tipo == "Kelvin"):

        print("Celsius:")
        print(temperatura - 273.15)

        print("Fahrenheit:")
        print(temperatura * 1.8 - 459.67)

        print("Kelvin:")
        print(temperatura)


    print("¿Desea repetir el programa, si o no?")
    bucle = input()

    if(bucle != "si"):
        break

print("¡programa finalizado!")


