import openai

# Use the API key
openai.api_key = "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"

# Start the conversation
print("Welcome to the AI dialogue mode! Type 'exit' to end the conversation.")

# Initialize the conversation context
conversation_context = ""

while True:
    # Get the user's input
    prompt = input("You: ")

    # Check if the user wants to exit
    if prompt.lower() == "exit":
        break

    # Add the user's input to the conversation context
    conversation_context += prompt + " "

    # Generate a response
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=10, n=1)
    # Print the response
    print("AI: ",response["choices"][0]["text"])
