from openai import OpenAI
import sys
import os
from pyfiglet import Figlet
from termcolor import colored

# Initialize the OpenAI client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="Your Api Key Here"
)

# Function to clear the terminal
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the chatbot header in cool ASCII art
def print_header():
    f = Figlet(font='slant')
    print(colored(f.renderText('ChatBot'), 'cyan'))

# Function to handle the chat interaction
def chat_with_ai():
    clear_console()
    print_header()  # Display the header
    
    print(colored("Welcome to ChatBot! Type your questions below.\n", 'green'))
    print(colored("(Press space and Enter to exit)\n", 'yellow'))

    while True:
        # Get user input
        user_input = input(colored("You: ", 'blue'))

        # Exit the loop if the user presses the space key
        if user_input.strip() == "":
            print(colored("\nExiting... Goodbye!", 'red'))
            break

        # Create a completion request to the AI
        completion = client.chat.completions.create(
            model="nvidia/llama-3.1-nemotron-70b-instruct",
            messages=[{"role": "user", "content": user_input}],
            temperature=0.5,
            top_p=1,
            max_tokens=1024,
            stream=True
        )

        # Output the response in real-time as the chunks arrive
        print(colored("\nAI's response:", 'cyan'))
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                sys.stdout.write(colored(chunk.choices[0].delta.content, 'yellow'))
                sys.stdout.flush()
        print("\n")  # Add a newline after the response for better readability

if __name__ == "__main__":
    try:
        from pyfiglet import Figlet
        from termcolor import colored
    except ImportError:
        print("Required packages are missing! Install them using:")
        print("pip install pyfiglet termcolor")
    else:
        chat_with_ai()









