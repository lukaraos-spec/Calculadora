lista = []

def opc():
    while True:
        try:
            opcion = int( input("Ingrese el numero de la opcion deseada: "));
            if opcion > 0 and opcion < 7:
                return opcion
            else:
                raise ValueError("Ingrese un numero valido.");
        except ValueError:
            print("Error: Ingrese un numero valido.");

def nomb_est(nombre):
    return nombre.strip() != ""

def edad_est(edad):
    return edad > 0

def nota_est(nota):
    return nota >= 1.0 and nota <= 7.0

def aprob_est(nota):
    return nota >= 4.0

def menu():
    print("---------- Menu de opciones ----------");
    print("1. Agregar estudiante");
    print("2. Buscar estudiante");
    print("3. Eliminar estudiante");
    print("4. Actualizar estados");
    print("5. Mostrar estudiantes");
    print("6. Salir");
    print("--------------------------------------");


def agregar_estudiante(lista):
    while True:
        try:
            nombre = input("Ingrese el nombre del estudiante: ");
            if nomb_est(nombre):
                print("Nombre ingresado correctamente.");
                break
            else:
                raise ValueError("El nombre no puede estar vacio o contener solo espacios en blanco.");
        except ValueError:
            print("Error: El nombre no puede estar vacio o contener solo espacios en blanco.");
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "));
            if edad_est(edad):
                print("Edad ingresada correctamente.");
                break
            else:
                raise ValueError("la edad debe ser un numero entero positivio.");
        except ValueError:
            print("Error: La edad debe ser un numero entero positivo.");
    while True:
        try:
            
            nota = float(input("Ingrese la nota del estudiante: "));
            if nota_est(nota):
                print("Nota ingresada correctamente.");
                break
            else:
                raise ValueError("La nota debe ser un numero decimal entre 1.0 y 7.0.");
        except ValueError as e:
            print(e)

    lista.append({"nombre": https://n9.cl/ln882 , "edad": edad, "nota": nota, "aprobado": False});


def busc_est(estudiante):
    posis = 0
    for alumno in lista:
        if alumno["nombre"] == estudiante:
            return posis
        posis += 1
        
    return -1

#opc3
def eliminar_est(estudiante):
    for perfil_est in lista:
        if perfil_est["nombre"] == estudiante:
            lista.remove(perfil_est);
        else:
            print("Estudiante no encontrado en la lista.");

#opc4
def actualizar_estados():
    for posis in range(len(lista)):
        lista[posis]["aprobado"] = aprob_est(lista[posis]["nota"]);

#opc5
def mostrar_estudiantes():
    actualizar_estados();
    for estudiante in lista:
        print("Nombre:", estudiante["nombre"]);
        print("Edad:", estudiante["edad"]);
        print("Nota:", estudiante["nota"]);
        print("Aprobado:", estudiante["aprobado"]);
        print("------------------------");

while True:

    menu();

    opcion = opc();
    if opcion == 1:
        agregar_estudiante(lista);
    elif opcion == 2:
        while True:
            try:
                estudiante = input("Ingrese el nombre del estudiante a buscar: ");
                if nomb_est(estudiante):
                    break
                else:
                    raise ValueError("El nombre no puede estar vacio o contener solo espacios en blanco.");
            except ValueError as e:
                print(f"{e}");

        if busc_est(estudiante) != -1:
            print("Estudiante encontrado en la lista.");
            perfil_est = lista[busc_est(estudiante)]
            print("=== LISTA DE ESTUDIANTES ===");
            print("Nombre:", perfil_est["nombre"]);
            print("Edad:", perfil_est["edad"]);
            print("Nota:", perfil_est["nota"]);
            print("Aprobado:", perfil_est["aprobado"]);
            print("********************************************");
        else:
            print("Estudiante no encontrado en la lista.");

    elif opcion == 3:
        while True:
            try:
                estudiante = input("Ingrese el nombre del estudiante a eliminar: ");
                if nomb_est(estudiante):
                    break
                else:
                    raise ValueError("El nombre no puede estar vacio o contener solo espacios en blanco.");
            except ValueError as e:
                print(f"{e}");
        
        eliminar_est(estudiante)
        print("Estudiante eliminado correctamente.");
    elif opcion == 4:
        actualizar_estados();
        print("Estados actualizados correctamente.");
    elif opcion == 5:
        mostrar_estudiantes();
    elif opcion == 6:
        print("“Gracias por usar el sistema. Vuelva Pronto”.");
        break
    else:
        print("Opcion invalida. Por favor, ingrese un numero valido del 1 al 6.");
