import mysql.connector
from mysql.connector import (connection)

#Connect to the Database
cnx = mysql.connector.connect(user='user', password='password',
                              host='127.0.0.1',
                              database='bloksel-user')
cnx.close()
