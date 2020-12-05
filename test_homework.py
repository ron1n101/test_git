"""

"""



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