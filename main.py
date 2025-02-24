from Persona import Persona
from estudiante import Estudiante

def mostrar_menu():
    print("\nMenu:")
    print("1. Registrar Persona")
    print("2. Registrar Estudiante")
    print("3. Salir")

def registrar_persona():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    direccion = input("Ingrese la dirección: ")
    return Persona(nombre, edad, direccion)

def registrar_estudiante():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    direccion = input("Ingrese la dirección: ")
    escuela = input("Ingrese la escuela: ")
    return Estudiante(nombre, edad, direccion, escuela)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            persona = registrar_persona()
            print("\nPersona registrada exitosamente.")
            print(persona)
        elif opcion == "2":
            estudiante = registrar_estudiante()
            print("\nEstudiante registrado exitosamente.")
            print(estudiante)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
