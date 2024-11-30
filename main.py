import getpass
import random
import time


# cool text from http://patorjk.com/software/taag/#p=testall&f=Broadway%20KB&t=HOPE%20CHATBOT
print("""
┓┏┏┓┏┓┏┓  ┏┓┓┏┏┓┏┳┓┳┓┏┓┏┳┓
┣┫┃┃┃┃┣   ┃ ┣┫┣┫ ┃ ┣┫┃┃ ┃ 
┛┗┗┛┣┛┗┛  ┗┛┛┗┛┗ ┻ ┻┛┗┛ ┻                     
""")

# get pc username
username = getpass.getuser()


# creating a list for a selection of greetings
greeting = ["What can I do for you?", "How may I help you today?", "How is it going?", "How are you doing?" , "Anything I can help with?",]


#greeting
print(f"Hello {username}! {random.choice(greeting)} ")



#GET user input here
user_input = input()



# convert to lower case for avoiding error and with or without the ?
if user_input.lower() == "how are you?".lower() or user_input.lower() == "how are you".lower():
    print("I am good! How are you?")
# get answer
    user_input = input()
    print("Nice!")



# convert to lower case for avoiding error and with or without the ? or without '
elif user_input.lower() == "What's your name?".lower() or user_input.lower() == "What's your name".lower() or user_input.lower() == "Whats your name?".lower() or user_input.lower() == "Whats your name".lower():
    print("My name is Marky!")
    print("What's your name?")
    user_input = input()
    print(f"Nice to meet you {user_input.upper()}! ")


time.sleep(100000000)






# TAKE A LOOK
''' 
username = getpass.getuser()

# Creating a list for a selection of greetings
greeting = ["What can I do for you?", "How may I help you today?", "How is it going?", "How are you doing?", "Anything I can help with?"]

# Greet the user
print(f"Hello {username}! {random.choice(greeting)}")

# First user input
user_input = input()

# Convert to lowercase for avoiding error and checking with or without the ?
if "how are you" in user_input.lower():
    print("I am good! How are you?")
    user_input = input()  # Ask for user's next input
    print("Nice!")

# Check for "What's your name?"
elif "what's your name" in user_input.lower() or "whats your name" in user_input.lower():
    print("My name is Marky!")
    print("What's your name?")
    user_input = input()  # Ask for user's name
    print(f"Nice to meet you {user_input.upper()}!")

# Sleep indefinitely (to keep the program running)
time.sleep(100000000)
'''

















