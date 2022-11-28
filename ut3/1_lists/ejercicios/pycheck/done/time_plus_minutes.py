'''
Dada una hora en formato HH:MM y un número de minutos (en valor entero), calcule la hora
resultante (en formato HH:MM) si sumamos los minutos a la hora de entrada.

Trabaje con formato de 24 horas.
'''


def run(time: str, offset: int) -> str:
    time_hours = int(time.split(":")[0])
    time_minutes = int(time.split(":")[1])
    hours_offset = offset // 60
    minutes_offset = offset - hours_offset * 60
    final_minutes = time_minutes + minutes_offset
    added_hour = 0
    if final_minutes > 60:
        added_hour = 1
        final_minutes -= 60
    final_hour = time_hours + hours_offset + added_hour
    if final_hour > 24:
        final_hour -= 24
    final_time = f"{final_hour}:{final_minutes}"
    return final_time


if __name__ == '__main__':
    run('17:15', 240)
