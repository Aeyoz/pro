# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:
    winner = ""
    A_match_points = B_match_points = 0
    player1_score = player2_score = 0
    while winner == "":
        for point in points:
            match point:
                case "A":
                    player1_score += 1
                    if player1_score >= 4 and player1_score - player2_score >= 2:
                        A_match_points += 1
                        player1_score = player2_score = 0
                case "B":
                    player2_score += 1
                    if player2_score >= 4 and player2_score - player1_score >= 2:
                        B_match_points += 1
                        player1_score = player2_score = 0
                case _:
                    continue
            if A_match_points - B_match_points >= 2:
                winner = f"El jugador1 tiene {A_match_points} sets\nEl jugador2 tiene {B_match_points} sets"
            elif B_match_points - A_match_points >= 2:
                winner = f"El jugador1 tiene {A_match_points} sets\nEl jugador2 tiene {B_match_points} sets\nEl ganador es el jugador1 (A)"
            else: 
                winner = f"El jugador1 tiene {A_match_points} sets\nEl jugador2 tiene {B_match_points} sets\nPor lo tanto no hay ganador"
    return winner

if __name__ == '__main__':
    run('ABAABA')
