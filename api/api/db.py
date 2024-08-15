# Creating a direct connection to the local database in MySQL 
import mysql.connector
from mysql.connector import Error
from .config import DB_CONFIG

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database'],
            auth_plugin="mysql_native_password"
        )
        if connection.is_connected():
            print("Connection to MySQL established successfully.")
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def get_cursor(connection):
    if connection:
        return connection.cursor(dictionary=True)
    else:
        print("No connection found.")
        return None

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
