# *************************************************************************************************
#										DATBASE FILE 
# The purpose of this file is to set up all the functions that will interact with the database
# Each screen will be able to access this file and call the desired function 
#**************************************************************************************************

# import modules
import mysql.connector

# variables for connections, host is local in this case since on this machine, 
HOST_ID = "localhost"

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
		cursor.execute("CREATE TABLE IF NOT EXISTS arkards.tags (tag VARCHAR(100) NOT NULL PRIMARY KEY, first_name VARCHAR(25), last_name VARCHAR(25), height VARCHAR(25), weight VARCHAR(25), sex VARCHAR(25), pic VARCHAR(10000))")			

		# commit close connections
		mydb.commit()
		mydb.close()

		return True
	except mysql.connector.Error as err:
		print(err)
		return False

# this function is for adding a tag to the db
def add_tag(user_id, password_id, tag, first_name, last_name, height, weight, sex, pic):

		try:
			# connect to mysql sever
			mydb = mysql.connector.connect(
				host = HOST_ID,
				user = user_id,
				password = password_id
			)

			# cursor instance
			cursor = mydb.cursor()

			# SQL query
			query = "INSERT INTO arkards.tags (tag, first_name, last_name, height, weight, sex, pic) VALUES(%s, %s, %s, %s, %s, %s, %s)"

			# data tuple for values
			values = (tag, first_name, last_name, height, weight, sex, pic)

			# execute the command
			cursor.execute(query, values)

			# commit close connections
			mydb.commit()
			mydb.close()

			return True
		except mysql.connector.Error as err:
			print(err)
			return False

# this function is designed to check against an already added tag, since there can only be one 
def check_tag(user_id, password_id, tag):
	
		try:
			# connect to mysql sever
			mydb = mysql.connector.connect(
				host = HOST_ID,
				user = user_id,
				password = password_id
			)

			# cursor instance
			cursor = mydb.cursor()

			# SQL query
			query = "SELECT * FROM arkards.tags WHERE tag = %s"

			# execute the command
			cursor.execute(query, (tag,))
			row = cursor.fetchone()

			# commit close connections
			mydb.commit()
			mydb.close()

			if not row:
				return False
			else:
				return True

		except mysql.connector.Error as err:
			print(err)


# *************************************************************************************************
#										END DATBASE FILE 
#**************************************************************************************************
