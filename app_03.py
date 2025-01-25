import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def fetch_page():
    url = "https://produto.mercadolivre.com.br/MLB-3660895165-console-playstation-5-midia-fisica-slim-branco-1tb-returnal-e-ratchet-e-clank-controle-sem-fio-dualsense-branco-_JM#polycard_client=search-nordic&position=9&search_layout=grid&type=item&tracking_id=f6746c2e-3808-4d2f-95bf-33494485f26e"
    response = requests.get(url)
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_="ui-pdp-title").get_text()
    prices =  soup.find_all('span', class_='andes-money-amount__fraction')
    old_price = int(prices[0].get_text().replace('.', ''))
    new_price = int(prices[1].get_text().replace('.', ''))
    installment_price = int(prices[2].get_text().replace('.', ''))
    
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    return {
        'product_name': product_name,
        'old_price': old_price,
        'new_price': new_price,
        'installment_price': installment_price,
        'timestamp': timestamp
    }

def save_to_dataframe(product_info, df):
    new_row = pd.DataFrame([produto_info])
    df = pd.concat([df, new_row], ignore_index=True)
    return df

if __name__ == "__main__":

    df = pd.DataFrame()

    while True:
        page_content = fetch_page()
        produto_info = parse_page(page_content)
        df = save_to_dataframe(produto_info, df)
        print(df)
        time.sleep(10)