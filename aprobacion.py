def verificar_aprobacion(promedio):
    if promedio is None:
        print("No es posible determinar el estado.")
        return

    if promedio >= 3:
        print("Estado: APROBADO")
    else:
        print("Estado: REPROBADO")

