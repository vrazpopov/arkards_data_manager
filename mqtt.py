#*************************************************************************************
# The purpose of this file is the hanlde the subscribing and publishing ot the MQTT 
# broker. The idea here is to be able to communicate with the hololense
#*************************************************************************************

import paho.mqtt.client as mqtt
import time

# fuction for starting the connection and prompting user options
def start():
	#broker to connect to
	broker = "test.mosquitto.org"
	client = mqtt.Client("arkards")

	# print the heading and the options
	print("************************************************")
	print("*          WELCOME - PYTHON MQTT               *")
	print("************************************************")
	print("Please Select Option:")
	print("\t1) Send Test Login")
	print("\t2) Send Test Tag")
	print("\t3) Exit program")

	#loop unit we get a correct answer then execute
	while(1):
		
		mode = input("\nInput: ") #user input

		if mode == "1":
			break
		elif mode == "2":
			break
		elif mode == "3":
			print("EXITING EDIT MODE...")
			break
		else:
			print("INVALID MODE PLEASE TRY AGAIN!\n")

start()