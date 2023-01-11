# ***************
# UN SET AL TENIS
# ***************

def run(points: str) -> tuple:
    games_player1 = games_player2 = 0
    player1_score = player2_score = 0
    GAMES_TO_WIN = 2
    for point in points:
        tie_break = games_player1 == games_player2 == 6 
        if tie_break:
            if point == "A":
                player1_score += 1
                if player1_score >= 7 and player1_score - player2_score >= 2:
                    games_player1 += 1
                    player1_score = player2_score = 0
            elif point == "B":
                player2_score += 1
                if player2_score >= 7 and player2_score - player1_score >= 2:
                    games_player2 += 1
                    player1_score = player2_score = 0
            if games_player1 == 7 or games_player2 == 7:
                player1_score = player2_score = 0      
        else:
            if point == "A":
                player1_score += 1
                if player1_score >= 4 and player1_score - player2_score >= 2:
                    games_player1 += 1
                    player1_score = player2_score = 0
            elif point == "B":
                player2_score += 1
                if player2_score >= 4 and player2_score - player1_score >= 2:
                    games_player2 += 1
                    player1_score = player2_score = 0

    return games_player1, games_player2

if __name__ == '__main__':
    run('AABBAABABBBABABABBBAAABBBABAABBABBAABBBABABBAAAABBBBABBBAB')
