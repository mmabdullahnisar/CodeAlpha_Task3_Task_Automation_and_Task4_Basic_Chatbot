def get_reply(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"
    elif message in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How are you?"
    elif message in ["i am fine", "i'm fine", "fine", "good"]:
        return "That is good to hear."
    elif message in ["what is your name", "what is your name?"]:
        return "My name is Python Chatbot."
    elif message in ["thank you", "thanks"]:
        return "You're welcome!"
    elif message in ["bye", "goodbye", "exit"]:
        return "Goodbye!"
    else:
        return "Sorry, I do not understand that."

print("Basic Chatbot")
print("You can type hello, how are you, what is your name, thanks, or bye.")

while True:
    user_message = input("\nYou: ")
    bot_reply = get_reply(user_message)
    print("Bot:", bot_reply)

    if user_message.lower().strip() in ["bye", "goodbye", "exit"]:
        break
