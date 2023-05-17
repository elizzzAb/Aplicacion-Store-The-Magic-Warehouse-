#Variables
Start = False
Variables = True
y = []

#Usuarios
Usuarios = ["Pedro Alvarenga","","Marilyn Funetes"]
CorreosG = ["ivanmemb49@gmail.com","soniaabrego67@gmail.com","marilynfuentes2023@gmail.com"]

#Variables del almacenamiento
while Variables:

    Areas = ["Golosinas","Limpieza"]

    CategoriasS = [["Churros","Bebidas","Dulces"],["Jabones","Desinfectantes","Shampos"]]
    CategoriasG = ["Churros","Bebidas","Dulces","Jabones","Desinfectantes","Shampos"]

    Productos = [[["Nachos","Yuca","YucaTekas","Platanitos","Alboroto","Candy Maíz","Cereza","Toztecas TNT","Toztecas Pizza","Toztecas Original","Jalapeños","Quesitos","Churritos","CogaMix"],
                ["Coca-Cola Original","Coca-Cola sin Azúcar","Fanta","Fresca","Tropical","Jugos del Valle","Powerade","Gatorade","Monster","Adrenaline","Energy","Agua Cristal","Agua del Campo"],
                ["Caramelos de Leche","Cereza","Menta"]],
                [["Palmolive","Dove","Suave","Nivea","Olay","Rexona","Axe","Lysol","Avon","Natural","Ambar","Supremo","Celestial","Eleglance","Essentials","Happy Chic","Jabontopía"],
                ["Alcohol isopropílico","Alcohol etílico","Ácido peracético","Fenol","Ácido láctico","Lysol","Clorox","Pine-Sol","Seventh Generation","Fabuloso","Windex","Zep"],
                ["Pantene Pro-V","Head & Shoulders","Garnier Fructis","L'Oreal Paris Elvive","Dove","Suave","Aussie","Paul Mitchell","Bumble and Bumble","Aveda","Moroccanoil","Nexxus","Matrix Biolage","Cantu"]]]
    ProductosS = [["Nachos","Yuca","YucaTekas","Platanitos","Alboroto","Candy Maíz","Cereza","Toztecas TNT","Toztecas Pizza","Toztecas Original","Jalapeños","Quesitos","Churritos","CogaMix"],
                  ["Coca-Cola Original","Coca-Cola sin Azúcar","Fanta","Fresca","Tropical","Jugos del Valle","Powerade","Gatorade","Monster","Adrenaline","Energy","Agua Cristal","Agua del Campo"],
                  ["Caramelos de Leche","Cereza","Menta"],
                  ["Palmolive","Dove","Suave","Nivea","Olay","Rexona","Axe","Lysol","Avon","Natural","Ambar","Supremo","Celestial","Eleglance","Essentials","Happy Chic","Jabontopía"],
                  ["Alcohol isopropílico","Alcohol etílico","Ácido peracético","Fenol","Ácido láctico","Lysol","Clorox","Pine-Sol","Seventh Generation","Fabuloso","Windex","Zep"],
                  ["Pantene Pro-V","Head & Shoulders","Garnier Fructis","L'Oreal Paris Elvive","Dove","Suave","Aussie","Paul Mitchell","Bumble and Bumble","Aveda","Moroccanoil","Nexxus","Matrix Biolage","Cantu"]]
    ProductosG = ["Nachos","Yuca","YucaTekas","Platanitos","Alboroto","Candy Maíz","Cereza","Toztecas TNT","Toztecas Pizza","Toztecas Original","Jalapeños","Quesitos","Churritos","CogaMix","Coca-Cola Original","Coca-Cola sin Azúcar","Fanta","Fresca","Tropical","Jugos del Valle","Powerade","Gatorade","Monster","Adrenaline","Energy","Agua Cristal","Agua del Campo","Caramelos de Leche","Cereza","Menta","Palmolive","Dove","Suave","Nivea","Olay","Rexona","Axe","Lysol","Avon","Natural","Ambar","Supremo","Celestial","Eleglance","Essentials","Happy Chic","Jabontopía","Alcohol isopropílico","Alcohol etílico","Ácido peracético","Fenol","Ácido láctico","Lysol","Clorox","Pine-Sol","Seventh Generation","Fabuloso","Windex","Zep","Pantene Pro-V","Head & Shoulders","Garnier Fructis","L'Oreal Paris Elvive","Dove","Suave","Aussie","Paul Mitchell","Bumble and Bumble","Aveda","Moroccanoil","Nexxus","Matrix Biolage","Cantu"]

    PreciosS = [[0.15,0.15,0.15,0.10,0.15,0.20,0.20,0.25,0.25,0.25,0.15,0.15,0.15,0.20],
               [0.75,0.85,0.65,0.70,0.60,0.65,0.75,1.25,0.90,0.85,0.90,0.50,0.30],
               [0.25,0.20,0.35],
               [1.75,1.30,1.45,0.85,0.90,1.20,0.60,0.95,1.10,1.05,0.94,1.80,1.90,1.99,2.10,1.97,1.15],
               [1.50,2.10,2.35,1.96,2.10,2.15,2.60,2.25,1.85,2.10,1.75,1.82],
               [1.90,2.50,2.20,3.00,2.60,2.70,2.05,1.15,1.50,1.55,1.25,1.40,3.15,1.97]]
    
    PreciosG = [0.15,0.15,0.15,0.10,0.15,0.20,0.20,0.25,0.25,0.25,0.15,0.15,0.15,0.20,0.75,0.85,0.65,0.70,0.60,0.65,0.75,1.25,0.90,0.85,0.90,0.50,0.30,0.25,0.20,0.35,1.75,1.30,1.45,0.85,0.90,1.20,0.60,0.95,1.10,1.05,0.94,1.80,1.90,1.99,2.10,1.97,1.15,1.50,2.10,2.35,1.96,2.10,2.15,2.60,2.25,1.85,2.10,1.75,1.82,1.90,2.50,2.20,3.00,2.60,2.70,2.05,1.15,1.50,1.55,1.25,1.40,3.15,1.97]

    break

