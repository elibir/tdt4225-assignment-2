from DbConnector import DbConnector
from tabulate import tabulate
import mysql.connector
from mysql.connector import errorcode
from tables import TABLES


class DbCreator:

    def __init__(self):
        self.db_connector = DbConnector()
        self.connection = self.db_connector.db_connection
        self.cursor = self.db_connector.cursor
     
    def create_tables(self):   
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                self.cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
                
        self.connection.commit()
        
    def show_tables(self):
        self.cursor.execute("SHOW TABLES")
        rows = self.cursor.fetchall()
        print(tabulate(rows, headers=self.cursor.column_names))
        
    def fetch_data(self, table_name):
        query = "SELECT * FROM %s"
        self.cursor.execute(query % table_name)
        rows = self.cursor.fetchall()
        print("Data from table %s, raw format:" % table_name)
        print(rows)
        # Using tabulate to show the table in a nice way
        print("Data from table %s, tabulated:" % table_name)
        print(tabulate(rows, headers=self.cursor.column_names))
        return rows
                        
def main():
    program = None
    try:
        program = DbCreator()
        program.create_tables()
        program.fetch_data(table_name="TrackPoint")
        program.show_tables()        
    except Exception as e:
        print("ERROR: Failed to use database:", e)
    finally:
        if program:
            program.db_connector.close_connection()

if __name__ == '__main__':
    main()