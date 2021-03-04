# The purpose of this file is to set up all the functions that will interact with the database
# Each screen will be able to access this file and call the desired function 

# import modules
import mysql.connector

# variables for connections, host is local in this case since on this machine, 
HOST_ID = "localhost"
DATABASE_ID = "arkards"

# this function creates the schema, also creates tables to go into schema
def start_db(user_id, password_id):
	try:
		# connect to mysql sever
		mydb = mysql.connector.connect(
			host = HOST_ID,
			user = user_id,
			password = password_id
		)

		# cursor instance
		cursor = mydb.cursor()

		# create arkards database if not already
		cursor.execute("CREATE DATABASE IF NOT EXISTS arkards")	

		# create table if not already
		cursor.execute("CREATE TABLE IF NOT EXISTS arkards.tags (first_name VARCHAR(25), last_name VARCHAR(25), height TINYINT(150), weight SMALLINT, sex VARCHAR(25), tag VARCHAR (100), pic LONGBLOB)")			

		# commit close connections
		mydb.commit()
		mydb.close()

		return True
	except mysql.connector.Error as err:
		return False


