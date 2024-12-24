name=input("what is your name? ")

match name:
    case "Harry" | "Hermonie" | "Ron":
        print("Grifindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")
            