#*************************************************************************************
# The purpose of this file is to test the MQTT python stuff
#*************************************************************************************

import paho.mqtt.client as mqtt
import time
import sys
import json

# fucntion for on_log callback
def on_log(clinet, userdata, level, buf):
    print("log: "+ buf)

# function for on connect callback
def on_connect(client, userdata, level, rc):
    # if connection is good then print OK otherwise report the return code
    if rc == 0:
        print("Connected OK")
    else:
        print("Bad Connection, ERROR = ", rc)

# function for the on_message callback
def on_message():


# fuction for starting the connection and prompting user options
def start():
	#broker to connect to
	broker = "test.mosquitto.org"
	client = mqtt.Client("arkards")

    # set the callback fucntions for connection and log
	client.on_connect = on_connect
	client.on_log = on_log
    client.on_message = on_message

	# connect tothe broker
	print("Connecting to broker: " + broker)
	client.connect(broker)

    # subscribe to the login and tags
    client.subscribe("ark/login")

	# start the loop for call backs to be processed
	client.loop_start()

    # wait 1 second
    time.sleep(1)

	# print the heading and the options
	print("************************************************")
	print("*       LISTENING FOR LOGIN AND TAGS          *")
	print("************************************************")


start()
