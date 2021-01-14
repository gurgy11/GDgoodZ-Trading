import os

from mysql.connector import connect
from dotenv import load_dotenv

load_dotenv()


class Database():
    
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_NAME')
        self.connection = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        
    def cursor(self):
        ''' Returns a DB connection cursor '''
        
        return self.connection.cursor()
    
    def execute_select_query(self, query):
        ''' Executes a query that selects records '''
        
        cursor = self.cursor()
        cursor.execute(query)
        
        results = cursor.fetchall()
        data = []
        
        for res in results:
            data.append(res)
            
        return data
    
    def execute_insert_query(self, query, values):
        cursor = self.cursor()
        cursor.execute(query, values)
        
        conn = self.connection
        conn.commit()
        
    def execute_update_query(self, query, values):
        cursor = self.cursor()
        cursor.execute(query, values)
        
        conn = self.connection
        conn.commit()
        
    def execute_delete_query(self, query):
        cursor = self.cursor()
        cursor.execute(query)
        
        conn = self.connection
        conn.commit()
        
    def select_all_records(self, table):
        ''' Returns all records from a table '''
        
        query = """SELECT * FROM {table}""".format(table=table)
        records = self.execute_select_query(query)
        
        return records
    
    def select_records_by_field(self, table, column, value):
        ''' Selects everything from a table based on a column and its value '''
        
        query = """SELECT * FROM {table} WHERE {column}="{value}" """.format(table=table, column=column, value=value)
        records = self.execute_select_query(query)
        
        return records
    
    def select_record_by_id(self, table, record_id):
        ''' Selects a single record from a table using its ID '''
        
        query = """SELECT * FROM {table} WHERE id={record_id}""".format(table=table, record_id=record_id)
        records = self.execute_select_query(query)
        record = records[0]
        
        return record
    
    def insert_new_record(self, table, columns, values):
        ''' Inserts a new record into the database '''
        
        query = """INSERT INTO {table} (""".format(table=table)
        
        for col in columns:
            col_str = """{column}""".format(column=col)
            
            if columns.index(col) == len(columns) - 1:
                col_str += ") "
            else:
                col_str += ", "
                
            query += col_str
        
        query += "VALUES ("
        
        for val in values:
            val_str = "%s"
            
            if values.index(val) == len(values) - 1:
                val_str += ") "
            else:
                val_str += ", "
                
            query += val_str
            
        print("Created insert SQL query: ", query)
        
        self.execute_insert_query(query, values)
        
    def update_existing_record(self, table, record_id, columns, values):
        ''' Updates a record in a table with the corresponding record ID '''
        
        query = """UPDATE {table} SET """.format(table=table)
        
        for col in columns:
            col_str = """{column} = %s""".format(column=col)
            
            if columns.index(col) == len(columns) - 1:
                col_str += " "
            else:
                col_str += ", "
                
            query += col_str
            
        query += """WHERE id = {record_id}""".format(record_id=record_id)
        
        self.execute_update_query(query, values)
        
    def delete_existing_record(self, table, record_id):
        ''' Deletes a record in the table using its ID '''
        
        query = """DELETE FROM {} WHERE id = {}""".format(table, record_id)
        self.execute_delete_query(query)