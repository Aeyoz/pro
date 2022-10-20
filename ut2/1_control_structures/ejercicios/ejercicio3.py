country = int(input('''Please enter the number related to your country: 
1. España 
2. Italia
3. Portugal
4. North Korea
5. USA
6. México	
7. Japan
8. China
9. India
'''))

match country:
    case 1:
        print("ES")
    case 2:
        print("IT")
    case 3:
        print("PT")
    case 4:
        print("KP")
    case 5:
        print("US")
    case 6:
        print("MX")
    case 7:
        print("JP")
    case 8:
        print("CN")
    case 9:
        print("IN")
    case _:
        print("Error")