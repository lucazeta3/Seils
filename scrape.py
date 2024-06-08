import requests
from bs4 import BeautifulSoup

def scrape_website_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        main_text = ""
        for element in soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"]):
            main_text += element.get_text().strip() + " "
        return main_text
    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)
        return None
    except Exception as e:
        print("An error occurred while scraping the website:", e)
        return None
