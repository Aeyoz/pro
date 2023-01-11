# ***************
# UN SET AL TENIS
# ***************

def run(points: str) -> tuple:
    games_player1 = games_player2 = 0
    player1_score = player2_score = 0 
    for point in points:
        tie_break = games_player1 == games_player2 == 6
        match tie_break:
            case True:
                match point:
                    case "A":
                        player1_score += 1
                        if player1_score >= 4 and player1_score - player2_score >= 2:
                            games_player1 += 1
                            player1_score = player2_score = 0
                    case "B":
                        player2_score += 1
                        if player2_score >= 4 and player2_score - player1_score >= 2:
                            games_player2 += 1
                            player1_score = player2_score = 0
                if 7 == games_player1 > games_player2 and player1_score >= 7 and player1_score - player2_score >= 2:
                    break
                elif 7 == games_player2 > games_player1 and player1_score >= 7 and player2_score - player1_score >= 2:
                    break
            case _:
                match point:
                    case "A":
                        player1_score += 1
                        if player1_score >= 4 and player1_score - player2_score >= 2:
                            games_player1 += 1
                            player1_score = player2_score = 0
                    case "B":
                        player2_score += 1
                        if player2_score >= 4 and player2_score - player1_score >= 2:
                            games_player2 += 1
                            player1_score = player2_score = 0
                    case _:
                        continue
    return games_player1, games_player2

if __name__ == '__main__':
    run('AABBAABABBBABABABBBAAABBBABAABBABBAABBBABABBAAAABBBBABBBAB')