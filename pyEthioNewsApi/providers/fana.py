from typing import Optional, Generator

from .base_scraper import BaseScraper, NewsResult, News


class FanaBc(BaseScraper):
    def __init__(self):
        super().__init__()
        self.url = "https://www.fanabc.com/"
        self.categorises = {
            "business": 55,
            "sport": 56,
        }

    def get_main_news(
            self,
            limit: int = 10,
    ) -> Generator[NewsResult, None, None]:
        url = self.url + "wp-json/wp/v2/posts" + "?per_page=" + str(limit)
        return self._fetch_news(url)

    def get_business_news(
            self,
            limit: int = 10,
    ) -> Generator[NewsResult, None, None]:
        url = self.get_url(self.categorises["business"], limit)
        return self._fetch_news(url)

    def get_sport_news(
            self,
            limit: int = 10,
    ) -> Generator[NewsResult, None, None]:
        url = self.get_url(self.categorises["sport"], limit)
        return self._fetch_news(url)

    def get_news(
            self,
            limit: int = 10,
            news: Optional[News] = News.LOCAL,
    ) -> Generator[NewsResult, None, None]:
        if news == News.LOCAL:
            return self.get_main_news(limit)

        elif news == News.WORLD_WIDE:
            return self.get_main_news(limit)

        elif news == News.BUSINESS:
            return self.get_business_news(limit)

        elif news == News.SPORT:
            return self.get_sport_news(limit)


if __name__ == '__main__':
    scraper = FanaBc()
    for news_ in scraper.get_news(limit=10):
        print(news_.title)
