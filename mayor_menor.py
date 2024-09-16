num1 = int(input("Ingresa un primer número "))
num2 = int(input("Ingresa un segundo número "))

if num1 > num2:
    print(f"El mayor es el primer número {num1}")
elif num2 > num1:
    print(f"El mayor es el segundo número {num2}")
else:
    print("Son iguales")