import abc
import requests
from abc import abstractmethod
from selenium import webdriver
from lxml import html
from lxml.html import soupparser

class WebScrapingETL(metaclass=abc.ABCMeta):

    def __init__(self, url=None, xpath=None, **kwargs):
        self.url = url
        self.xpath = xpath

    def process(self):
        self.extract()
        self.transform()
        self.load()

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def load(self):
        pass


class SeleniumETL(WebScrapingETL):

    def __init__(self, driver=webdriver.Firefox(), **kwargs):
        super(SeleniumETL, self).__init__(**kwargs)
        self.driver = driver

    def extract(self):
        self.driver.get(self.url)

    def transform(self):
        html_source = self.driver.page_source
        self.tree = html.fromstring(html_source)
        self.element = self.tree.xpath(self.xpath)


class SoupHtmlETL(WebScrapingETL):

    def __init__(self, user_agent=None, **kwargs):
        super(SoupHtmlETL, self).__init__(**kwargs)
        self.headers = requests.utils.default_headers()
        if user_agent:
            self.headers.update({'User-Agent': user_agent})

        def extract(self):
            self.html_source = requests.get(self.url, headers=self.headers)

        def transform(self):
            if self.soup:
                tree = soupparser.fromstring(self.html_source)
            else:
                tree = html.fromstring(self.html_source)
            self.element = tree.xpath(self.xpath)
