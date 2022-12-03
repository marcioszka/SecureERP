""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

def get_table():
   sales = data_manager.read_table_from_file(DATAFILE)
   return sales

def write_file(table):
    data_manager.write_table_to_file(DATAFILE, table)
