while True:
    user = input("you:")
    if user.upper() in ["BYE","EXIT","QUIT"]:
        print("bot:goodbye!")
        break
    if user.lower() in ["hi","good morning"]:
        print("bot:hello!")
    if user.lower() in ["how are you"]:
        print("bot:fine,what about you!")
    if user.lower() in ["how is your studies going"]:
        print("bot:going good!")
    if user.upper() in ["BYE"]:
        print("bot:goodbye!")
    
        