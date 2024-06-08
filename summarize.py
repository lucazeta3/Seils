import requests

def summarize_text_with_mistral(text):
    url = "http://localhost:11434/api/generate"
    prompt = f"Summarize the following text: {text}"
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "response" in data:
            return data["response"]
        else:
            print("Error: No response found in the API response.")
            return None
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None
