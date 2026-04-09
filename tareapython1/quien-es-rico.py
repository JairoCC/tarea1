
nombre = input("cual es tu nombre?: ")

while nombre == "" or nombre.isdigit():
    nombre = input("ingresa un nombre valido: ")

edad = input("Que edad tienes?: ")


while True:

    if not edad.isdigit():
        edad = input("ingresa una edad valida: ")
        continue
    edad = int(edad)
    if edad < 0:
        print("Ingresa una edad válida (no negativa).")
    else:
        break

print("Hola, " + nombre + " tu tienes " + str(edad) + " y eres rico.")