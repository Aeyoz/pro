TILES = 6
for tile_1_number in range(TILES + 1):
    line = ""
    for tile_2_number in range(tile_1_number, TILES + 1):
        line += f"[{tile_1_number} | {tile_2_number}] "
    print(line)


# TILES = 6
# 
# for tile_1_number in range(TILES + 1):
#     for tile_2_number in range(tile_1_number, TILES + 1):
#         print(f"[{tile_1_number} | {tile_2_number}]", end= " ")
#     print()