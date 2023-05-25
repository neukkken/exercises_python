pedido = int(input("1 para pizza vegetariana, 2 para no vegetariana: "))
pedido2 = 0

if (pedido == 1):
    print("Eliga entre los siguientes ingredientes")
    pedido2 = int(input("1 Pimenton, 2 Tofu: "))

    print("La pizza que ordeno lleva los siguientes ingredientes: ")
    
elif (pedido == 2):
    print("Eliga entre los siguientes ingredientes")
    pedido2 = int(input("1 Peperoni, 2 Jamón, 3 Salmon: "))