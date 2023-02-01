# ****************
# YELLOW SUBMARINE
# ****************
from pathlib import Path


def run(route_path: Path) -> tuple:

    with open(route_path) as f:
        fuel = int(f.readline())
        distances = "".join(f.readline()).strip()
        lower_distance, upper_distance = 600, 0
        distance = depth = 0
        for position in distances.split(","):
            x, y = position.split(":")
            x, y = int(x), int(y)
            distance += x
            depth += y
            fuel -= 3 * abs(x) 
            if fuel == 0 or depth < upper_distance or depth > lower_distance:
                break

    return distance, depth, fuel


if __name__ == '__main__':
    run('data/submarine/route1.dat')