import requests

def generate_outreach_message(name, company, product, summary):
    url = "http://localhost:11434/api/generate"
    prompt = (
        f" Agisci come venditore a freddo esperto nel copy e nei messaggi a freddo, assisterai la seguente risorsa: **Nome del venditore**: {name} che lavora per: {company}"
        f"Il tuo compito è solo quello di scrivere messaggi di outreach a freddo al posto della risorsa che assisti, andando a vendere **Descrizione del prodotto/servizio da vendere**: {product} , impersonando un messaggio da parte di {name}"
        f"Ora ti fornirò un brief del potenziale cliente a cui dovrai scrivere il messaggio **Prospetto del cliente**: {summary}"
        f"Il messaggio deve essere scritto in italiano e deve seguire questa struttura:"
        f"- **Introduzione**: Presentati a nome del venditore e dell'azienda."
        f"- **Connessione personale**: Cita un elemento specifico dal prospetto del cliente che dimostri che hai fatto ricerche sulla loro attività."
        f"- **Proposta di valore**: Spiega brevemente come il prodotto/servizio offerto può risolvere un problema o soddisfare un bisogno specifico del cliente."
        f"- **Invito all'azione**: Concludi con un invito chiaro per il prossimo passo. Esempio: 'Sarebbe possibile organizzare una breve chiamata per esplorare questa opportunità? Fammi sapere quando sei disponibile.' {summary}"
    )
    payload = {
        "model": "llama3:latest",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "seed": 40,
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
