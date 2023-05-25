n1 = float(input("Ingrese su puntacion y tal: "))

if (n1==0.0):
    print ("Su nivel es Inaceptable y cobra: 2400")
elif(n1==0.4):
    print("Su nivel es Aceptable y cobra: ", 2400*n1)
elif(n1>=0.6):
    print("Su nivel Meritorio es y cobra: ", 2400*n1)