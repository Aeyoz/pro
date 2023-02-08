# ********************
# LEYENDO FICHEROS CSV
# ********************
from pathlib import Path


def run(datafile: Path) -> list:
    data = []
    with open(datafile) as pkcats:
        categories = pkcats.readline().strip().split(",")
    
    with open(datafile) as pkstats:
        for pkstat in pkstats.readlines()[1:]:
            pokemon = {}
            unprocessed_stats = pkstat.strip().split(",")
            stats = []
            for stat in unprocessed_stats:
                if stat.isdigit():
                    stats.append(int(stat))
                elif stat == "False":
                    stats.append(False)
                elif stat == "True":
                    stats.append(True)
                else:
                    stats.append(stat)
            for categorie, stat in zip(categories, stats):
                pokemon[categorie] = stat
            data.append(pokemon)
    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')