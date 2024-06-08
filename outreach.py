import requests

def generate_outreach_message(summary):
    url = "http://localhost:11434/api/generate"
    prompt = (
        f": As a sales executive conducting LinkedIn cold outreach on behalf of [], your goal is to initiate meaningful "
        f"conversations with potential prospects. Once you have the summary, your task is to craft a personalized message "
        f"that resonates with the target and prompts them to engage further. Now here is the summary: {summary}"
    )
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
