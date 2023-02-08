age = int(input("Introduce your age: "))
weight = int(input("Introduce your weight: "))
heartbeat = int(input("Introduce your heartbeat time: "))
platelets = int(input("Introduce your total of platelets: "))
wrong= ""
good = ""

match age: 
    case age if 18 > age:
        wrong += "you are too young, "
    case age if age >= 65:
        wrong += "you are too old"
    case age if  65 >= age >= 18:
        good += "you have the adequate age, "

match weight:
    case weight if weight < 50:
        wrong += "you don't weight enough, "
    case weight if weight >= 50:
        good += "you weight enough, "

match heartbeat:
    case heartbeat if 50 > heartbeat:
        wrong += "your heartbeat is too slow, " 
    case heartbeat if heartbeat > 110:
        wrong += "your heartbeat is too fast"
    case heartbeat if 50 <= heartbeat <= 110:
        good += "your heartbeat is adequate, "
        
match platelets:
    case platelets if 150_000 > platelets:
        wrong += "you have few platelets." 
    case platelets if 400_000 < platelets:
        wrong += "you have many platelets."
    case platelets if 400_000 >= platelets >= 150_000:
        good += "you have enough platelets; "

match wrong:
    case wrong if wrong == "":
        print(f"{good.capitalize()}you are able to donate")
    case _:
        print(f"You cannot donate because {wrong}")