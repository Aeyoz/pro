points = "AABAABABBABAAABABBBAABABABABABABABBBBABBABAAAAABBAABAABBABBAABBAAABBBAABAAABBBBAAAABBBBAAA"
games_player1 = games_player2 = 0
player1_score = player2_score = 0
new_game = player1_score == player2_score == 0
MIN_POINTS = 4
GAMES_TO_WIN = 2
for point in points:
    tie_break = games_player1 == games_player2 == 6 
    if point == "A":
        player1_score += 1
        if player1_score >= MIN_POINTS and player1_score - player2_score >= GAMES_TO_WIN:
            games_player1 += 1
            player1_score = player2_score = 0
    elif point == "B":
        player2_score += 1
        if player2_score >= MIN_POINTS and player2_score - player1_score >= GAMES_TO_WIN:
            games_player2 += 1
            player1_score = player2_score = 0
    if tie_break and new_game:
        MIN_POINTS = 7

print(games_player1, games_player2)