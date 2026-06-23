def chatbot_response(user_input):
    # Convert input to lowercase for easier matching
    text = user_input.lower().strip()

    # Define chatbot responses
    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! What's on your mind?",
        "how are you": "I'm just code, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a nice day!",
        "thanks": "You're welcome!"
    }

    # Check if input matches any response
    for key in responses:
        if key in text:
            return responses[key]

    # Default response
    return "Sorry! I don't understand that."


# Main Program
if __name__ == "__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() == "bye":
            print("Chatbot: Goodbye!")
            break

        response = chatbot_response(user_input)
        print("Chatbot:", response)