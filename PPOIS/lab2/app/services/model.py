import sys
import os

import pandas as pd
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


class Model:
    def __init__(self) -> None:
        try:
            self.df = pd.read_csv('app/data/data.csv')

        except (FileNotFoundError, pd.errors.EmptyDataError):
            self.df = pd.DataFrame({
                'tour_name': [f'test_tour{x}' for x in range(5)],
                'date': [f'test_date{x}' for x in range(5)],
                'sport': [f'test_sport{x}' for x in range(5)],
                'name': [f'Test Name {x}' for x in range(5)],
                'reward': [(x + 1) * 100 for x in range(5)],
            })
            self.df['winner_reward'] = self.df['reward'] * 0.6

        self.df.to_csv('app/data/data.csv', index=False)
        self.active_df = self.df

    def get_list(self):
        return self.active_df.values.tolist()

    def add_line(self, line):
        print(line)
        self.df.loc[len(self.df.index)] = line
        self.df.to_csv('app/data/data.csv', index=False)

        self.active_df = self.df

    def delete_customers(self, customers):

        if not len(customers):
            return

        self.df = self.df.set_index('tour_name')
        self.df = self.df.drop(customers, axis=0)
        self.df = self.df.reset_index()

        self.df.to_csv('app/data/data.csv', index=False)

    def filter_customers(self, filter_options):
        self.active_df = self.df
        if filter_options['tour_name'] is not None:
            re_str = f'.*{filter_options["tour_name"]}.*'
            self.active_df = self.active_df[self.active_df.tour_name.str.match(re_str)]

        if filter_options['date'] is not None:
            self.active_df = self.active_df[self.active_df.date == filter_options['date']]

        if filter_options['sport'] is not None:
            re_str = f'.*{filter_options["sport"]}.*'
            self.active_df = self.active_df[self.active_df.sport.str.match(re_str)]

        if filter_options['name'] is not None:
            re_str = f'.*{filter_options["name"]}.*'
            self.active_df = self.active_df[self.active_df.name.str.match(re_str)]

        if filter_options['min_reward'] is not None:
            self.active_df = self.active_df[self.active_df.reward >= filter_options['min_reward']]
        if filter_options['max_reward'] is not None:
            self.active_df = self.active_df[self.active_df.reward <= filter_options['max_reward']]

        if filter_options['min_winner_reward'] is not None:
            self.active_df = self.active_df[self.active_df.winner_reward >= filter_options['min_winner_reward']]
        if filter_options['max_winner_reward'] is not None:
            self.active_df = self.active_df[self.active_df.winner_reward <= filter_options['max_winner_reward']]

    def disable_filter_customers(self):
        self.active_df = self.df
