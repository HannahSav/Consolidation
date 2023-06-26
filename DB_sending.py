import sqlite3


def sqlite_creating():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("База данных создана и успешно подключена к SQLite")

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print("Версия базы данных SQLite: ", record)
        cursor.close()

    except sqlite3.Error as error:
        print("Не удалось подключиться к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def create_table(table_name, list_of_headers):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        sqlite_create_table_query = '''CREATE TABLE ''' + table_name + ''' (
                                    id INTEGER PRIMARY KEY'''
        for column_name in list_of_headers:
            sqlite_create_table_query += ', \ncolumn_' + str(column_name) +  ' TEXT NOT NULL'
        sqlite_create_table_query += ');'

        print(sqlite_create_table_query)
        cursor = sqlite_connection.cursor()
        print("База данных подключена к SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблица SQLite создана")

        cursor.close()

    except sqlite3.Error as error:
        print("Error during the connection with sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Connection closed")


def drop_table(table_name):
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    sqlite_insert_table_query = '''DROP TABLE ''' + table_name + ''' ; '''
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_insert_table_query)
    sqlite_connection.commit()


def insert_values(table_name, list_of_headers, list_of_meanings):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        sqlite_insert_table_query = '''INSERT INTO ''' + table_name + ''' (id '''
        for column_name in list_of_headers:
            sqlite_insert_table_query += ', column_' + str(column_name)
        sqlite_insert_table_query += ') VALUES '

        for line in range(0, len(list_of_meanings)):
            #print('list = ', list_of_meanings[line])
            if str(list_of_meanings[line][0]) != 'nan':
                sqlite_insert_table_query += '(' + str(line)
                print("'", list_of_meanings[line][0], "'", sep='')
                for meaning in range(len(list_of_meanings[line])):
                    sqlite_insert_table_query += ", '" + str(list_of_meanings[line][meaning])+ "' "
                sqlite_insert_table_query += "),\n"

        sqlite_insert_table_query = sqlite_insert_table_query[:-2]
        sqlite_insert_table_query += ';'

        print(sqlite_insert_table_query)
        cursor = sqlite_connection.cursor()
        print("Connected")
        cursor.execute(sqlite_insert_table_query)
        sqlite_connection.commit()
        print("Values added")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
