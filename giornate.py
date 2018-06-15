from lxml import html
import pandas as pd
from web_scraping_etl import SeleniumETL


class Giornate(SeleniumETL):

    def __init__(self, **kwargs):
        super(Giornate, self).__init__(**kwargs)
        print(self.url)
        print(self.xpath)

    def load(self):
        table = self.element[0].getchildren()[0]
        raw_html = html.tostring(table)
        self.df = pd.read_html(raw_html)[0]
