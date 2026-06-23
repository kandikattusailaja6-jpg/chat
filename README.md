This program implements a simple rule-based chatbot using Python.
The chatbot_response() function processes the user's input.
User input is converted to lowercase using lower() for easy comparison.
The strip() method removes extra spaces from the input.
A dictionary named responses stores predefined questions and answers.
Common greetings like "hello" and "hi" have corresponding responses.
The program checks whether any key in the dictionary matches the user's input.
A for loop is used to search through all predefined keywords.
If a match is found, the corresponding response is returned.
If no match is found, a default message is displayed.
The if __name__ == "__main__": statement starts the main program execution.
The chatbot greets the user when the program begins.
A while True loop allows continuous conversation with the user.
When the user enters "bye", the chatbot exits the loop and terminates.
This chatbot demonstrates basic Natural Language Processing (NLP) concepts using simple keyword matching techniques.
