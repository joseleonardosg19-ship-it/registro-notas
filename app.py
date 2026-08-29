print(">>> ESTOY EJECUTANDO EL APP.PY NUEVO <<<")

from menu import mostrar_menu
from estudiantes import registrar_estudiante, listar_estudiantes
from notas import registrar_nota, calcular_promedio
from aprobacion import verificar_aprobacion

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_estudiante()

    elif opcion == "2":
        registrar_nota()

    elif opcion == "3":
        calcular_promedio()

    elif opcion == "4":
        listar_estudiantes()

    elif opcion == "5":
        promedio = calcular_promedio()
        verificar_aprobacion(promedio)

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")