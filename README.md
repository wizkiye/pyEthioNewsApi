# pyEthioNewsApi

This is a python wrapper for the Ethiopian news websites [Voa Amharic](https://amharic.voanews.com/), [Fanabc](https://www.fanabc.com/), [Mereja](https://mereja.com/), [WaltaInfo](https://waltainfo.com/)

## Installation

```bash
pip install https://github.com/wizkiye/pyEthioNewsApi.git
```

## Usage

```python
from pyEthioNews.providers import VOAAmharic, FanaBc, Mereja, Walta


async def main():
    # Get latest news
    
    voa = VOAAmharic()
    fana = FanaBc()
    mereja = Mereja()
    walta = Walta()

    voa_latest = await voa.get_world_wide_news()
    fana_latest = await fana.get_main_news()
    mereja_latest = await mereja.get_news()
    walta_latest = await walta.get_world_wide_news()

    print(voa_latest[0].title)
    print(fana_latest[0].title)
    print(mereja_latest[0].title)
    print(walta_latest[0].title)

```