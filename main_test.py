"""
Вам дан шаблон main.py, в шаблоне объявлены две функции "parse_parameters" и "parse_cookies" (шаблоны).
Необходимо реализовать функционал данных функций и написать по 10 тестов к каждой из функций, в шаблоне,
в качестве примера, уже написано по два теста на каждую функцию.


Функция "parse_parameters" должна принимать строку запроса и извлекать (парсить) из нее переданные параметры, результат
 возвращать в виде словаря


Функция "parse_cookies" должна принимать строку куков и извлекать (парсить) из нее куки,
результат возвращать в виде словаря
"""

from bs4 import BeautifulSoup
import requests

URL = 'https://telemart.ua/processor/intel/'
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0',
           'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


# def get_page_count(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     pagenation = soup.findAll('a', class_='b-cat-loadmore-link load_more')


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_ = 'b-i-product-inner-b')

    procc = []
    for item in items:
        procc.append({
            'title': item.find('div', class_= 'b-i-product-name').get_text(strip=True),
            'link': item.find('div', class_='b-i-product-name').get_text(strip=True),
            'price': item.find('div', class_='b-price').get_text(strip=True)
        })
    print(procc)
    print(len(procc))
    return procc
    # print(items)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        # page_count = get_page_count(html.text)
        procc = get_content(html.text)
    else:
        print('Ops')
# parse() #Запуск тестового парсера



from urllib import parse
from http.cookies import SimpleCookie

def parse_parameters(url):
    r = dict(parse.parse_qsl(parse.urlsplit(url).query))
    return r

def parse_cookies(storage):
    cookies = SimpleCookie()
    cookies.load(storage)
    d_cookies = {}
    for key, st_cookie in cookies.items():
        d_cookies[key] = st_cookie.values()
    return d_cookies


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}

    assert parse_parameters('https://www.youtube.com/watch?v=5qap5aO4i9A') == {'v' : '5qap5aO4i9A'}
    assert parse_parameters('https://mail.google.com/mail/u/0/?tab=rm#inbox') == {'tab' : 'rm'}
    assert parse_parameters('https://example.com/path/to/page?name=josh&age=22') == {'name':'josh', 'age': '22'}
    assert parse_parameters('https://example.com/path/to/page?character=nonproud&name=Irina') == {'character': 'nonproud',
                                                                                                  'name': 'Irina'}

    assert parse_parameters('http://httpbin.com/page/?input=15&output=24') == {'input': '15', 'output': '24'}
    assert parse_parameters('http://swap-file.com/path/to/page?file=plshelpmeforthishw&count=404') =={
        'file': 'plshelpmeforthishw',
        'count': '404'
    }
    assert parse_parameters('http://googlemaps.com/page/?country=Texas&city=Odessa') == {
        'country' : 'Texas',
        'city' : 'Odessa'
    }
    assert parse_parameters('https://telemart.ua/page/as/prod?proccessor=intel&model=i5') == {
        'proccessor':'intel',
        'model':'i5'
    }

    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
    assert parse_cookies('v=5qap5aO4i9A;') == {'v': '5qap5aO4i9A'}
    assert parse_cookies('tab=rm;') == {'tab': 'rm'}
    assert parse_cookies('name=josh;age=22') == {'name':'josh',
                                                 'age': '22'}
    assert parse_cookies('character=nonproud;name=Irina') == {'character': 'nonproud',
                                                              'name':'Irina'}
    assert parse_cookies('input=15;output=24') == {'input':'15', 'output':'24'}
    assert parse_cookies('file=plshelpmeforthishw;count=404') == {'file':'plshelpmeforthishw', 'count':'404'}
    assert parse_cookies('country=Texas;city=Odessa') == {'country':'Texas', 'city':'Odessa'}
    assert parse_cookies('proccessor=intel;model=i5') == {'proccessor':'intel', 'model':'i5'}