
#**********************************************************************************************
#										ADD SCREEN
#
# this function is for adding a tag into the MySQL db. This will be a child window to the main
# screen and will accepnt a root as a parameter, in this case the menu root
#**********************************************************************************************

# import modules
from tkinter import *
from database import *
from PIL import ImageTk, Image

# fonts
FONT_LARGE = ("Calibri", 24)
FONT_MEDIUM = ("Calibri", 16)
FONT_SMALL = ("Calibri", 12)


def start_add(root, user, password):

	# create child window
	add_root = Toplevel(root)

	# set the title and icon
	add_root.title("ARKARDS - ADD")
	add_root.iconbitmap("icon.ico")

	# window demenisons
	add_width = 500
	add_height = 600

	# window width and height of the splash screen and screen
	screen_width = root.winfo_screenwidth()
	screen_height =root.winfo_screenheight()

	# x and y variables for centering the screen
	x = (screen_width / 2) - (add_width / 2)
	y = (screen_height / 2) - (add_height / 2)

	# adjust the splash screen width and height and then center
	add_root.geometry(f'{add_width}x{add_height}+{int(x)}+{int(y)}')

	# make the window a fixed size
	add_root.resizable(0,0)

	# title and message labels
	title_label = Label(add_root, text = "Add Tag to DB", font = FONT_LARGE, pady = 10)

	message_label = Label(add_root, text = "", font = FONT_MEDIUM, pady = 10)
	
	# frames
	entry_frame = Frame(add_root)
	button_frame = Frame(add_root)

	# labels for entry
	tag_label = Label(entry_frame, text = "Tag #:", font = FONT_SMALL, pady = 10)
	first_label = Label(entry_frame, text = "Frist Name:", font = FONT_SMALL, pady = 10)
	last_label = Label(entry_frame, text = "Last Name:", font = FONT_SMALL, pady = 10)
	height_label = Label(entry_frame, text = "Height:", font = FONT_SMALL, pady = 10)
	weight_label = Label(entry_frame, text = "Weight:", font = FONT_SMALL, pady = 10)
	sex_label = Label(entry_frame, text = "Sex:", font = FONT_SMALL, pady = 10)

	# entry fields for the information
	tag_entry = Entry(entry_frame, width = 20, font = FONT_SMALL)
	first_entry = Entry(entry_frame, width = 20, font = FONT_SMALL)
	last_entry = Entry(entry_frame, width = 20, font = FONT_SMALL)
	height_entry = Entry(entry_frame, width = 20, font = FONT_SMALL)
	weight_entry = Entry(entry_frame, width = 20, font = FONT_SMALL)
	sex_entry = Entry(entry_frame, width = 20, font = FONT_SMALL)

	# buttons
	add_button = Button(button_frame, bd = 5, text = "Add", font = FONT_SMALL, width = 10,)
	cancel_button = Button(button_frame, bd = 5, text = "Cancel", font = FONT_SMALL, width = 10, command = add_root.destroy) # if pressed then exit application

	# place labels into the frame
	tag_label.grid(row = 0, column = 0, padx = 10, pady = 10)
	first_label.grid(row = 1, column = 0, padx = 10, pady = 10)
	last_label.grid(row = 2, column = 0, padx = 10, pady = 10)
	height_label.grid(row = 3, column = 0, padx = 10, pady = 10)
	weight_label.grid(row = 4, column = 0, padx = 10, pady = 10)
	sex_label.grid(row = 5, column = 0, padx = 10, pady = 10)

	# place the entry boxes into the frame
	tag_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
	first_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
	last_entry.grid(row = 2, column = 1, padx = 10, pady = 10)
	height_entry.grid(row = 3, column = 1, padx = 10, pady = 10)
	weight_entry.grid(row = 4, column = 1, padx = 10, pady = 10)
	sex_entry.grid(row = 5, column = 1, padx = 10, pady = 10)

	# place buttons to button frame
	add_button.grid(row = 0, column = 0, padx = 10, pady = 10)
	cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

	# pack everything
	title_label.pack()
	entry_frame.pack()
	button_frame.pack()
	message_label.pack()

	add_root.mainloop()


#**********************************************************************************************
#						  		      END ADD SCREEN
#**********************************************************************************************

# this functino takes an image path, opens it resizes and returns PhotoImage object
def resize_image(image_path):
	
	# open the image
	pic = Image.open(image_path)

	# resize the image to a 128 x 128 
	resized_pic = pic.resize((128, 128), Image.ANTIALIAS)

	# make photoimage object
	new_pic = ImageTk.PhotoImage(resized_pic)

	# return the resized image
	return new_pic

