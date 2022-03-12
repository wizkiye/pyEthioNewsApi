import datetime
import html
import re
from enum import Enum
from typing import Union, Generator, Dict, Any, Optional

import httpx
import requests
import ujson as json
from bs4 import BeautifulSoup


class News(Enum):
    LOCAL = "Local"
    WORLD_WIDE = "World"
    BUSINESS = "Business"
    SPORT = "Sport"


class NewsResult:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.id_ = data["id"]
        self.date = data["date"]
        self.slug = data['slug']
        self.modified = data["modified"]
        self.domain = re.findall(r"^(?:https|http):\/\/(.*.com)\/", data['link'])[0]
        self.url = data["link"]
        self.title = data["title"]['rendered']
        self.content = data["content"]['rendered']
        self.excerpt = data["excerpt"]['rendered']
        self.author = data.get("author") if not data.get("pwapp_author") else data.get("pwapp_author")
        self.categories = data["categories"]
        self.tags = data["tags"]
        self.comment_status = data["comment_status"]
        self.format = data["format"]
        self.status = data["status"]
        self.pwapp_category = data.get("pwapp_terms")
        self.image = data.get("share_image") if not data.get("featured_image") else data["featured_image"]

    def clean_content(self):
        soup = BeautifulSoup(self.content, 'lxml')
        return html.unescape(soup.text)

    def clean_title(self):
        return html.unescape(self.title)

    def convert_date(self):
        return datetime.datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S").timestamp()

    def convert_modified_date(self):
        return datetime.datetime.strptime(self.modified, "%Y-%m-%dT%H:%M:%S").timestamp()


class BaseScraper:
    def __init__(self):
        self.url = None
        self.headers = {'User-Agent': 'Mozilla/5.0 '}

    def _fetch_news(self, url: str) -> Generator[NewsResult, None, None]:
        r = requests.get(url, headers=self.headers)
        results_json = json.loads(r.text)
        for result in results_json:
            news = NewsResult(result)
            yield news

    def get_url(self, news_id: int, limit: Optional[Union[int, str]] = None) -> str:
        if limit:
            return f"{self.url}wp-json/wp/v2/posts?categories={news_id}&per_page={limit}"
        return self.url + "wp-json/wp/v2/posts?categories={}".format(news_id)


class AsyncBaseScraper:
    def __init__(self):
        self.url = None
        self.headers = {'User-Agent': 'Mozilla/5.0 '}

    async def _fetch_news(self, url: str, limit: Union[str, int]) -> Generator[NewsResult, None, None]:
        s = httpx.AsyncClient()
        r = await s.get(url, headers=self.headers)
        results_json = json.loads(r.text)
        for result in results_json[:limit]:
            news = NewsResult(result)
            yield news

    def get_url(self, news_id: int | str) -> str:
        r"""Get news category url.

        :param news_id: News Category id, str or int.
        :return: str
        """
        return self.url + "wp-json/wp/v2/posts?categories=".format(news_id)
