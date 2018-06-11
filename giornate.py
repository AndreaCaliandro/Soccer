from lxml import html
import pandas as pd
from web_scraping_etl import SeleniumETL
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep


class Giornate(SeleniumETL):

    def __init__(self, **kwargs):
        super(Giornate, self).__init__(**kwargs)

    def page_interaction(self):
        counter = 0
        element = self.driver.find_element_by_id("tournament-page-results-more")
        cond = expected_conditions.invisibility_of_element_located((By.ID, "tournament-page-results-more"))
        while cond(self.driver) is False:
            element.click()
            counter += 1
            print('click n {}'.format(counter))
            sleep(5)

    def load(self):
        element = self.tree.xpath(self.xpath)
        table = element[0]
        raw_html = html.tostring(table)
        self.df = pd.read_html(raw_html)[0]
