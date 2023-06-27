import pandas as pd
from DB_sending import *
import pathlib

table_name = 'consolid_table'


def clear_db():
    # First start to create table
    drop_table(table_name)


def parsing_directory(path):
    dir = pathlib.Path(path)
    dir.iterdir()
    dir_list = list(dir.iterdir())
    for file in dir_list:
        parsing_file(file)


def parsing_file(path):
    df_ord = pd.read_excel(path, header=8)
                           #header=[3, 4, 5, 6, 7, 8])
    pd.set_option('display.max_rows', 5)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 500)

    insert_values(table_name, df_ord.columns.tolist(), df_ord.values.tolist())
