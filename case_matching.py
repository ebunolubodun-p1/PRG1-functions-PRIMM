day = input("enter day ")

match day:
    case "monday":
        print("start")
    case "saturday" | "sunday":
        print("weekend")
    case _ :
        print("no")