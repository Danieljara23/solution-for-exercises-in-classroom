name = input("Ingresa tu nombre: ")
year = int(input("Ingresa tu año de nacimiento: "))

age = 2024 - year
print(f"Hola {name}, tienes {age} años")

if year >= 1930 and year <= 1948:
    print("Eres un niño de la postguerra")
elif year <= 1968: 
    print("Eres un Baby boomer")
elif year <= 1993:
    print("Eres un millenial")
elif year >= 2011:
    print("Eres de la generación Z")