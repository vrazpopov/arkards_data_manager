# The purpose of this file is to set up all the functions that will interact with the database
# Each screen will be able to access this file and call the desired function 

# import modules
import mysql.connector 

# this function creates the schema
def create_db():

	# connect to 
	mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "@rkARD$1921#"
	)

	# cursor instance
	cursor = mydb.cursor()

	# create arkards database if not already
	cursor.execute("CREATE DATABASE IF NOT EXISTS arkards")	

	# close connections
	cursor.close()
	mydb.close()


# this fuction creates the tables intade the created schema
def create_tables():

	# connect to 
	mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "@rkARD$1921#",
		database = "arkards"
	)

	# cursor instance
	cursor = mydb.cursor()

	# create tables if not already
	cursor.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(25), password VARCHAR(25))")
	cursor.execute("CREATE TABLE IF NOT EXISTS tags (first_name VARCHAR(25), last_name VARCHAR(25), height TINYINT(150), weight SMALLINT, sex VARCHAR(25), tag VARCHAR (100), pic LONGBLOB)")			

	# create default entry if we havent already
	if not check_user_db("arkadmin","arkPASS9211"):
		cursor.execute("INSERT INTO users (username, password) VALUES ('arkadmin', 'arkPASS9211');")

	# close connections
	mydb.commit()
	mydb.close()


# this is the startup fuction called in the beginging to ensure the correct schema (db) and tables are created if they already do not exist.
def start_db():

	create_db()
	create_tables()

# this fuction searches the user tables to make sure a valid user is signin in
def check_user_db(user, login_pass):

	# connect to 
	mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "@rkARD$1921#",
		database = "arkards"
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
	mydb. close()
	
	# now if we have a match then we can let the user login, this is just a check and doesnt affect the next screen, mayeb can change in the future\
	# return false if empty aka no match, other true aka match
	if  result is None:
		return False
	else:
		return True

