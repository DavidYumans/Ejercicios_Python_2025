print("Bienvenido")
numero1 = float(input("Ingrese el primer Número: "))
numero2 = float(input("Ingrese el segundo Número: "))
numero3 = float(input("Ingrese el tercer Número: "))

if numero1 > numero2 and numero1 >= numero3:
    print("El Número Mayor es: ")
    print(numero1)
elif numero2 > numero1 and numero2 >= numero3:
    print("El Número Mayor es: ")
    print(numero2)
else: 
     print("El Número Mayor es: ")
     print(numero3)