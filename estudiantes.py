estudiantes = {}


def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    if nombre in estudiantes:
        print("El estudiante ya está registrado.")
    else:
        estudiantes[nombre] = []
        print("Estudiante registrado correctamente.")


def listar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    print("\n--- ESTUDIANTES REGISTRADOS ---")

    for nombre, notas in estudiantes.items():
        print(f"Estudiante: {nombre}")
        print(f"Notas: {notas}")