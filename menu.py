# This file contains the the guts of the main screen.
# From here the user can direct themselves throughout the application

# import modules
from tkinter import *
from database import *


#**********************************************************************************************
#										MAIN SCREEN
#
#		 function for starting the menu, accept the user and pass from the menu screen
#**********************************************************************************************
def start_menu(user, password):

	#create the menu root
	menu_root = Tk()

	# set the title and icon
	menu_root.title("ARKARDS - MENU")
	menu_root.iconbitmap("icon.ico")

	# set demintions for the window, also get the screen width and height for centering later
	menu_width = 1200
	menu_height = 720
	screen_width = menu_root.winfo_screenwidth()
	screen_height = menu_root.winfo_screenheight()

	# x and y variables for then placing the window onto the middle of the screen.
	x = (screen_width / 2) - (menu_width / 2)
	y = (screen_height / 2) - (menu_height / 2)

	# now set the geometry of the screen and center it
	menu_root.geometry(f'{menu_width}x{menu_height}+{int(x)}+{int(y)}')

	# check the user and password against the database, just incase login screen gets bypassed. 
	# if the check returns bad then kill the program
	check = check_user_db(user, password)
	if not check:
		messagebox.showerror("ERROR","SECURITY COMPROMISED! EXITING...")
		menu_root.destroy()


	# main loop
	menu_root.mainloop()

#**********************************************************************************************
#						  		      END MAIN SCREEN
#**********************************************************************************************