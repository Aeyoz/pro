first_key = input("Introduce the fist key: ")
second_key = input("Introduce the second key: ")
third_key = input("Introduce the third key: ").capitalize()

match first_key, second_key, third_key:
    case "Ctrl", "Alt", "T":
        print("Opens terminal")
    case "Ctrl", "Alt", "L":
        print("Locks Screen")
    case "Ctrl", "Alt", "D":
        print("Shows Desktop")
    case "Ctrl", "Alt", "Arrow":
        print("Moves Between Workspaces")
    case "Ctrl", "Alt", "Del":
        print("Logs out of Sessions")
    case "Win", "", "F":
        print("Opens folder system")
    case "Win", "", "A":
        print("Opens the app executer")
    case _:
        print("Nothing")
    