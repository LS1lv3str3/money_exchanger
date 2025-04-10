from typing import Tuple, Dict
import dotenv
import os
from dotenv import load_dotenv
import requests as rq
import json
import streamlit as st
from openai import OpenAI

## Load Exchange API Key and API Url from environment file
load_dotenv()
EXCHANGERATE_API_KEY = os.getenv('EXCHANGERATE_API_KEY')
URL_API = os.getenv('API_URL')

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)


def get_exchange_rate(base: str, target: str, amount: str) -> Tuple:
    """Return a tuple of (base, target, amount, conversion_result (2 decimal places))"""
   
    url = f"{URL_API}/{EXCHANGERATE_API_KEY}/pair/{base}/{target}/{amount}"

    response = json.loads(rq.get(url).text)
    conversion_result = round(response['conversion_result'], 2)

    return (base, target, amount, conversion_result)
    

def call_llm(textbox_input) -> Dict:
    """Make a call to the LLM with the textbox_input as the prompt.
       The output from the LLM should be a JSON (dict) with the base, amount and target"""
    try:
        response = client.chat.completions.create(
            messages=[  
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": textbox_input,
                }
            ],
            temperature=1.0,
            top_p=1.0,
            max_tokens=1000,
            model=model_name
        )

    except Exception as e:
        print(f"Exception {e} for {text}")
    else:
        return response.choices[0].message.content


def run_pipeline():
    """Based on textbox_input, determine if you need to use the tools (function calling) for the LLM.
    Call get_exchange_rate(...) if necessary"""

    if True: #tool_calls
        # Update this
        st.write(f'{base} {amount} is {target} {exchange_response["conversion_result"]:.2f}')

    elif True: #tools not used
        # Update this
        st.write(f"(Function calling not used) and response from the model")
    else:
        st.write("NotImplemented")

# Set the title of the app
st.title("Multilingual Money Changer")

# Create a single text box for user input
user_input = st.text_input("Enter the ammount and the currency")

# Submit button
if st.button("Submit"):
    # Display the user input below the text box
    st.write(call_llm(user_input))