#!/user/bin/python3.10
def match():
    user_input = int(input("\n\n\nenter 4 to quit\n\ngimme dat number (1-3): \n> "))
    match user_input:
        case 1:
            print("loser")
        case 2:
            print("uhhh no you")
        case 3:
            print("i mean... i guess... baka!")
        case 4:
            print("\nquitting...")
            quit()
        case _:     # this is the default structure
            print("i said between 1 and 3, IDIOT...")
    match()
match()