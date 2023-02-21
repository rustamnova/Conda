import openai

# Use the API key
openai.api_key = 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

# The prompt
prompt = "What is GPT-3"

# Generate a response
response = openai.Completion.create(engine="text-davinci-002", prompt=prompt)

# Print the response
print(response["choices"][0]["text"])
