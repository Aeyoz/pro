# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    data = {}
    with open(datafile) as pkcats:
        categories = pkcats.readline().strip().split(",")
    
    with open(datafile) as pkstats:
        stats = {}
        for categorie, pkstat in zip(categories, pkstats.readlines()[1:]):
            ""
        
    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')