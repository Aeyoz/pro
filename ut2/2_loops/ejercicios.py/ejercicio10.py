TILES = 6

for tile_1number in range(TILES + 1):
    for tile_2number in range(tile_1number, TILES + 1):
        print(f"[{tile_1number} | {tile_2number}]", end= " ")
    print()