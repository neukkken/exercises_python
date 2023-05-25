euros = int(input("Ingrese sus ingresos: "))
edad = int(input("Ingrese su edad: "))

if (euros >= 1000 and edad >= 16):
    print("Debe tributar")
else:
    print("No debe tributar")