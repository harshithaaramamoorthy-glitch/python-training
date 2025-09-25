while True:
    user = input("you:")
    if user.upper() in ["BYE","EXIT","QUIT"]:
        print("bot:goodbye!")
        break
    else:
        print("bot:you said->",user)
        