notas = []


def registrar_nota():
    try:
        nota = float(input("Ingrese la nota (0 a 5): "))

        if 0 <= nota <= 5:
            notas.append(nota)
            print("Nota registrada correctamente.")
        else:
            print("La nota debe estar entre 0 y 5.")

    except ValueError:
        print("Ingrese un valor numérico válido.")


def calcular_promedio():
    if len(notas) == 0:
        print("No hay notas registradas.")
        return None

    promedio = sum(notas) / len(notas)

    print(f"Promedio: {promedio:.2f}")

    return promedio