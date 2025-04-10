from typing import Tuple, Dict
import dotenv
import os
from dotenv import load_dotenv
import requests as rq
import json
import streamlit as st

## Load Exchange API Key and API Url from environment file
load_dotenv()
EXCHANGERATE_API_KEY = os.getenv('EXCHANGERATE_API_KEY')
URL_API = os.getenv('API_URL')


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
        completion = ...
    except Exception as e:
        print(f"Exception {e} for {text}")
    else:
        return completion

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
    st.write("You entered: ", user_input)