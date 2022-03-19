#include libraries
from time import sleep

#this flag is used to exit the program when "end of transfer" message is detected: {0}
exitFlag = 0

#set source and destination MAC addresses
senderIP = g_ipv4_msg.ip_header.ip_address_source = Simulation.get_ip()
g_ipv4_msg.ip_header.ip_address_destination = Logging.get_ip()

#receving function
def on_eth_msg_received(msg):
    global exitFlag
    if msg.ip_header.ip_address_destination == senderIP:
        print "Receiver: Received message: [{1}]".format(senderIP, msg)
        if msg.payload[0]==0:
            exitFlag = 1
    
try:
    #set receiving function and start capturing
    g_ipv4_msg.on_message_received += on_eth_msg_received
    g_ipv4_msg.start_capture()
    while exitFlag == 0:
        sleep(1)
    #show an status message
    print("Receive: All frames received successfully. Ending receiver script ...")
    
finally:
    g_ipv4_msg.on_message_received -= on_eth_msg_received
    g_ipv4_msg.stop_capture()
    