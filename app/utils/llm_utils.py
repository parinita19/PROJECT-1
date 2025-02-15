import os
import requests
from app.config import AIPROXY_TOKEN

# Hypothetical LLM API endpoint; replace with your actual endpoint.
LLM_API_URL = "https://aiproxy.sanand.workers.dev/openai/"

def call_llm_api(prompt: str) -> str:
    """
    Call the LLM API with the given prompt and return the generated text.
    This function uses the AIPROXY_TOKEN from the environment for authentication.
    """
    headers = {
        "Authorization": f"Bearer {AIPROXY_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o-mini",  # Use the specified model
        "prompt": prompt,
        "max_tokens": 50,        # Adjust token limit as needed
        "temperature": 0.3       # Adjust for creativity vs. determinism
    }
    
    response = requests.post(LLM_API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"LLM API request failed: {response.status_code}, {response.text}")
    
    # Assuming the API returns a JSON with a structure similar to OpenAI's API:
    result = response.json()
    # Get the generated text from the first choice.
    return result.get("choices", [{}])[0].get("text", "").strip()

def extract_email(text: str) -> str:
    """
    Use the LLM to extract an email address from the provided text.
    """
    prompt = f"Extract the sender's email address from the following text:\n\n{text}\n\nReturn only the email address."
    return call_llm_api(prompt)

def extract_credit_card(text: str) -> str:
    """
    Use the LLM to extract a credit card number from the provided text.
    Ensure the output contains only digits with no spaces.
    """
    prompt = f"Extract the credit card number from the following text. Return only the number with no spaces or dashes:\n\n{text}"
    return call_llm_api(prompt)