#Variables de ventas
Compras = []
Monto = []
NUsuario = []

#Inicio de sesión o registro
def SesionRegistro():
    RegistroCompleto = False
    while RegistroCompleto == False:
        x = 0
        while x < 4:
            Registro = input("\nRegistro\nYa poseé una cuenta?: \n1. Si\n2. No \n-> ").lower()
            if Registro == "si".lower() or Registro == "1":
                print("\n\tCuentas activas")
                x = 0
                for i in CorreosG:
                    print(f"\t{x + 1}- {CorreosG[x]}")
                    x += 1
                    
                Correo = input("\nIngrese su corrreo: ")
                if Correo in CorreosG:
                    Contraseña = input("Ingrese su contraseña: ")
                    Position = CorreosG.index(Correo)
                    NUsuario.append(Usuarios[Position])
                    RegistroCompleto = True
                    break

                else:
                    print("\n~~~ Correo no válido ~~~")
                    x += 1
                    break

            elif Registro == "no".lower() or Registro == "2":
                Nombre = input("\nIngrese su nombre: ")
                Apellido = input("Ingrese su apellido: ")
                Datos_ID = input("Igrese su ID -> ")
                Correo = 1
                while Correo:
                    Correo = input("Ingrese su corrreo: ")
                    if "@" in Correo:
                        break
                
                    else:
                        print("~~~ Correo no válido (Debe llevar un @) ~~~")
                        
                Contraseña = input("Cree una contraseña: ")
                NUsuario.append(f"{Nombre} {Apellido}")
                RegistroCompleto = True
                CorreosG.append(Correo)
                Usuarios.append(f"{Nombre} {Apellido}")
                break

            else:
                print("~~~ Dato no válido ~~~")
                x += 1

#Programas 

