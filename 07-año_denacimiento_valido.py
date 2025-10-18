from datetime import dato

año = int(input("Ingrese su año de nacimiento: "))
año_actual = dato.now().year

if año > 1900 and año < año_actual:
    print(f"El año {año} es un año de nacimiento válido.")
else:
    print(f"El año {año} no es válido.")