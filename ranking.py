""" Class to create the ranking of teams according the matches results. The ranking is updated after each giornata"""
import pandas as pd


class ranking():

    def __init__(self, **kwargs):
        """ Initialize variables here"""
        # Initialize an empty df
        col_names = ['team', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pt', 'pos']
        df = pd.DataFrame(columns=col_names)
        first_day = "Giornata 1"
        list_of_days = ['Giornata 38', 'Giornata 37']

    def load_giornata(self, first_day, df):
        """ Load the giornate table, select giornate and initialize """
        # Read from the entire table only lines relative to the same day
        df_init = df_loaded.loc[df['day'] == first_day]
        # df_init = df_loaded.loc[df_loaded['day'].isin(list)]

        # Initialize lines based on team name
        home = df_init['home']
        visitor = df_init['visitor']
        df['team'] = pd.concat([home, visitor])
        df.set_index('team', inplace=True)
        df = df.fillna(0)

        return df

    def matches_played(self, list_of_days, df):
        """ Number of matches played"""
        df_info = df_loaded.loc[df_loaded['day'].isin(list_of_days)]

        def mph_count():
        #Count how many match played at home
        df["MPH"] = df_loaded.groupby("home").count()
        # Count how many match played as visitor
        df["MPV"] = df_loaded.groupby("visitor").count()
        df = df.fillna(0)
        # Count total matches
        df["MP"] = df["MPH"] + df["MPV"]

        return df

    def won(self):
        """ Number of matches won"""

    def draw(self):
        """ Number of times a team has finished a match with an even score or tie """

    def loss(self):
        """ Number of matches lost """

    def goals_for(self):
        """ Number of goals scored """

    def goal_against(self):
        """ Number of goals conceded by a team """

    def goal_difference(self):
        """ Difference between GF and GA,"""

    def points(self):
        """ Number of points earned by a team after playing a certain number of games """

    def position(self):
        """ Ranking number """

    def create_ranking_table(self):
        """ Function to create the final table """
        # my_df.loc[len(my_df)] = [2, 4, 5]
        # my_df = my_df.append(my_df2)
