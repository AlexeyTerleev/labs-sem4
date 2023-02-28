import sys
import os

import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

#from app.services.orm_model import Customer


class Model:
    def __init__(self) -> None:
        self.customers = pd.read_csv('../data/data.csv')

    def get_customers(self):
        return self.customers

    def add_customer(self, customer):
        self.customers.append(customer)
        self.customers.to_csv('../data/data.csv')

    def delete_customers(self, customers):
        pass

    def filter_customers(self, filter_options):
        pass
