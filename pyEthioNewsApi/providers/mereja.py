from typing import Generator

from fake_useragent import UserAgent

from .base_scraper import BaseScraper, NewsResult


class Mereja(BaseScraper):
    def __init__(self):
        super().__init__()
        self.ua = UserAgent()
        self.url = 'https://www.merega.com/'

    def get_news(
            self,
            limit: int = 10,
    ) -> Generator[NewsResult, None, None]:
        url = "http://mereja.com/amharic/v2/wp-json/wp/v2/posts" + "?per_page=" + str(limit)
        return self._fetch_news(url)


if __name__ == '__main__':
    mereja = Mereja()
    for news in mereja.get_news(limit=10):
        print(news.title)