def ProgramaCompras():
    FinPrograma = False
    print('\nBienveniddo a "Store The Magic Warehouse"')

    while Areas:
        w = 0

        #Imprimiendo las Areas
        print("\nAlmacenamiento")
        print("\n\tÁreas:")
        x = 0
        for i in Areas:
            print(f"\t{x + 1}- {Areas[x]}")
            x += 1

        SelectA = input("\nElija el área: ")

        if SelectA in Areas:
            
            #Imprimiendo las Categorias
            while w < 4:
                positionA = Areas.index(SelectA)
                print("\n\tCatregorías:")
                x = 0
                for i in CategoriasS[positionA]:
                    print(f"\t{x + 1}- {CategoriasS[positionA][x]}")
                    x += 1

                SelectB = input("\nElija la categoría -> ")

                if SelectB in CategoriasG:

                    #Imprimiendo los Productos
                    w = 0
                    while w < 4:
                        positionB = CategoriasS[positionA].index(SelectB)
                        positionC = ProductosS.index(Productos[positionA][positionB])
                        print("\n\tProductos")
                        x = 0
                        for i in range(len(ProductosS[positionC])):
                            print(f"\t{x + 1}- {ProductosS[positionC][x]}\t\t${PreciosS[positionC][x]}")
                            x += 1

                        SelectC = input("\nElija el producto -> ")

                        if SelectC in ProductosG:
                            Compras.append(SelectC)

                            positionD = ProductosS[positionC].index(SelectC)
                            
                            PositionE = PreciosS[positionC][positionD]#########
                            
                            Monto.append(PositionE)

                            print(Monto)

                            #Comprar algo más o cerrar el programa
                            w = 0
                            while w == 0:
                                Continuar = input("\n¿Desea comprar algo más? -> ").lower()
                                if Continuar == "si".lower():
                                    FinPrograma = False
                                    break

                                elif Continuar == "no".lower():
                                    FinPrograma = True
                                    break

                                else:
                                    print("\n~~~ Opción no válida ~~~")

                            break

                        else:
                            w += 1
                            if w == 4:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("~~~ Demasiados intentos fallidos ~~~")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            
                            else:
                                print("\n~~~ Opción no válida ~~~")

                    break

                else:
                    w += 1
                    if w == 4:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("~~~ Demasiados intentos fallidos ~~~")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    
                    else:
                        print("\n~~~ Opción no válida ~~~")

        else:
            print("\n~~~ Opción no válida ~~~")

        if FinPrograma == True:
            print("\nProductos comprados:")
            x = 0
            for i in range(len(Compras)):
                print(f"{x + 1}- {Compras[x]}")
                x += 1

            print(Monto)

            break

def ProgramaGerente():
    FinPrograma = False

    while Areas:
        w = 1

        #Imprimiendo las Areas
        print("\nAlmacenamiento")
        print("\n\tÁreas:")
        x = 0
        for i in Areas:
            print(f"\t{x + 1}- {i}")
            x += 1

        SelectA = input("\nElija el área: ")

        if SelectA in Areas:
            
            #Imprimiendo las Categorias
            w = 0
            while w < 4:
                print("\n\tCatregorías:")
                positionA = Areas.index(SelectA)#SOLO pude ser 0 y 1
                x = 0
                for i in CategoriasS[positionA]:
                    print(f"\t{x + 1}- {CategoriasS[positionA][x]}")
                    x += 1

                SelectB = input("\nElija la categoría -> ")

                if SelectB in CategoriasG:

                    #Imprimiendo los Productos
                    w = 0
                    while w < 4:
                        positionB = CategoriasS[positionA].index(SelectB)
                        positionC = ProductosS.index(Productos[positionA][positionB])
                        #positionC = Productos[positionA][positionB].index(Productos[positionA][positionB])
                        
                        print("\n\tProductos")
                        x = 0
                        for i in ProductosS[positionC]:
                            print(f"\t{x + 1}- {ProductosS[positionC][x]}\t\t${PreciosS[positionC][x]}")
                            x += 1

                        #Seguir revisando o cerrar el programa
                        w = 0
                        while w == 0:
                            Continuar = input("\n¿Desea segir revisando? -> ").lower()
                            if Continuar == "si".lower():
                                FinPrograma = False
                                break

                            elif Continuar == "no".lower():
                                FinPrograma = True
                                break

                            else:
                                print("\n~~~ Opción no válida ~~~")

                        break
                    break

                else:
                    print("\n~~~ Opción no válida ~~~")
                    w += 1

        else:
            print("\n~~~ Opción no válida ~~~")

        if FinPrograma == True:
            break

