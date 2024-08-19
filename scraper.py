import requests
from bs4 import BeautifulSoup

def get_lenovo_laptops():
    url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    laptops = []
    for item in soup.select('.thumbnail'):
        title = item.select_one('.title').text
        if 'Lenovo' in title:
            price = float(item.select_one('.price').text.replace('$', ''))
            description = item.select_one('.description').text
            laptops.append({'title': title, 'price': price, 'description': description})

    return sorted(laptops, key=lambda x: x['price'])

if __name__ == '__main__':
    laptops = get_lenovo_laptops()
    for laptop in laptops:
        print(laptop)
