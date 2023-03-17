import sys
import openai
import os
from dotenv import load_dotenv

load_dotenv() # load environment variables from .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        temperature = 0.6,                      # Temperature is the randomness of the model.
                                                # The higher the temperature, the more random the text.
                                                # The lower the temperature, the less random the text.
                                                # 0.9 is the default value.
        max_tokens = 1024,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0,
    )
    return response.choices[0].text.strip()

while True:
    # Get user input
    user_input = input("You: ")

    # Exit if user types "exit"
    if user_input.lower() == "exit":
        print("Bot: Bye!")
        sys.exit()
    elif user_input.lower() == "close":
        print("Bot: Closing...")
        sys.exit()
    elif user_input.lower() == "clear":
        os.system("cls")
        continue

    prompt = f"User: {user_input}\nBot: "
    # Generate response
    response = generate_response(prompt)
    # Print response
    print("Bot: ",response)
