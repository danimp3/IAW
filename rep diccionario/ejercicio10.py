clientes = {}




while True:
    
    print("!Bienvenido al sistema!,eliga una de las siguientes opciones:")
    print("1. Registro de usuario en el sistema")
    print("2. Eliminar usuarios del sistema")
    print("3. Mostrar datos de usuario")
    print("4. Mostrar todos los usuarios")
    print("5. Mostrar todos los usuarios preferentes")
    print("6. Terminar programa")
    opc = int(input("Seleccione una opcion: "))
    
        
    if opc == 1:
        nif = input("NIF del usuario: ")
        nombr = input("Nombre del usuario: ")
        direc = input("Direccion del usuario: ")
        tfono = input("Telefono del usuario: ")
        correo = input("Correo del usuario: ")
        prefer = input("¿Es preferente?(Si/No)").lower() == 'sí'
        
        clientes[nif] = {'nombre': nombr, 'direccion': direc, 'telefono': tfono, 'correo': correo, 'preferente': prefer}
        print("Usuario agregado con exito")
    elif opc == 2:
        nif = input("NIF del usuario: ")
        if nif in clientes:
            clientes.pop(nif)
            print("Usuario eliminado correctamente")
        else:
            print("Usuario no encontrado")
    elif opc == 3:
        nif = input("NIF del usuario: ")
        if nif in clientes:
            print(clientes.get(nif))
        else:
            print("Usuario no encontrado")
    elif opc == 4:
        print(clientes)
    elif opc == 5:
        for nif, datos in clientes.items():
            if datos['preferente']:
                print("NIF:", nif, "- Nombre:", datos['nombre'])
    elif opc == 6:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida, seleccione otra")
            
            
            
            
            
            
            

