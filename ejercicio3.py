n1 = int(input("Ingrese su renta: "))

if (n1<=10000):
    print("su Tipo impositivo es de 5%")
elif (n1>10000 and n1 <=20000):
    print("su Tipo impositivo es de 15%")
elif (n1>20000 and n1 <= 35000):
    print("su Tipo impositivo es de 20%")
elif (n1>35000 and n1 <= 60000):
    print("su Tipo impositivo es de 30%")
elif (n1>60000):
    print("su Tipo impositivo es de 45%")