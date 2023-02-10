# ====================================================================================================================
# /*
# APP NAME: Lily - The AI Virtual Assistant
# APP URI: https://franklinmedia.com.au/apps/lily-chatbot
# AUTHOR: Z3r0-K3lv1n
# AUTHOR URI: https://franklinmedia.com.au/z3r0-k3lv1n
# DESCRIPTION: LILY is a chatbot written in the Python programming language that uses the Tkinter and OpenAI Python
# libraries to create a graphical user interface and interact with the OpenAI GPT3 API respectively. The Chatbot
# enables the user to enter their name and then type requests and submit them to the AI API. This simple program gives
# easy access for users to interact with the OpenAI API from a chatbox on their desktop. The code utilises the OpenAI
# API completions element and this can be edited in the code by changing the engine Variable declared at the top of the
# code beneath the prompt.
# TAGS: Chatbot, OpenAi, GPT3, DaVinci, Tkinter, GUI
# VERSION: 1.0
# LICENSE: Franklin Media Australia Pty Ltd - Private Use Copyright License
# LICENSE URI:https://www.franklinmedia.com.au/impressum-credits/website-terms-conditions/private-use-copyright-license/
# COPYRIGHT LICENSE FOR PRIVATE USE ONLY
# Sophia - The AI Virtual Assistant is privately licensed by Franklin Media Australia Pty Ltd for
# non-commercial use only. This means that you may use the software for personal or internal business purposes, but
# you may not distribute, sell, or use it for any commercial purpose without the express written permission of
# Franklin Media Australia Pty Ltd.
# By using Sophia - The AI Virtual Assistant, you agree to be bound by the terms of the Franklin
# Media Australia Pty Ltd - Private Use Copyright License. The full text of this license can be found here.
# Please note that this software is provided "as is" without warranty of any kind, express or implied. Franklin Media
# Australia Pty Ltd shall not be liable for any damages arising from the use of this software.
# If you have any questions or concerns about the license for The Basic Universal Translator - The Cunning Linguist,
# please contact Franklin Media Australia Pty Ltd at admin@franklinmedia.com.au.
# */
# ====================================================================================================================

import openai
import api_key

# Openai API Key
openai.api_key = api_key.api_key

prompt_lily = f"Lily is an AI Virtual Assistant. She is clever and witty and wanting to teach and learn as " \
              f"much as she can."
engine = "text-davinci-003"
chatbot_name = "LILY"


def generate_response(prompt):
    completions = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()


prompt_Sophia = "Lily is a Virtual Assistant AI she is clever and witty and wanting to teach and learn as " \
                "much as she can."
user_name = input(f"{chatbot_name}: Hi, I'm {chatbot_name}. What's your name? ")
name = user_name
print(f"{chatbot_name}: Nice to meet you, {name}!")

while True:
    user_input = input(f"{name}: ")
    if user_input == "exit" or user_input == "goodbye".lower():
        break
    else:
        print(f"{chatbot_name}:", generate_response(f"{prompt_Sophia} {user_input}"))
