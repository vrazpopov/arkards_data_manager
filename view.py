#**********************************************************************************************
#										VIEW SCREEN
#
#		 The purpose of this file is to view the current tags inside the database.
#**********************************************************************************************

from tkinter import *
from database import *

# fonts
FONT_LARGE = ("Calibri", 24)
FONT_MEDIUM = ("Calibri", 16)
FONT_SMALL = ("Calibri", 12)


def start_view(root, user, password):

	#create the view root
	view_root = Toplevel(root)
	# set the title and icon
	view_root.title("ARKARDS - VIEW")
	view_root.iconbitmap("icon.ico")

	# set demintions for the window, also get the screen width and height for centering later
	view_width = 1200
	view_height = 720
	screen_width = view_root.winfo_screenwidth()
	screen_height = view_root.winfo_screenheight()

	# x and y variables for then placing the window onto the middle of the screen.
	x = (screen_width / 2) - (view_width / 2)
	y = (screen_height / 2) - (view_height / 2)

	# now set the geometry of the screen and center it
	view_root.geometry(f'{view_width}x{view_height}+{int(x)}+{int(y)}')

	# load the images
	logo_image = PhotoImage(file = "images/logo.png")
	add_image = PhotoImage(file = "images/add.png")
	view_image =  PhotoImage(file = "images/view.png")
	gear_image =  PhotoImage(file = "images/gear.png")
	home_image =  PhotoImage(file = "images/home.png")	

	# frameS
	title_frame = Frame(view_root)
	button_frame = Frame(view_root)

	# labels
	logo_label = Label(title_frame, image = logo_image, padx = 10, pady = 10)
	title_label = Label(title_frame,  text = "ARKARDS - Maintenance", font = FONT_LARGE, padx = 10, pady = 10)

	# buttons
	add_button = Button(button_frame, image = add_image, width = 175, height = 175, bd = 10, text = "Add Tag", font = FONT_LARGE, compound = "top")
	view_button = Button(button_frame, image = view_image, width = 175, height = 175, bd = 10, text = "View Tags", font = FONT_LARGE, compound = "top")
	gear_button = Button(button_frame, image = gear_image, width = 175, height = 175,  bd = 10, text = "Maintenance", font = FONT_LARGE, compound = "top")
	home_button = Button(button_frame, image = home_image, width = 175, height = 175,  bd = 10, text = "Main Screen", font = FONT_LARGE, compound = "top", command = view_root.destroy)

	# place the labels into the frame
	logo_label.grid(row = 0, column = 0)
	title_label.grid(row = 0, column = 1)

    # place buttons
	add_button.grid(row = 0, column = 0, padx = 50, pady = 20)
	view_button.grid(row = 0, column = 1, padx = 50, pady = 20)
	gear_button.grid(row = 1, column = 0, padx = 50, pady = 20)
	home_button.grid(row = 1, column = 1, padx = 50, pady = 20)

	# pack the frame onto the screen
	title_frame.pack()
	button_frame.pack()

	# main loop
	view_root.mainloop()







#**********************************************************************************************
#						  		      END VIEW SCREEN
#**********************************************************************************************