print(" Welcome to Simple Rule-Based Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! How can I help you?")
    elif user == "how are you":
        print("Bot: I am fine. Thank you!")
    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")
    elif user == "what is python":
        print("Bot: Python is a popular programming language.")
    elif user == "help":
        print("Bot: You can ask me about AI, Python, or greet me.")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand that.")