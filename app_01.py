import requests


def fetch_page():
    url = "https://www.mercadolivre.com.br/playstation-5-pro-playstation-5-pro-sony-2024/p/MLB43432698#polycard_client=search-nordic&searchVariation=MLB43432698&wid=MLB3939468229&position=5&search_layout=grid&type=product&tracking_id=cec2a4be-9a4e-48a5-aa2c-c5491822e1be&sid=search"
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    page_content = fetch_page()
    print(page_content)