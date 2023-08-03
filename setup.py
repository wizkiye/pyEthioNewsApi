from setuptools import setup, find_packages

setup(
    name="pyEthioNews",
    version="1.0.0",
    url="https://github.com/wizkiye/pyEthioNewsApi",
    license="MIT",
    author="https://github.com/wizkiye",
    author_email="wizkiye@gmail.com",
    description="Ethiopian News Scraper",
    install_requires=[
        "httpx",
        "bs4",
        "lxml",
    ],
    packages=find_packages(),
)
