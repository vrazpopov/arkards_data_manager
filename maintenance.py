#**********************************************************************************************
#										MAINTENANCE SCREEN
#
#		 The purpose of this file is to for the maintenance screen, handle functions like 
#		adding users, and clearing the tags out, etc.
#**********************************************************************************************

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from database import *


# fonts
FONT_LARGE = ("Calibri", 24)
FONT_MEDIUM = ("Calibri", 16)
FONT_SMALL = ("Calibri", 12)


def start_maintenace(root, user, password):

	# button functions

	# hide the parent
	root.withdraw()

	# warn user, that db will be cleared, then prompt for password if they want to continue
	def clear_click():

		response = messagebox.askyesno("WARNING!","THIS WILL CLEAR TAGS, DO YOU WANT TO CONTINUE?")
		# yes is selected ask for password, used simple dialog for simplicity cant figure out how to center, who cares...
		if response == 1:

			# now check the password 
		    answer = simpledialog.askstring("Password", "Enter Password for : " + str(user), parent = admin_root, show = '*')
		    
		    #if the password is correct clear tags
		    if answer == password:
		    	check = clear_tags(user, password)
		    	
		    	# if clear is works
		    	if check:
		    		message_label.config(text = "CLEARING TAGS...", fg = "green")
		    		admin_root.after(1500, clear_text)

		    	else:
		    		message_label.config(text = "ERROR CLEARING TAGS...", fg = "red")
		    		admin_root.after(1500, clear_text)

		    # othwerwise error
		    else:
		    	messagebox.showerror("ERROR!","INCORRECT PASSWORD!")

		    admin_root.focus_force()

	# unhide parent and close
	def home_click():
		root.deiconify()
		admin_root.destroy()

	# function for clicking backup, calls db function 
	def backup_click():
		backup_db(user, password)
		message_label.config(text = "CREATING BACKUP...", fg = "green")
		admin_root.after(1500, clear_text)

	# function clicking add, creates child window
	def add_click():
		child_add(admin_root, user, password)


	# simple function for clearing text
	def clear_text():
		message_label.config(text = "")

	#create the admin root
	admin_root = Toplevel(root)
	# set the title and icon
	admin_root.title("ARKARDS - MAINTENANCE")
	admin_root.iconbitmap("icon.ico")

	# set demintions for the window, also get the screen width and height for centering later
	admin_width = 1200
	admin_height = 720
	screen_width = admin_root.winfo_screenwidth()
	screen_height = admin_root.winfo_screenheight()

	# x and y variables for then placing the window onto the middle of the screen.
	x = (screen_width / 2) - (admin_width / 2)
	y = (screen_height / 2) - (admin_height / 2)

	# now set the geometry of the screen and center it
	admin_root.geometry(f'{admin_width}x{admin_height}+{int(x)}+{int(y)}')

	# incase window is force closed
	admin_root.bind("<Destroy>", lambda e: root.deiconify())

	# load the images
	logo_image = PhotoImage(file = "images/logo.png")
	add_image = PhotoImage(file = "images/add_user.png")
	clear_image =  PhotoImage(file = "images/clear.png")
	backup_image =  PhotoImage(file = "images/backup.png")
	home_image =  PhotoImage(file = "images/home.png")	

	# frameS
	title_frame = Frame(admin_root)
	button_frame = Frame(admin_root)

	user_text = "Logged in: " + user

	# labels
	logo_label = Label(title_frame, image = logo_image, padx = 10, pady = 10)
	title_label = Label(title_frame,  text = "ARKARDS - Maintenance", font = FONT_LARGE, padx = 10, pady = 10)
	user_label = Label(admin_root, text = user_text, font = FONT_MEDIUM, pady = 10)
	message_label = Label(admin_root, text = "", font = FONT_MEDIUM, pady = 10)

	# buttons
	clear_button = Button(button_frame, image = clear_image, width = 175, height = 175, bd = 10, text = "Clear Tags", font = FONT_LARGE, compound = "top", command = clear_click)
	backup_button = Button(button_frame, image = backup_image, width = 175, height = 175, bd = 10, text = "Backup Tags", font = FONT_LARGE, compound = "top", command = backup_click)
	add_button = Button(button_frame, image = add_image, width = 175, height = 175,  bd = 10, text = "Add User", font = FONT_LARGE, compound = "top", command = add_click)
	home_button = Button(button_frame, image = home_image, width = 175, height = 175,  bd = 10, text = "Main Screen", font = FONT_LARGE, compound = "top", command = home_click)

	# place the labels into the frame
	logo_label.grid(row = 0, column = 0)
	title_label.grid(row = 0, column = 1)


    # place buttons
	clear_button.grid(row = 0, column = 0, padx = 50, pady = 20)
	backup_button.grid(row = 0, column = 1, padx = 50, pady = 20)
	add_button.grid(row = 1, column = 0, padx = 50, pady = 20)
	home_button.grid(row = 1, column = 1, padx = 50, pady = 20)

	# pack the frame onto the screen
	title_frame.pack()
	button_frame.pack()

	# pack the user and message label
	user_label.pack()
	message_label.pack()

	# main loop
	admin_root.mainloop()

