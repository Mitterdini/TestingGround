#!/user/bin/python3.10

user_input = input("gimme dat number (1-3): \n> ")
match user_input:
    case 1:
        print("loser")
    case 2:
        print("uhhh no you")
    case 3:
        print("i mean... i guess... baka!")
    case _:     # this is the default structure
        print("i said between 1 and 3, IDIOT...")