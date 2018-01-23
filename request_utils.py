from requests import get


class InvalidURL(Exception):

    def __init__(self):
        super().__init__()
        self.message = 'The specified URL is invalid.'


def complete(url):
    http_prefix = 'http://'
    www_prefix = 'www.'
    com_suffix = '.com'
    if www_prefix not in url:
        url = www_prefix + url
    if http_prefix not in url:
        url = http_prefix + url
    if '.' not in url[url.index('www.') + 4:]:
        url += com_suffix
    return url


def validate(url):
    if url.count('.') < 2 or not url.startswith('http://www.'):
        raise InvalidURL


def make_valid(url):
    url = complete(url)
    validate(url)
    return url


def get_page(url):
    url = make_valid(url)
    page = get(url)
    page.raise_for_status()
    return page


def get_page_text(url):
    return get_page(url).text
