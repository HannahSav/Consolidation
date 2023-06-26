import pandas as pd
from DB_sending import *

table_name = 'consolid_table'

def parsing_file(path):
    df_ord = pd.read_excel(path, header=8)
                           #header=[3, 4, 5, 6, 7, 8])
    pd.set_option('display.max_rows', 5)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 500)

    print(df_ord)
    print(df_ord.columns.tolist())

    #First start to create table
    drop_table(table_name)
    create_table('consolid_table', df_ord.columns.tolist())
    insert_values(table_name, df_ord.columns.tolist(), df_ord.values.tolist())