def ProgramaVentas():
    Total = 0
    w = True
    while w == True:
        a = True
        while a == True:
            try:
                for i in Monto:
                    Total += i

                print("\nBienvenido al Cajero")
                print(f"\nSu cuenta es de: ${round(Total,2)}")
                Pago = float(input("Ingrese su pago -> $"))
                break

            except ValueError:
                print("\n~~~ El valor ingresado no es válido ~~~")
                Total = 0
                continue

        if Pago >= Total:
            print("\n\t---------")
            print("\t|Factura|")
            print("\t---------")
            print("--------------------------------")
            print(f"Usted pago: ${round(Total,2)}")
            print(f"Su cambio es de: ${round(Pago - Total,2)}")
            print("--------------------------------")
            print("\nProductos comprados:")
            x = 0
            for i in range(len(Compras)):
                print("--------------------------------")
                print(f"| {x + 1}- {Compras[x]}")
                x += 1

            print("--------------------------------")
            print(f"Cliente: {NUsuario[0]}")
            print("--------------------------------")
            Compras[:] = []
            Monto[:] = []
            w = False

        else:
            Total = 0
            z = True
            y = True
            print("\nUsted no cuenta con saldo suficiente")
            while y == True:
                AccionP = input("\n\tAcciones:\n\t1. Quitar productos\n\t2. Reingresar saldo\n\t3. Dejar de comprar\n\n¿Qué desea hacer? -> ").lower()

                if AccionP == "Quitar productos".lower() or AccionP == "Quitar".lower() or AccionP == "1":
                    while z == True:
                        print("\n\tProductos en el carrito:")
                        x = 0
                        for i in Compras:
                            print(f"\t{x + 1}- {i}")
                            x += 1

                        AccionQ = input("\n¿Qué producto desea quitar? -> ")

                        if AccionQ in Compras:
                            position = Compras.index(AccionQ)
                            Monto.remove(Monto[position])
                            Compras.remove(AccionQ)

                            z = True
                            while z == True:
                                Re_New = input("\n\tAcciones:\n\t1. Quitar otro producto\n\t2. Regresar\n\n¿Qué desea hacer? -> ").lower()
                                
                                if Re_New == "Quitar otro producto".lower() or Re_New == "Quitar".lower() or Re_New == "Quitar otro".lower() or Re_New == "1":
                                    break

                                elif Re_New == "Regresar".lower() or Re_New == "2":
                                    z = False
                                    break

                elif AccionP == "Reingresar saldo".lower() or AccionP == "Reingresar".lower() or AccionP == "2":
                    y = False

                elif AccionP == "Dejar de comprar".lower() or AccionP == "Dejar".lower() or AccionP == "3":
                    w = False
                    y = False
                    Compras[:] = []
                    Monto[:] = []

                else:
                    print("\n~~~ Opción no válida ~~~")

