from bs4 import BeautifulSoup
from integrationAPI import data_site
from datetime import datetime

def treating_data():
    soup = BeautifulSoup(data_site, 'html.parser')
    tr_elements = soup.find_all('tr')
    converted_data = []

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
        if 'data-sort' in td_elements[6].attrs:
            ends_in = td_elements[6]['data-sort']
            ends_in = datetime.fromtimestamp(int(ends_in)).strftime('%Y-%m-%d %H:%M:%S')
        if 'data-sort' in td_elements[7].attrs:
            started = (td_elements[7]['data-sort'])
            started = datetime.fromtimestamp(int(started)).strftime('%Y-%m-%d %H:%M:%S')
        if 'data-sort' in td_elements[8].attrs:
            release = td_elements[8]['data-sort']
            release = datetime.fromtimestamp(int(release)).strftime('%Y-%m-%d %H:%M:%S')

        converted_data.append({
            'name': name,
            'discount_percentage': discount_percentage,
            'price': price,
            'rating': rating,
            'ends_in': ends_in,
            'started': started,
            'release': release
        })
        return converted_data

converted_data = treating_data()
