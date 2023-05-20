  
"""/*MIT License

Copyright (c) 2023 Vivek Verma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/"""


import openai
import os
import time

# Set up the OpenAI API credentials
openai.api_key = "Enter Your API Key"
"""
 AI Engine: text-davinci-003 :-> fastest one
 max_token size: the response buffer for the input string.
 temprature can range between 0.1 to 0.8

"""


# Define the chatbot function
def chatbot(input_message):
    response = openai.Completion.create(
        #engine="text-davinci-003",
        engine="text-davinci-003",
        prompt=input_message,
        max_tokens=50,
        n=4,
        stop=None,
        temperature=0.2,
    )
    return response.choices[0].text.strip()



# Get the discussion topic from the user
topic = input("Enter the discussion topic: ")

# Initialize chatbots
bot1_message = "Hello President_Vladimir_Putin"
bot2_message = "Hello President_Volodymyr_Zelenskyy"

# Start the conversation loop
while True:
    # Chatbot 1 responds to the user or chatbot 2
    boot1_input = f"Volodymyr_Zelenskyy: {bot2_message}" if bot2_message else f"Volodymyr_Zelenskyy: {topic}"
    bot1_message = chatbot(boot1_input)
    print(f"Volodymyr_Zelenskyy: {bot1_message}")

    # Chatbot 2 responds to chatbot 1
    boot2_input = f"Vladimir_Putin: {bot1_message}"
    bot2_message = chatbot(boot2_input)
    print(f"Vladimir_Putin: {bot2_message}")

    # Check if the conversation has ended
    if " Goodbye" in bot1_message or "Goodbye" in bot2_message:
        break
