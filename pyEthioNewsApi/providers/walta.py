from enum import Enum
from typing import Union, Optional, Generator

from rich.traceback import install

from .base_scraper import BaseScraper, NewsResult, News

install()


class WaltaNewsType(Enum):
    NEWS = "News"
    ECONOMY = "Economy"
    POLITICS = "Politics"
    SOCIAL = "Social"


class WaltaSportNewsType(Enum):
    FOOTBALL = "Football"
    LOCAL = "Social"
    INTERNATIONAL = "International"


class Walta(BaseScraper):
    def __init__(self):
        super().__init__()
        self.url = 'https://waltainfo.com/'
        self.categorises = {
            "local": {
                WaltaNewsType.NEWS.value: 158,
                WaltaNewsType.ECONOMY.value: 162,
                WaltaNewsType.POLITICS.value: 160,
                WaltaNewsType.SOCIAL.value: 158
            },
            "africa": {
                WaltaNewsType.NEWS.value: 167,
                WaltaNewsType.ECONOMY.value: 169,
                WaltaNewsType.POLITICS.value: 171,
                WaltaNewsType.SOCIAL.value: 173
            },
            "world": {
                WaltaNewsType.NEWS.value: 177,
                WaltaNewsType.ECONOMY.value: 179,
                WaltaNewsType.POLITICS.value: 181,
                WaltaNewsType.SOCIAL.value: 183
            },
            "sport": {
                WaltaSportNewsType.FOOTBALL.value: 199,
                WaltaSportNewsType.LOCAL.value: 352,
                WaltaSportNewsType.INTERNATIONAL.value: 350
            }

        }

    def get_local_news(
            self,
            limit: int = 10,
            type_: Optional[WaltaNewsType] = WaltaNewsType.NEWS
    ) -> Generator[NewsResult, None, None]:
        url = self.get_url(self.categorises["local"][type_.value], limit)
        return self._fetch_news(url)

    def get_africa_news(
            self,
            limit: int = 10,
            type_: Optional[WaltaNewsType] = WaltaNewsType.NEWS
    ) -> Generator[NewsResult, None, None]:
        url = self.get_url(self.categorises["africa"][type_.value], limit)
        return self._fetch_news(url)

    def get_world_wide_news(
            self,
            limit: int = 10,
            type_: Optional[WaltaNewsType] = WaltaNewsType.NEWS
    ) -> Generator[NewsResult, None, None]:
        url = self.get_url(self.categorises["world"][type_.value], limit)
        return self._fetch_news(url)

    def get_sport_news(
            self,
            limit: int = 10,
            type_: Optional[WaltaSportNewsType] = WaltaSportNewsType.FOOTBALL
    ) -> Generator[NewsResult, None, None]:
        url = self.get_url(self.categorises["sport"][type_.value], limit)
        return self._fetch_news(url)

    def get_business_news(self, limit: int = 10) -> Generator[NewsResult, None, None]:
        url = self.url + "wp-json/wp/v2/posts?categories=303" + "&per_page=" + str(limit)
        return self._fetch_news(url)

    def get_news(
            self,
            type_: Optional[Union[WaltaNewsType, WaltaSportNewsType]] = None,
            limit: int = 10,
            news: Optional[News] = News.LOCAL,
    ) -> Generator[NewsResult, None, None]:
        if type_ is None:
            type_ = WaltaNewsType.NEWS

        if news == News.LOCAL:
            return self.get_local_news(limit, type_)

        elif news == News.WORLD_WIDE:
            return self.get_world_wide_news(limit, type_)

        elif news == News.BUSINESS:
            return self.get_business_news(limit)

        elif news == News.SPORT:
            if not type_ or not isinstance(type_, WaltaSportNewsType):
                type_ = WaltaSportNewsType.FOOTBALL
            return self.get_sport_news(limit, type_)


if __name__ == '__main__':
    walta = Walta()
    for news_ in walta.get_news(
            news=News.WORLD_WIDE,
    ):
        print(news_.title)