def ProgramaAdmin():
    while Areas:
        AccionPA = input("\n\tAcciones\n\t1. Revisar el programa\n\t2. Agregar area\n\t3. Agregar categoria\n\t4. Agregar producto\n\t5. Salir\n\n¿Que desea hacer? -> ").lower()

        if AccionPA == "Revisar".lower() or AccionPA == "Revisar el programa".lower() or AccionPA == "1":
            ProgramaGerente()

        #Nueva area
        elif AccionPA == "Agregar area".lower() or AccionPA == "Agregar área".lower() or AccionPA == "Area".lower() or AccionPA == "Área".lower() or AccionPA == "2":
            w = 1
            while w:
                New_Area = input("\nNombre del area que quieras crear -> ")
                Confirmation = input(f"Area: {New_Area}, ¿Esta seguro? Si/No -> ").lower()

                #Nueva categoría -> Crear area
                if Confirmation == "si".lower():
                    Areas.append(New_Area)
                    while w:
                        New_Categoria = input("\nDebe agregar al menos 1 categoria -> ")
                        Confirmation2 = input(f"Categoría: {New_Categoria}, ¿Esta seguro? Si/No -> ").lower()

                        #Nueva area -> Crear area
                        if Confirmation2 == "si".lower():
                            CategoriasS.append([New_Categoria])
                            CategoriasG.append(New_Categoria)
                            while w:
                                New_Producto = input("\nDebe agregar al menos 1 producto -> ")
                                Confirmation3 = input(f"Producto: {New_Producto},¿Esta seguro? Si/No -> ").lower()

                                if Confirmation3 == "si".lower():
                                    Productos.append([[New_Producto]])
                                    ProductosS.append([New_Producto])
                                    ProductosG.append(New_Producto)
                                    Proveedor = input("\nProveedor-> ")
                                    Fecha_de_Caducidad = input("\nFecha de Caducidad -> ")
                                    Fecha_de_Entrada = input("\nFecha de Entrada -> ")
                                    Detalles = input("\nDetalles -> ")
                                    Unidades = input("\nUnidades -> ")  

                                    while w:
                                        try:
                                            New_Precio = float(input(f"\nIngrese el precio del producto {New_Producto} -> "))
                                        
                                        except ValueError:
                                            print("\nEse no es un precio válido")

                                        if New_Precio != ValueError:
                                            Confirmacion4 = input(f"Producto: {New_Producto}, precio {New_Precio}, ¿Esta seguro? Si/No -> ").lower()

                                            if Confirmacion4 == "si".lower():
                                                PreciosS.append([New_Precio])
                                                PreciosG.append(New_Precio)
                                                break

                                            else:
                                                continue
                                        else:
                                            continue
                                    break

                                else:
                                    continue
                            break

                        else:
                            continue
                    break

                else:
                    continue
            
        #Nueva Categoría
        elif AccionPA == "Agregar categoria".lower() or AccionPA == "Agregar categoría".lower() or AccionPA == "Categoria".lower() or AccionPA == "Categoría".lower() or AccionPA == "3":
            w = 1
            while w == 1:
                print("\n\tÁreas disponibles:")
                x = 0
                for i in Areas:
                    print(f"\t{x + 1}- {i}")
                    x += 1

                Select_Area = input("\n\nElija el área donde agregará la categoría -> ")

                if Select_Area in Areas:
                    positionA = Areas.index(Select_Area)
                    while w == 1:
                        New_Categoria = input("\nElija el nombre de  la categoría -> ")
                        Confirmation2 = input(f"Categoría: {New_Categoria}, ¿Esta seguro? Si/No -> ").lower()

                        #Nueva area -> Crear Categoría
                        if Confirmation2 == "si".lower():

                            CategoriasS[positionA].append(New_Categoria)

                            CategoriasG.append(New_Categoria)
                            positionB = CategoriasS[positionA].index(New_Categoria)

                            while w == 1:
                                New_Producto = input("\nDebe de agregar al menos 1 produto -> ")
                                Confirmation3 = input(f"Producto: {New_Producto}, ¿Esta seguro? Si/No -> ").lower()
                                
                                if Confirmation3 == "si".lower():
                                    Productos[positionA].append([New_Producto])
                                    ProductosS.insert(positionB, [New_Producto])
                                    ProductosG.append(New_Producto)
                                    Proveedor = input("\nProveedor-> ")
                                    Fecha_de_Caducidad = input("\nFecha de Caducidad -> ")
                                    Fecha_de_Entrada = input("\nFecha de Entrada -> ")
                                    Detalles = input("\nDetalles -> ")
                                    Unidades = input("\nUnidades -> ")
                                    while w:
                                        try:
                                            New_Precio = float(input("\nPongale el precio al producto -> "))

                                        except ValueError: continue

                                        if New_Precio != ValueError:
                                            Confirmation3 = input(f"Producto: {New_Producto}, precio: {New_Precio}, ¿Esta seguro? Si/No -> ").lower()
                                            if Confirmation3 == "si".lower():
                                                PreciosS.insert(positionB, [New_Precio])
                                                PreciosG.append(New_Precio)

                                                #print(CategoriasS)
                                                #print(ProductosS)
                                                #print(PreciosS)
                                                break

                                            else:
                                                continue

                                        else:
                                            continue
                                    break

                                else:
                                    continue
                            break

                        else:
                            continue
                    break

                else:
                    continue

        elif AccionPA == "Agregar producto".lower() or AccionPA == "Producto".lower() or AccionPA == "4":
            w = 1
            while w:
                print("\n\tÁreas disponibles:")
                x = 0
                for i in Areas:
                    print(f"\t{x + 1}- {i}")
                    x += 1

                Select_Area = input("\n\nElija el área en donde agregará el producto -> ")

                if Select_Area in Areas:
                    positionA = Areas.index(Select_Area)
                    while w:
                        print("\n\tCategorias disponibles:")
                        x = 0
                        for i in CategoriasS[positionA]:
                            print(f"\t{x + 1}- {i}")
                            x += 1

                        Select_Category = input("\n\nElija la categoría en donde agregará el producto -> ")

                        if Select_Category in CategoriasG:
                            positionB = CategoriasS[positionA].index(Select_Category)
                            
                            while w == 1:
                                New_Producto = input("\nEscriba el nombre del nuevo producto -> ")
                                Confirmation3 = input(f"Producto: {New_Producto}, ¿Esta seguro? Si/No -> ").lower()
                                
                                if Confirmation3 == "si".lower():
                                    Productos[positionA][positionB].append(New_Producto)
                                    positionC = Productos[positionA][positionB].index(New_Producto)
                                    ProductosS[positionB].append(New_Producto)
                                    ProductosG.append(New_Producto)
                                    #print(Productos)
                                    #print(ProductosS)
                                    Fecha_de_Caducidad = input("\nFecha de Caducidad -> ")
                                    Fecha_de_Entrada = input("\nFecha de Entrada -> ")
                                    Detalles = input("\nDetalles -> ")
                                    Unidades = input("\nUnidades -> ")
                                    
                                    while w:
                                        try:
                                            New_Precio = float(input("\nPongale el precio al producto -> "))

                                        except ValueError: continue

                                        if New_Precio != ValueError:
                                            Confirmation3 = input(f"Producto: {New_Producto}, precio: {New_Precio}, ¿Esta seguro? Si/No -> ").lower()
                                            if Confirmation3 == "si".lower():
                                                PreciosS[positionB].append(New_Precio)
                                                PreciosG.append(New_Precio)

                                                #print(CategoriasS)
                                                #print(ProductosS)
                                                #print(PreciosS)

                                                break

                                            else:
                                                continue
                                        else:
                                            continue
                                    break

                                else:
                                    continue
                            break

                        else:
                            continue
                    break
                
                else:
                    continue

        elif AccionPA == "Salir".lower() or AccionPA == "5":
            break

        else:
            print("\n~~~ Opción no válida ~~~")

