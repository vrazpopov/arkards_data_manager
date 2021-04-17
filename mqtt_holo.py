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

# function for the on_message callback
def login_results_callback(client, userdata, msg):

    # message decdoing then convert from JSON to list
    msg_decode = str(msg.payload.decode("utf-8","ignore"))
    msg_list = json.loads(msg_decode)

    # get the user name and password then save it
    user_id = msg_list["user_id"]
    valid = msg_list["valid"]

    if valid:
        print("LOGIN IS GOOD PROCEED")
    else:
        print("INVALID LOGIN")

def tag_results_callback(client, userdata, msg):

    # message decdoing then convert from JSON to list
    msg_decode = str(msg.payload.decode("utf-8","ignore"))
    msg_list = json.loads(msg_decode)

    print(msg_list)

# function for pressing 1) on the menue
def start_login(client):
	# print the heading
	print("\n******LOGIN SCREEN******\n")

	# get user name and password
	user_id = input("Enter User: ")
	password_id = input("Enter Password: ")

	# list of infomration  then convert to JSON
	info = {
            "user_id": user_id,
            "password_id" : password_id
            }
	infoJson = json.dumps(info)

	# publish message
	client.publish("dwm/holo/login", infoJson)

    #print that it is beeing added
	print("Publishing...\n")

# function for pressing 2) on the menue
def start_tag(client):
    # print the heading
    print("\n******TAG SCREEN******\n")

    tag = input("Enter Tag: ")
    # list of infomration  then convert to JSON
    info = {"tag_id": tag,
            "user_id" : "test",
            "password_id" : "pass"
            }
    infoJson = json.dumps(info)
    # publish message
    client.publish("dwm/holo/requesttaginfo", infoJson)

    #print that it is beeing added
    print("Publishing...\n")

# this fucntion is for testing the DWM network message with the hololense
def start_dwm(client):

    #get tag info for sending over mqtt
    tag = input("Enter Tag ID: ")
    nodeType = input("Enter ANCHOR/TAG: ") # no error checking just trust
    x = input("Enter X cord: ")
    y = input("Enter Y cord: ")
    z = input("Enter Z cord: ")

    # list
    info = {

            "configuration" : {
                                "nodeType" : nodeType

                                },

            "loc" : {
                        "x" : x,
                        "y" : y,
                        "z" : z

                    }

            }

    # turn list into json and publish to the fake dwm network
    infoJson = json.dumps(info)
    pub_topic = "dwm/node/"+tag+"uplink/config"
    client.publish(pub_topic, infoJson)

    # print publishing with message for debugging
    print("Publishing: \n")
    print(infoJson)


# fuction for starting the connection and prompting user options
def start():
    #broker to connect to
    broker = "test.mosquitto.org"
    client = mqtt.Client("arkards_holo")

    # set the callback fucntions for connection and log
    client.on_connect = on_connect
    #client.on_log = on_log

    # connect to the broker
    print("Connecting to broker: " + broker)
    client.connect(broker)

    # set the callback functions for the topics
    client.message_callback_add("dwm/node/loginresults", login_results_callback)
    client.message_callback_add("dwm/node/tag", tag_results_callback)

    # subscribe to the result topics for check the data sent to the database
    client.subscribe("dwm/node/tag")
    client.subscribe("dwm/node/loginresults")

    # start the loop for call backs to be processed
    client.loop_start()

    #loop unit we get a correct answer then execute
    while(1):
        # wait 1 second before printing screen
        time.sleep(1)
        # print the heading and the options
        print("************************************************")
        print("*          WELCOME - PYTHON MQTT               *")
        print("************************************************")
        print("Please Select Option:")
        print("\t1) Send Test Login")
        print("\t2) Send Test Tag")
        print("\t3) Send DWM Config")
        print("\t4) Exit program")

        mode = input("\nInput: ") #user input

        # if user presses one then simulated the login function
        if mode == "1":
        	start_login(client)
        #if user pressed two then simulated the tag function
        elif mode == "2":
        	start_tag(client)
        #if user pressed two then simulated the tag function
        elif mode == "3":
            start_dwm(client)
        # if user presses three then stop loop disconnect and exit application
        elif mode == "4":
        	print("EXITING...")
        	client.loop_stop()
        	client.disconnect()
        	sys.exit(0)
        else:
        	print("INVALID MODE PLEASE TRY AGAIN!\n")

start()
