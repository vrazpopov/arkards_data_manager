#*************************************************************************************
# The purpose of this file is the handle the subscribing and publishing ot the MQTT
# broker. The idea here is to be able to communicate with the hololense
#*************************************************************************************
import paho.mqtt.client as mqtt
import time
import sys
import json


# fucntion for on_log callback
def on_log(clinet, userdata, level, buf):
    print("log: "+ buf)

# function for on connect callback
def on_connect(client, userdata, flags, rc):
    # if connection is good then print OK otherwise report the return code
    if rc == 0:
        print("Connected OK")
    else:
        print("Bad Connection, ERROR = " + rc)
     

# function for pressing 1) on the menue
def start_login(client):
	# print the heading
	print("\n******LOGIN SCREEN******\n")

	# get user name and password
	user = input("Enter User: ")
	password = input("Enter Password: ")

	# list of infomration  then convert to JSON
	info = [user, password]
	infoJson = json.dumps(info)

	# publish message
	client.publish("ark/login", infoJson)

    #print that it is beeing added
	print("Publishing...\n")

# function for pressing 2) on the menue
def start_tag(client):
	# print the heading
	print("\n******TAG SCREEN******\n")

	# get user name and password
	tag = input("Enter Tag: ")

	# publish message
	client.publish("ark/login", tag)

    #print that it is beeing added
	print("Publishing...\n")


# fuction for starting the connection and prompting user options
def start():
	#broker to connect to
	broker = "test.mosquitto.org"
	client = mqtt.Client("arkards_holo")

    # set the callback fucntions for connection and log
	client.on_connect = on_connect
	client.on_log = on_log

	# connect tothe broker
	print("Connecting to broker: " + broker)
	client.connect(broker)

	# start the loop for call backs to be processed
	client.loop_start()

	# wait 1 second before printing screen
	time.sleep(1)

	#loop unit we get a correct answer then execute
	while(1):
		
		# print the heading and the options
		print("************************************************")
		print("*          WELCOME - PYTHON MQTT               *")
		print("************************************************")
		print("Please Select Option:")
		print("\t1) Send Test Login")
		print("\t2) Send Test Tag")
		print("\t3) Exit program")

		mode = input("\nInput: ") #user input

		# if user presses one then simulated the login function
		if mode == "1":
			start_login(client)
		#if user pressed two then simulated the tag function
		elif mode == "2":
			start_tag(client)
		# if user presses three then stop loop disconnect and exit application
		elif mode == "3":
			print("EXITING...")
			client.loop_stop()
			client.disconnect()
			sys.exit(0)
		else:
			print("INVALID MODE PLEASE TRY AGAIN!\n")

start()
