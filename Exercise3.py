
month=int(input("Enter month: "))

match(month):
    case 1 | 3 | 5 | 7 | 8 | 10 :
        print("31")
    case 2:
        print("28|29")
    case 4 | 6 | 9 | 11 :
        print("30")
    case _:
        print("Wrong")
