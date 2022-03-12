from setuptools import setup

setup(
    name='pyEthioNewsApi',
    version='1.0.0',
    url='https://github.com/wizkiye/pyEthioNewsApi',
    license='MIT',
    author='https://github.com/wizkiye',
    author_email='wizkiye@gmail.com',
    description='Ethiopian News Scraper',
    install_requires=['requests', 'motor', 'rich', 'httpx', "telegraph", "ujson", "bs4", "beautifulsoup4", "lxml"],
    packages=['pyEthioNewsApi', "pyEthioNewsApi.providers"]
)
