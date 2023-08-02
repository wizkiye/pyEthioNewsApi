from rich.pretty import pprint

from pyEthioNews.providers import VOAAmharic


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    voa = VOAAmharic()
    news = loop.run_until_complete(voa.get_world_wide_news())
    pprint(news)
    # pprint(news[0])
    news_detail = loop.run_until_complete(news[0].fetch())
    pprint(news_detail)
