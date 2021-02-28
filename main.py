# this is the main file that will start the application

from login import *
from database import start_db
from menu import start_menu

start_db()
#start_login()
start_menu("arkadmin", "arkPASS9211") # do this so i dont have to enter the damn login everytime I want to test something 