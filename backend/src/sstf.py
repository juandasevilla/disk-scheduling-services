def sstf(arm_position, lrequests, debug=False):
    """
    SSTF Disk Scheduling Algorithm (Shortest Seek Time First)

    Args:
        arm_position (int): Posición inicial del brazo del disco
        lrequests (list<int>): Lista de solicitudes de acceso a las pistas
        debug (bool): Si es True, imprime el movimiento del brazo durante la ejecución

    Returns:
        dict: Diccionario con la secuencia de movimientos, la distancia total recorrida y el promedio de distancia.
    """
    distance = 0
    n = len(lrequests)
    current_pos = arm_position
    requests = lrequests.copy()  # Copiar la lista de solicitudes para no modificar la original
    sequence = [arm_position]  # Iniciar la secuencia con la posición inicial

    # Mientras haya solicitudes por atender
    while requests:
        # Encontrar la solicitud más cercana
        closest_request = min(requests, key=lambda x: abs(x - current_pos))

        # Calcular la distancia
        distance += abs(closest_request - current_pos)
        current_pos = closest_request

        # Agregar la solicitud a la secuencia
        sequence.append(current_pos)

        # Si debug está activado, imprimir el movimiento
        if debug:
            print("> Se movió a", current_pos)

        # Eliminar la solicitud procesada de la lista
        requests.remove(closest_request)

    # Calcular el promedio de distancia recorrida
    average = distance / n

    # Retornar el resultado como un diccionario
    return {
        "sequence": sequence,
        "average": average,
        "distance": distance,
    }
