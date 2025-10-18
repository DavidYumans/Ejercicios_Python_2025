letra = input("Ingrese una letra: ").lower()

if len(letra) == 1 and letra.isalpha():
    if letra in 'aeiou':
        print(f"La letra '{letra}' es una vocal.")
    else:
        print(f"La letra '{letra}' es una consonante.")
else:
    print("Por favor, ingrese solo una letra válida.")