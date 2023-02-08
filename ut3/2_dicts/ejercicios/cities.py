# ********************
# DESCIFRANDO CIUDADES
# ********************


def run(cinfo: str) -> dict:
    cities = {}
    city_and_inhabitants = cinfo.split(";")
    for i in city_and_inhabitants:
        city = i.split(":")[0]
        inhabitants = i.split(":")[1]
        cities[city] = inhabitants
    return cities


if __name__ == '__main__':
    run('Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000')
