can_fly = bool(int(input('''Can your character fly?:
0. No
1. Yes
''')))

is_human = bool(int(input('''Is it human?: 
0. No
1. Yes
''')))

has_mask = bool(int(input('''Has mask?: 
0. No
1. Yes
''')))

if can_fly:
    if is_human:
        if has_mask:
            print("Your character is IronMan")
        else:
            print("Your character is Captain Marvel")
    else:
        if has_mask:
            print("Your character is Ronnan Accuser")
        else:
            print("Your character is Vision")
else:
    if is_human:
        if has_mask:
            print("Your character is Spiderman")
        else:
            print("Your character is Hulk")
    else:
        if has_mask:
            print("Your character is Black Bolt")
        else:
            print("Your character is Thanos")