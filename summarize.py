import requests

def summarize_text_with_mistral(text):
    url = "http://localhost:11434/api/generate"
    prompt = f"Estrai le informazioni rilevanti dal seguente testo estratto dal sito web di un potenziale cliente, e scrivi come risposta un documento di profilazione altamente dettagliato da mandare al reparto sales, ecco il testo del sito web: {text}"
    payload = {
        "model": "llama3:latest",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "seed": 20,
            "top_k": 40,
            "top_p": 0.9,
            "repeat_penalty": 1.1,
            "mirostat": 1,
            "mirostat_eta": 0.1,
            "mirostat_tau": 5.0,
            "num_ctx": 4096,
            "repeat_last_n": 64
        }
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
