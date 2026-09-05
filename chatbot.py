while True:
    user_input=input("YOU:").lower().strip()


    if user_input in["hi","hello","hey"]:
        print("Bot:Hello! How can i help you?")
    elif user_input in["Bye","Exit","Quit"]:
        print("Bot:Goodbye!")
        break
    elif"how are you" in user_input:
        print("Bot:I am just a Bot,but I am doing great!")
    elif "your name"in user_input:
        print("Bot:I am a rule based chatbox.")
    else:
        print("Bot:Sorry,I did'nt understand that")
