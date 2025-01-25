import requests
from bs4 import BeautifulSoup

def fetch_page():
    url = "https://www.mercadolivre.com.br/caneta-brush-pen-36-cores-duas-pontas-pincel-fina-canetinha/p/MLB26260324#polycard_client=recommendations_home_second-trend-function-recommendations&reco_backend=second_trend_function&wid=MLB3933122535&reco_client=home_second-trend-function-recommendations&reco_item_pos=2&reco_backend_type=function&reco_id=b86df75a-cb71-47da-886d-2dbf700d24f4&sid=recos&c_id=/home/second-trend-recommendations/element&c_uid=ce40d716-cf9d-43ab-ba11-80cc1345d4ed"
    response = requests.get(url)
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_="ui-pdp-title").get_text()
    prices: list = soup.find_all('span', class_='andes-money-amount__fraction')
    old_price: int = int(prices[0].get_text().replace('.', ''))
    new_price: int = int(prices[1].get_text().replace('.', ''))
    installment_price: int = int(prices[2].get_text().replace('.', ''))
    
    return {
        'product_name': product_name,
        'old_price': old_price,
        'new_price': new_price,
        'installment_price': installment_price

    }

if __name__ == "__main__":
    page_content = fetch_page()
    produto_info = parse_page(page_content)
    print(produto_info)