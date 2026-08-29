from estudiantes import estudiantes

def registrar_nota():
    if len(estudiantes) == 0:
        print("Primero debe registrar un estudiante.")
        return

    nombre = input("Ingrese el nombre del estudiante: ").strip()

    if nombre not in estudiantes:
        print("El estudiante no está registrado.")
        return

    try:
        nota = float(input("Ingrese la nota (0 a 5): "))

        if nota < 0 or nota > 5:
            print("Error: la nota debe estar entre 0 y 5.")
            return

        estudiantes[nombre].append(nota)
        print("Nota registrada correctamente.")

    except ValueError:
        print("Error: ingrese un valor numérico válido.")


def calcular_promedio():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return None

    nombre = input("Ingrese el nombre del estudiante: ").strip()

    if nombre not in estudiantes:
        print("El estudiante no está registrado.")
        return None

    notas = estudiantes[nombre]

    if len(notas) == 0:
        print("El estudiante no tiene notas registradas.")
        return None

    promedio = sum(notas) / len(notas)

    print(f"Estudiante: {nombre}")
    print(f"Notas: {notas}")
    print(f"Promedio: {promedio:.2f}")

    return promedio

