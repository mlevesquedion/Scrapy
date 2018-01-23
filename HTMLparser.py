from bs4 import BeautifulSoup


class HTMLparser:

    def __init__(self):
        self.soup = None

    def is_set(self):
        return self.soup is not None

    def set_html(self, html):
        self.soup = BeautifulSoup(html, 'html5lib')

    def get_pattern_matches(self, pattern):
        return self.soup.select(pattern)

    def get_available_tags(self):
        return sorted({tag.name for tag in self.soup.findAll()})
