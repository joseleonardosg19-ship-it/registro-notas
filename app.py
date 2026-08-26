notas = []


def registrar_nota():
    nota = float(input("Ingrese la nota (0 a 5): "))

    if 0 <= nota <= 5:
        notas.append(nota)
        print("Nota registrada correctamente.")
    else:
        print("La nota debe estar entre 0 y 5.")


def calcular_promedio():
    if len(notas) == 0:
        print("No hay notas registradas.")
    else:
        promedio = sum(notas) / len(notas)
        print(f"Promedio: {promedio:.2f}")

        if promedio >= 3:
            print("Estado: APROBADO")
        else:
            print("Estado: REPROBADO")


while True:
    print("\n--- REGISTRO DE NOTAS ---")
    print("1. Registrar nota")
    print("2. Ver promedio")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_nota()
    elif opcion == "2":
        calcular_promedio()
    elif opcion == "3":
        print("Programa finalizado")
        break
    else:
        print("Opción no válida")