#include libraries
from time import sleep

#this flag is used to exit the program when "end of transfer" message is detected: {0}
exitFlag = 0

#set source and destination MAC addresses
senderMAC = g_ethernet_msg.mac_address_source = Stimulation.get_mac()
g_ethernet_msg.mac_address_destination = Logging.get_mac()

#receving function
def on_eth_msg_received(msg):
    global exitFlag
    if msg.mac_address_source == senderMAC:
        print "Receiver: Received message: [{1}]".format(senderIP, msg)
        if msg.payload[0]==0:
            exitFlag = 1

try:
    #set receiving function and start capturing
    g_ethernet_msg.on_message_received += on_eth_msg_received
    g_ethernet_msg.start_capture()
    while exitFlag == 0:
        sleep(1)
    #show an status message
    print("Receive: All frames received successfully. Ending receiver script ...")

finally:
    g_ethernet_msg.on_message_received -= on_eth_msg_received
    g_ethernet_msg.stop_capture()
