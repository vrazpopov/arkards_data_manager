# The purpose of this file is to set up all the functions that will interact with the database
# Each screen will be able to access this file and call the desired function 

# import modules
import mysql.connector

# variables for connections, host is local in this case since on this machine, 
# also user and password are set up when installed onto machine, these are the values I chose.
HOST_ID = "localhost"
USER_ID = "root"
PASSWORD_ID = "@rkARD$1921#"
DATABASE_ID = "arkards"

# this function creates the schema, also creates tables to go into schema
def start_db():

	# connect to mysql sever
	mydb = mysql.connector.connect(
		host = HOST_ID,
		user = USER_ID,
		password = PASSWORD_ID
	)

	# cursor instance
	cursor = mydb.cursor()

	# create arkards database if not already
	cursor.execute("CREATE DATABASE IF NOT EXISTS arkards")	


	# create tables if not already
	cursor.execute("CREATE TABLE IF NOT EXISTS arkards.users (username VARCHAR(25), password VARCHAR(25))")
	cursor.execute("CREATE TABLE IF NOT EXISTS arkards.tags (first_name VARCHAR(25), last_name VARCHAR(25), height TINYINT(150), weight SMALLINT, sex VARCHAR(25), tag VARCHAR (100), pic LONGBLOB)")			

	# create default entry if we havent already
	if not check_user_db("arkadmin","arkPASS9211"):
		cursor.execute("INSERT INTO arkards.users (username, password) VALUES ('arkadmin', 'arkPASS9211');")


	# commit close connections
	mydb.commit()
	mydb.close()


# this fuction searches the user tables to make sure a valid user is signin in
def check_user_db(user, login_pass):

	# connect to server
	mydb = mysql.connector.connect(
		host =  HOST_ID,
		user = USER_ID,
		password = PASSWORD_ID,
		database = DATABASE_ID
	)

	# cursor instance
	cursor = mydb.cursor()

	# query for searching the table
	query = "SELECT * FROM users WHERE username LIKE %s AND password LIKE %s;"
	data_tuple = (user, login_pass)

	# execute query,search for username and password combination.
	cursor.execute(query, data_tuple)

	# there should only be one so set it to the result
	result = cursor.fetchone()

	# commit and close db connection
	mydb.commit()
	mydb.close()
	
	# now if we have a match then we can let the user login, this is just a check and doesnt affect the next screen, mayeb can change in the future\
	# return false if empty aka no match, other true aka match
	if  result is None:
		return False
	else:
		return True

