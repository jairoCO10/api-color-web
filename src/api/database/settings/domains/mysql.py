from dotenv import load_dotenv
import os
load_dotenv()


class MySql:
    '''
    conexion de base de datos con mysql
    '''
    SQL_DB= os.getenv('MYSQL_DB')
    SQL_USER= os.getenv('MYSQL_USER')
    SQL_PASSWORD= os.getenv('PASSWORD')
    SQL_SERVER= os.getenv('MYSQL_SERVER')
    SQL_PORT= os.getenv('MYSQL_PORT')
    SERVER_TYPE= os.getenv('SERVER_TYPE')
    LIBRARY_SERVER= os.getenv('LIBRARY_SERVER')

sql = MySql