def Ayuda():
    AEstados = ["Administrador", "Gerente", "Dependiente","Cliente","Salir"]

    while AEstados:
        print("\nHa entrado a ayuda al usuario\n")
        x = 0
        for elemento in AEstados:
            print(f"{x + 1}- {elemento}")
            x += 1

        SelectEstado = input("\n¿Sobre que desea saber? --> ").lower()

        if SelectEstado in AEstados[0].lower() or SelectEstado == "1":
            print("\nAdministrador permite las opciones para tener un control y edición de archivos y productos")
            
        elif SelectEstado in AEstados[1].lower() or SelectEstado == "2":
            print("\nGerente nos permite únicamente visualizar archivos")
            
        elif SelectEstado in AEstados[2].lower() or SelectEstado == "3":
            print("\nDependiente permite unicamente realizar ventas y hacer facturas")

        elif SelectEstado in AEstados[3].lower() or SelectEstado == "4":
            print("\nSer cliente le permite interactuar con los productos y agregar productos al carrito")

        elif SelectEstado in AEstados[4].lower() or SelectEstado == "5":
            break
        
        else:
            print("\nNo es posible ejecutar")

        Volver = input("\n¿Desea buscar algo mas? --> si/no -> ").lower()

        if Volver =="si".lower() or Volver == "volver".lower():
            continue

        elif Volver == "no".lower():
            break


#######################
## Inicios de prueba ##
#######################

#ProgramaAdmin()

#ProgramaGerente()

#ProgramaCompras()

#ProgramaVentas()

##################################################################################
##################################################################################
#####             ###         ###  ###            ###           ###  ######  #####
#####  #########  ###  #####  ###  ###  #############  ############    ####  #####
#####  #########  ###  ###   ####  ###  #############  ############  #  ###  #####
#####  #########  ###  ##  ######  ###  #####     ###           ###  ##  ##  #####
#####  #########  ###  ###  #####  ###  ########  ###  ############  ###  #  #####
#####  #########  ###  ####  ####  ###  ########  ###  ############  ####    #####
#####             ###  #####  ###  ###            ###           ###  #####   #####
##################################################################################
##################################################################################

#Inicio o no del programa
UsuarioActive = False
Reinicio = False
Continuar = True

