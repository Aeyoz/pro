# *******************
# TEMPERATURAS MEDIAS
# *******************
import filecmp
from pathlib import Path


def run(input_path: Path) -> bool:
    output_path = 'data/avg_temps/avg_temps.dat'
    with open("data/avg_temps/temperatures.dat") as data:
        avg_temps = open(output_path, "w")
        for month in data:
            temps = [int(temp) for temp in month.split(",")]
            avg_temp = (sum(temps) / len(temps))
            avg_temps.write(f"{avg_temp}\n")
    
    avg_temps.close()    

    return filecmp.cmp(output_path, 'data/avg_temps/.expected', shallow=False)


if __name__ == '__main__':
    run('data/avg_temps/temperatures.dat')