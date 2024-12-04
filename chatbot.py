# Importing required libraries for the chatbot
import getpass # to get pc username
import random # for random greeting and random joke

# cool ASCII ART from http://patorjk.com/software/taag/#p=testall&f=Broadway%20KB&t=HOPE%20CHATBOT
print("""
┓┏┏┓┏┓┏┓  ┏┓┓┏┏┓┏┳┓┳┓┏┓┏┳┓
┣┫┃┃┃┃┣   ┃ ┣┫┣┫ ┃ ┣┫┃┃ ┃ 
┛┗┗┛┣┛┗┛  ┗┛┛┗┛┗ ┻ ┻┛┗┛ ┻                     
""")

# get pc username, link it to the variable username
username = getpass.getuser()

# creating chatbot function
def chatbot():

    # creating a list for a selection of greetings
    greeting = ["What can I do for you?", "How may I help you today?", "How is it going?", "How are you doing?",
                "Anything I can help with?", ]

    # greeting the user with a random greeting message chosen from the list above
    print(f"Hello {username}! {random.choice(greeting)} ")

    # loop
    while True:
        # List of jokes
        jokes = ["Why don’t eggs tell jokes? \n Because they’d crack each other up!",
                 "What do you call fake spaghetti? \n An impasta!",
                 "Why did the bicycle fall over? \n Because it was two-tired!",
                 "Why don’t scientists trust atoms? \n Because they make up everything! ",
                 "Why was the computer cold? \n Because it left its Windows open!", ]
        # get user input here
        user_input = input().lower()  # .lower for error handling

        # possible chats and responds
        if user_input == 'exit':
            print("HopeGPT: Goodbye!")
            break
        elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print("HopeGPT: Hi there! How can I help you?")
        elif "how are you" in user_input or "how are u" in user_input:
            print("HopeGPT: I'm good. How are you? ")
        elif "im fine" in user_input or "I'm good" in user_input or "im alright" in user_input or "fine" in user_input or "alright" in user_input or "im good" in user_input:
            print("HopeGPT: Cool! ")
        elif "your name" in user_input or "ur name" in user_input:
            print("HopeGPT: My name is HopeGPT. What's your name?")
        elif "my name is" in user_input:
            print("Nice to meet you!")
        elif "who created you" in user_input:
            print("This chatbot is created by Marky (Anonymous).")
        elif "a joke" in user_input:
            print(f"Here is a joke for you! \n {random.choice(jokes)} ")
        elif "haha" in user_input:
            print("Funny right!")
        else:  # Unexpected user inputs here
            print("HopeGPT: I'm not sure how to respond to that.")


chatbot() #execute
