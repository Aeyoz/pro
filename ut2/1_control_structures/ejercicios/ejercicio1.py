human1 = input('''You are Human1
1. Rock
2. Paper
3. Scissors
Your Choice: ''')

human2 = input('''You are Human2
1. Rock
2. Paper
3. Scissors
Your Choice: ''')

if human1 == human2 and (human1 and human2) != "":
    print("Tie")
elif human1 == "1" and human2 == "2":
    print("Human2 Paper's covers Human1 Rock's")
elif human1 == "1" and human2 == "3":
    print("Human1 Rock's smashes Human2 Scissors'")
elif human2 == "1" and human1 == "2":
    print("Human1 Paper covers Human2 Rock's")
elif human2 == "1" and human1 == "3":
    print("Human2 Rock's smashes Human1 Scissors'")
elif human1 == "2" and human2 == "3":
    print("Human2 Scissors' cuts Human1 Paper")
elif human2 == "2" and human1 == "3":
    print("Human1 Scissors' cuts Human2 Paper's")
elif human1 or human2 == "":
    print("Both have to choose an option to be able to play")
else:
    print("Not a valid option")
