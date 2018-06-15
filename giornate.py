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

    def clean_and_reshape(self):
        """ Function to perform basic operations of cleaning and reshaping data."""

        def pools(result):
            """" Function to defind the outcome 1,X,2 in the game sheet"""
            goals_home = int(result.split(":")[0])
            goals_visitor = int(result.split(":")[1])
            if goals_home > goals_visitor:
                return "1"
            elif goals_home < goals_visitor:
                return "2"
            else:
                return "X"
            
        # Eliminate the last column
        self.df.drop("Unnamed: 5", axis=1, inplace=True)
        # Assign a name to columns
        self.df.columns = ["day", "date", "home", "visitor", "result"]
        # Substitute the Nan with the last valid value
        self.df["day"].fillna(method='ffill', inplace=True)
        self.df.dropna(inplace=True)
        # Add the column pools based on the results of the match
        self.df['pools'] = self.df["result"].apply(lambda x: pools(x))