# fucnction for calling child window 
def child_add(root, user, password):

	# function for clicking the create button, checks passwords to make sure they match, then calls db funciton
	def add_click():

		# get values from the entry fields cast as strings 
		user_value = str(user_entry.get())
		pass_value = str(pass_entry.get())
		check_pass_value = str(check_pass_entry.get())
		
		if pass_value == check_pass_value:

			message_label.config(text = "CREATING USER...", fg = "green")
			clear_entry()
			child_root.after(1500, clear_text)
			user_entry.focus_force()

		# if passwords do not match error
		else:

			message_label.config(text = "PASSWORDS DO NOT MATCH!", fg = "red")
			child_root.after(1500, clear_text)		

	# simple function for deleting the message label
	def clear_text():

		message_label.config(text = "")

	# simple function for clearing entry fields
	def clear_entry():

		user_entry.delete(0, END)
		pass_entry.delete(0, END)
		check_pass_entry.delete(0, END)	

	#create the admin root
	child_root = Toplevel(root)
	# set the title and icon
	child_root.title("ARKARDS - CREATE USER")
	child_root.iconbitmap("icon.ico")

	# set demintions for the window, also get the screen width and height for centering later
	child_width = 600
	child_height = 350
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()

	# x and y variables for then placing the window onto the middle of the screen.
	x = (screen_width / 2) - (child_width / 2)
	y = (screen_height / 2) - (child_height / 2)

	# now set the geometry of the screen and center it
	child_root.geometry(f'{child_width}x{child_height}+{int(x)}+{int(y)}')

	# make the window a fixed size
	child_root.resizable(0,0)

	# create frames
	entry_frame = Frame(child_root)
	button_frame = Frame(child_root)

	# create labels
	title_label = Label(child_root, text = "CREATE NEW USER", font = FONT_LARGE, pady = 10)
	user_label = Label(entry_frame, text = "Username: ", font = FONT_SMALL)
	pass_label = Label(entry_frame, text = "Password: ", font = FONT_SMALL)
	check_pass_label = Label (entry_frame, text = "Re-enter Password: ", font = FONT_SMALL)
	message_label = Label(child_root, text = "", font = FONT_SMALL)

	# create entry boxes
	user_entry = Entry(entry_frame, width = 25, font = FONT_SMALL)
	pass_entry = Entry(entry_frame, width = 25, show = "*", font = FONT_SMALL)
	check_pass_entry = Entry(entry_frame, width = 25, show = "*", font = FONT_SMALL)

	# create buttons
	add_button = Button(button_frame, bd = 5, text = "Create User", font = FONT_SMALL, width = 10, command = add_click)
	cancel_button = Button(button_frame, bd = 5, text = "Cancel", font = FONT_SMALL, width = 10, command = child_root.destroy) # if pressed then exit application

	# place the labels and entry boxes into the frame
	user_label.grid(row = 0, column = 0, padx = 10, pady = 10)
	pass_label.grid(row = 1, column = 0, padx = 10, pady = 10)
	check_pass_label.grid(row = 2, column = 0, padx = 10, pady = 10)
	user_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
	pass_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
	check_pass_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

	# place buttons onto the button frame
	add_button.grid(row = 0, column = 0, padx = 10, pady = 10)
	cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)

	# pack the title label
	title_label.pack()

	# pack the frame onto the screen
	entry_frame.pack(pady = 10)

	# pack the button frame onto the screen
	button_frame.pack(pady = 10)

	# pack the message label onto the screen
	message_label.pack()

	# set focus on the user entry label
	user_entry.focus_set()

	# if enter is pressed then focus on the password entry
	user_entry.bind("<Return>", lambda e: pass_entry.focus_set())

	# if enter is pressed then focus on the password entry
	pass_entry.bind("<Return>", lambda e: check_pass_entry.focus_set())  

	#if enter is pressed same as clicking login button
	check_pass_entry.bind("<Return>", lambda e: add_click())		

	child_root.mainloop()





























#**********************************************************************************************
#						  		      END MAINTENANCE SCREEN
#**********************************************************************************************




