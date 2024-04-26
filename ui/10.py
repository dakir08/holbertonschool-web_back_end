import gradio as gr
import random

# Define the different states of the chatbot
state = "initial"
game_mode = None
target_number = 0
guess_count = 0

def start_game(max_num):
    global target_number, guess_count
    target_number = random.randint(1, max_num)
    guess_count = 0
    return f"Okay, guess a number between 1 and {max_num}."

def bot_guess_game(max_num):
    global state, game_mode, guess_count, target_number

    target_number = random.randint(1, max_num)
    guess_count = 0
    return f"I will guess a number between 1 and {max_num}. Is it {target_number}?"

def handle_bot_guess_response(message):
    global state, game_mode, guess_count, target_number

    if message in ['yes', 'y']:
        state = "initial"
        game_mode = None
        return "Great! I guessed correctly. Come back later if you want to play again."
    elif message in ['no', 'n']:
        state = "initial"
        game_mode = None
        return "Ahh, hopefully I will have better luck next time! Come back later if you want to play again."
    else:
        return "I'm sorry, I didn't understand that. Did I guess the correct number, yes or no?"

def chatbot_response(message):
    global state, game_mode, guess_count, target_number

    message = message.lower().strip()

    if message in ["reset", "quit", "exit"]:
        state = "initial"
        game_mode = None
        return "Ok, come back later if you want to play Guess the number with me."

    if state == "initial":
        if message == "":
            return ""
        else:
            state = "awaiting_play_confirmation"
            return "Hi, do you want to play Guess the number with me?"

    if state == "awaiting_play_confirmation":
        if message in ["yes", "y"]:
            state = "choosing_game_mode"
            return "You or I can guess the number, did you want to be the one guessing?"
        elif message in ["no", "n"]:
            state = "initial"
            return "Ok, come back later if you want to play Guess the number with me."
        else:
            state = "awaiting_play_confirmation_error"
            return "I’m sorry, I didn’t understand that. Do you want to play Guess the number with me, yes or no?"

    if state == "awaiting_play_confirmation_error":
        state = "initial"
        return "I guess we don’t understand each other, bye for now."

    if state == "choosing_game_mode":
        if message in ["yes", "y"]:
            game_mode = "user_guesses"
            state = "setting_max_number"
            return "Ok you guess the number. What is the maximum number we will guess up to?"
        elif message in ["no", "n"]:
            game_mode = "bot_guesses"
            state = "setting_max_number"
            return "Ok I will guess. What is the maximum number we will guess up to?"
        else:
            state = "choosing_game_mode_error"
            return "I'm sorry, I didn't understand that, do you want to be the one guessing, yes or no?"

    if state == "choosing_game_mode_error":
        if message in ["yes", "y"]:
            game_mode = "user_guesses"
            state = "setting_max_number"
            return "Ok you guess the number. What is the maximum number we will guess up to?"
        elif message in ["no", "n"]:
            game_mode = "bot_guesses"
            state = "setting_max_number"
        state = "initial"
        return "I guess we don’t understand each other, bye for now."

    if state == "setting_max_number":
        try:
            max_num = int(message)
            if max_num < 2:
                raise ValueError("Number must be greater than 2")
            if game_mode == "user_guesses":
                state = "user_guessing"
                return start_game(max_num)
            elif game_mode == "bot_guesses":
                state = "bot_guessing"
                return bot_guess_game(max_num)
        except ValueError:
            state = "setting_max_number_error"
            return "I'm sorry I didn’t understand that. Please let me know a round number greater than 2."

    if state == "setting_max_number_error":
        state = "initial"
        return "I guess we don’t understand each other, bye for now."

    if state == "user_guessing":
        try:
            guess = int(message)
            if guess < target_number:
                return "Too low! Guess again:"
            elif guess > target_number:
                return "Too high! Guess again:"
            else:
                state = "initial"
                return f"You guessed correct! Come back later if you want to play again."
        except ValueError:
            return "I'm sorry I didn’t understand that. Please let me know what round number is your guess."

    if state == "bot_guessing":
        return handle_bot_guess_response(message)

def reset():
    global state, game_mode
    state = "initial"
    game_mode = None
    return "Game reset. Let's start over!"

iface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    allow_flagging="never",
    title="Guess the Number Chatbot",
    description="Play 'Guess the Number' with me! Type 'reset' anytime to start over or 'quit' to exit.",
    theme="huggingface"
)

iface.launch()
