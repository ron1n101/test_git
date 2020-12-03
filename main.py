def parse_parameters(query: str) -> dict:
    return {}


def parse_cookies(query: str) -> dict:
    return {}


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}

    assert parse_parameters('https://www.youtube.com/')
    assert parse_parameters('https://www.youtube.com/watch?v=7T4yfmJBBGc') == {'name': 'Test', 'color': 'red'}


    # # Tests for function "parse_cookies"
    # assert parse_cookies('') == {}
    # assert parse_cookies('name=Dima;') == {'name': 'Dima'}
