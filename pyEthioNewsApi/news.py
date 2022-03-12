from rich.pretty import pprint

from providers import *

walta = Walta()

if __name__ == '__main__':
    walta = walta.get_news()
    for news in walta:
        pprint(news.domain)
