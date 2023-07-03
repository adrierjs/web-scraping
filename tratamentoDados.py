from bs4 import BeautifulSoup
from integrationAPI import data_site

soup = BeautifulSoup(data_site, 'html.parser')
tr_elements = soup.find_all('tr')
data_convertidos = []

for row in tr_elements[1:]:
    td_elements = row.find_all('td')

    name = td_elements[2].find('a', class_='b').text.strip()
    discount_percentage = td_elements[3].text.strip()
    price_element = td_elements[4]
    if price_element:
        price = price_element.text.strip()
    rating_element = td_elements[5]
    if rating_element:
        rating = rating_element.text.strip()
    if 'title' in td_elements[6].attrs:
        ends_in = td_elements[6]['title']
    if 'title' in td_elements[7].attrs:
        started = td_elements[7]['title']
    release = (td_elements[8] if td_elements else '').text.strip()

    data_convertidos.append({
        'name': name,
        'discount_percentage': discount_percentage,
        'price': price,
        'rating': rating,
        'ends_in': ends_in,
        'started': started,
        'release': release
    })


