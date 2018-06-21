""" Class to create the ranking of teams according the matches results. The ranking is updated after each giornata"""
import andas as pd


class ranking():

    def load_giornata(self):
        """ Load the giornate table"""

    def matches_played(self):
        """ Number of matches played"""

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
