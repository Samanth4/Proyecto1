#Samantha Dominguez Flores
prim = []
quin = []
ter = []
fin = []

opc = 1
while(opc != 0):
    opc = int(input("Menú\n1) Agregar alumno[1]\n2) Eliminar alumno[2]\n3) Salir[0]\n4) Opción: "))
    if opc == 1:
        nombre = input("Escribe el nombre del alumno a inscribir: ")
        opt = int(input("Ingresa la oportunidad del alumno:"))
        if opt == 1:
            prim.append(nombre)
            prim.sort
        elif opt == 3:
            ter.append(nombre)
            ter.sort
        elif opt == 5:
            quin.append(nombre)
            quin.sort
        else:
            print("Oportunidad inválida")
    elif opc == 2:
        nombre = input("Escribe el nombre del alumno a dar de baja: ")
        if nombre in prim:
            prim.remove(nombre)
            prim.sort()
        elif nombre in ter:
            ter.remove(nombre)
            ter.sort()
        elif nombre in quin:
            quin.remove(nombre)
            quin.sort()
        else:
            print("Alumno no encontrado. Ingrese de nuevo el nombre: ")   
    elif opc == 0:
        prim.sort()
        ter.sort()
        quin.sort()
        print("El grupo de 1era oportunidad es:")
        print (prim)
        print("El grupo de 3ra oportunidad es:")
        print(ter)
        print("El grupo de 5ta oportunidad es:")
        print(quin)
        print("Todos los grupos juntos son:")
        fin = prim+ter+quin
        print (fin)
    else:
        print("Opción no válida")
