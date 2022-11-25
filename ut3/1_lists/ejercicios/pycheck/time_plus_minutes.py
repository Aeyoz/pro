'''
Dada una hora en formato HH:MM y un número de minutos (en valor entero), calcule la hora
resultante (en formato HH:MM) si sumamos los minutos a la hora de entrada.

Trabaje con formato de 24 horas.
'''


def run(time: str, offset: int) -> str:
    time_hours = int(time.split(":")[0])
    time_minutes = int(time.split(":")[1])
    offset_hours = offset // 60
    offset_minutes = offset - (offset_hours * 60)
    time_hours += offset_hours
    final_time = f"{time_hours}:{time_minutes}"
    return final_time


if __name__ == '__main__':
    run('17:15', 240)
