from DbConnector import DbConnector
from tabulate import tabulate
import mysql.connector
from mysql.connector import errorcode
from tables import TABLES
import os


class DbCreator:

    def __init__(self):
        self.db_connector = DbConnector()
        self.connection = self.db_connector.db_connection
        self.cursor = self.db_connector.cursor
        self.base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset/')  # Ensures that os methods has this file's location as its root
     
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
        # print("Data from table %s, raw format:" % table_name)
        # print(rows)
        
        # Using tabulate to show the table in a nice way
        print("Data from table %s, tabulated:" % table_name)
        print(tabulate(rows, headers=self.cursor.column_names))
        return rows
    
    def drop_table(self, table_name):
        print("Dropping table %s..." % table_name)
        query = "DROP TABLE %s"
        self.cursor.execute(query % table_name)    
        
    def insert_userdata(self):
        user_ids = os.listdir(self.base_path + "Data")
        with open(self.base_path + "labeled_ids.txt", 'r') as f:
            labeled_ids = {line.strip() for line in f}

        for user_id in user_ids:
            has_labels = user_id in labeled_ids
            try:
                query = "INSERT INTO `User` (id, has_labels) VALUES (%s, %s)"
                self.cursor.execute(query, (user_id, has_labels))
            except mysql.connector.Error as err:
                print(f"Error inserting user {user_id}: {err.msg}")

        # Commit the changes
        self.connection.commit()
        print("User data inserted successfully.")
        
                        
def main():
    program = None
    try:
        program = DbCreator()
        program.create_tables()
        program.fetch_data(table_name="TrackPoint")
        program.show_tables()
        program.drop_table("User")
        program.drop_table("Activity")
        program.drop_table("TrackPoint")
        program.show_tables()        
    except Exception as e:
        print("ERROR: Failed to use database:", e)
    finally:
        if program:
            program.db_connector.close_connection()

if __name__ == '__main__':
    # main()
    program = DbCreator()
    program.create_tables()
    program.insert_userdata()
    program.fetch_data(table_name="User")
    program.drop_table("TrackPoint")
    program.drop_table("Activity")
    program.drop_table("User")
    program.db_connector.close_connection()

    