while Start == False:
    if Reinicio == False:
        StartB = input("\n¿Desea iniciar el programa? -> ").lower()
    else:
        StartB = input("\n¿Desea reiniciar el programa? -> ").lower()        
    
    if StartB == "si".lower():

        while StartB == "si":
            
            while UsuarioActive == False:
                Registro = input("\n¿Desea iniciar sesion/Registrarse? -> ").lower()

                if Registro == "si".lower():
                    SesionRegistro()
                    UsuarioActive = True
                    break

                elif Registro == "no".lower():
                    break

                else:
                    print("\n~~~ Opción no válida ~~~")

            if UsuarioActive == True:

                while Continuar == True:
                    if Reinicio == False:
                        print(f"\n\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2")
                        print(f'\n\2 Bienvenido a "Store the Magic Warehouse", {NUsuario[0]} \2')
                        print(f"\n\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2")
                        
                    else:
                        print(f"\n\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2")
                        print(f'\n\2 Bienvenido de nuevo a "Store the Magic Warehouse", {NUsuario[0]} \2')
                        print(f"\n\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2\2")
                    
                    #Menu
                    Accion = input("\n\tMenú de navegación\n\t1. Realizar una compra\n\t2. Realizar una venta\n\t3. Revisar el almacenamiento\n\t4. Administrar Almacenamiento\n\t5. Ayuda\n\t6. Cerrar sesión \n\t7. Salir\n\n¿Que desea hacer? -> ").lower()

                    if Accion == "Ayuda".lower() or Accion == "5":
                        Ayuda()

                    elif Accion == "Comprar".lower() or Accion == "Realizar una compra".lower() or Accion == "1" or Accion == "Vender".lower() or Accion == "Realizar una venta".lower() or Accion == "2" or Accion == "Revisar".lower() or Accion == "Revisar el almacenamiento".lower() or Accion == "Revisar almacenamiento".lower() or Accion == "3" or Accion == "Administrar".lower() or Accion == "Administrar almacenamiento".lower() or Accion == "Administrar el almacenamiento".lower() or Accion == "4":
                        Estado = input("\n\tEstados:\n\t1. Dependiente\n\t2. Gerente\n\t3. Administrador\n\t4. Cliente\nEscoja su estado -> ").lower()
                        print(f"\nEstas en modo {Estado}")

                        if Estado == "Dependiente".lower()  or Estado == "Administrador".lower() or Estado == "Cliente".lower() or Estado == "Gerente".lower():
                            if (Accion == "Comprar".lower() or Accion == "Realizar una compra".lower() or Accion == "1") and (Estado == "Cliente".lower()):
                                ProgramaCompras()

                            elif (Accion == "Vender".lower() or Accion == "Realizar una venta".lower() or Accion == "2") and (Estado == "Dependiente".lower()):
                                ProgramaVentas()

                            elif (Accion == "Revisar".lower() or Accion == "Revisar el almacenamiento".lower() or Accion == "Revisar almacenamiento".lower() or Accion == "3") and (Estado == "Gerente".lower()):
                                ProgramaGerente()

                            elif (Accion == "Administrar".lower() or Accion == "Administrar almacenamiento".lower() or Accion == "4") and (Estado == "Administrador".lower()):
                                ProgramaAdmin()

                            else:
                                print(f"\nNo puede {Accion} si su estado es {Estado}")

                        else:
                            print("\n~~~ Estado no válido ~~~")

                    elif Accion == "Cerrar sesión".lower() or Accion == "Cerrar sesion".lower() or Accion == "Cerrar".lower() or Accion == "6":
                        UsuarioActive = False
                        Reinicio = True
                        Start = False
                        StartB = "no".lower()
                        NUsuario[:] = []
                        break

                    elif Accion == "Salir".lower() or Accion == "7":
                        StartB = "no".lower()
                        Start = True
                        break
                    
                    else:
                        print("\n~~~ Acción no válida ~~~")

                    Reinicio = True

            elif UsuarioActive == False:
                print("\nNo ha iniciado seción, inicie sesión/Registrese e intentelo nuevamente")

    elif StartB == "no".lower():
        break

    else:
        print("\n\t~~~ Opción no válida ~~~")
        continue

print("\nFin del programa")


#Este programa tiene el propsosito de administrar el almacenamiento interno de una tienda, 