import sys
import openai
import os
from dotenv import load_dotenv
from colorama import Fore, Back, Style

load_dotenv()  # load environment variables from .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

# define prompts
prompt = [
    "Tell me about yourself.",
    "What are your hobbies?",
    "Why do you want to work for our company?",
    "What are your strengths?",
    "What are your weaknesses?",
    "What are your salary expectations?",
    "What are your career goals?",
    "What are your long-term goals?",
    "What are your short-term goals?",
    "Do you have any questions for me?",
    "Why should we hire you?",
    "What are your greatest achievements?",
]


def generate_response(prompt, chat_history=None):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        # Temperature is the randomness of the model.
        temperature=0.7,
        # The higher the temperature, the more random the text.
        # The lower the temperature, the less random the text.
        # 0.9 is the default value.
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    message = response.choices[0].text.strip()
    if chat_history is not None:
        chat_history.append((prompt, message))
    return message

def start_chat():
    print("Welcome to the Job Interview Chatbot!")
    while True:
        chat_history = []
        # Get user input
        user_input = input(Fore.GREEN + Style.BRIGHT + "You: " + Style.RESET_ALL).strip()
        # Exit if user types "exit"
        if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
            print(Fore.RED + Style.BRIGHT + "Bot: Bye!")
            break
        # prompt = f"User: {user_input}\nBot: "
        prompt = user_input
        # Generate response
        response = generate_response(prompt, chat_history)
        print(Fore.CYAN + Style.BRIGHT + "Bot: " + Style.NORMAL + response)

start_chat()