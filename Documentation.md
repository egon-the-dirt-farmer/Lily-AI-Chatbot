# Technical Documentation for Lily - AI Chatbot
## Introduction
Lily is a chatbot app that works in conjunction with the OpenAI GPT API developed by Franklin Media Australia Pty Ltd. It utilises the OpenAI API to generate responses to prompts typed into the GUI interface by the user. The user can enter their name so that it will appear in the chatbox with the user responses on the right of the chatbox and the bot responses on the left side of the chatbox. The app is designed as a desktop chatbot to interface with the OpenAI narrow Artificial Intelligence API.

## Requirements
In order to use Lily, you will need the following:

* API Key from OpenAI
* Python 3.x installed on your system
* Required Python libraries: openai, tkinker

## How it Works
Lily is has two basic files that you can run. Version 1.0 is a basic test of concept that can be run in the command line and will enable the user to interact with the OpenAI API in a conversational way.
Version 1.1 builds this into a simple GUI wrapper using the Tkinter Python library. The user can enter their name so that their text prompts are labelled with the name they choose. While the chosen name of the chatbot can be altered based on user choice.
The name can be changed just by changing the chatbot_name variable that is declared near the api_key variable.
The api model can also be changed by using the engine variable. Make sure you know what models are available before you change this.

## The app has the following main functions:
* generate_response() - generates a response from the OpenAi completions endpoint.
* on_submit() - submits the user response to the API when the Submit button on the GUI is pressed.


## Technical Details
* The app uses OpenAI's completion API to generate responses. 
* The app uses the text-davinci-003 engine to generate the text. 
* The app sets the maximum tokens to 1024 and temperature to 0.7 for the completion API.
* The app sets the n parameter to 1 and the stop parameter to None for the completion API.

## License
Lily is privately licensed by Franklin Media Australia Pty Ltd for non-commercial use only. You may use the software for personal or internal business purposes, but you may not distribute, sell, or use it for any commercial purpose without the express written permission of Franklin Media Australia Pty Ltd. By using New Swizard, you agree to be bound by the terms of the Franklin Media Australia Pty Ltd - Private Use Copyright License. 

Please note that this software is provided "as is" without warranty of any kind, express or implied. Franklin Media Australia Pty Ltd shall not be liable for any damages arising from the use of this software. If you have any questions or concerns about the license for New Swizard, please comment to the Franklin Media Australia programmers through their GitHub Repository.
