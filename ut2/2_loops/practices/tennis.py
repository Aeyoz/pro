points = """AABBAA BBAABB AABBAA AABBAA BBAABB BBAABB BBAABB BBAABB BBAABB
            AABBAA BBAABB AABBAA AABBAA BBAABB BBAABB BBAABB BBAABB BBAABB
            BBAABB AABBAA BBAABB BBAABB AABBAA AABBAA AABBAA AABBAA AABBAA
            BBAABB AABBAA BBAABB BBAABB AABBAA AABBAA AABBAA AABBAA AABBAA
            BBAABB AABBAA BBAABB BBAABB AABBAA AABBAA AABBAA AABBAA AABBAA
            BBAABB AABBAA BBAABB BBAABB AABBAA AABBAA AABBAA AABBAA AABBAA            
            AABBAA BBAABB AABBAA AABBAA BBAABB BBAABB BBAABB BBAABB BBAABB
            AABBAA BBAABB AABBAA AABBAA BBAABB BBAABB BBAABB BBAABB BBAABB
            AABBAA BBAABB AABBAA AABBAA BBAABB BBAABB BBAABB BBAABB BBAABB
            AABBAA BBAABB AABBAA AABBAA BBAABB BBAABB BBAABB BBAABB BBAABB
            """
winner = ""
A_sets = B_sets = 0
A_points = B_points = 0
player1_score = player2_score = 0
while winner == "":
    for point in points:
        match point:
            case "A":
                player1_score += 1
                if player1_score >= 4 and player1_score - player2_score >= 2:
                    A_points += 1
                    player1_score = player2_score = 0
                    if A_points - B_points >= 2 and A_points >= 6:
                        A_sets += 1
                        A_points = B_points = 0
            case "B":
                player2_score += 1
                if player2_score >= 4 and player2_score - player1_score >= 2:
                    B_points += 1
                    player1_score = player2_score = 0
                    if B_points - A_points >= 2 and B_points >= 6:
                        B_sets += 1
                        A_points = B_points = 0
            case _:
                continue
        if A_sets - B_sets >= 2:
            winner = f"El jugador1 tiene {A_sets} sets\nEl jugador2 tiene {B_sets} sets\nGanador : Jugador 1"
        elif B_sets - A_sets >= 2:
            winner = f"El jugador1 tiene {A_sets} sets\nEl jugador2 tiene {B_sets} sets\nGanador : Jugador 2"

print(winner)