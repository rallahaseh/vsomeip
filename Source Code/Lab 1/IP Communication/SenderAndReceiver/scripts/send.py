#include libraries
from time import sleep

#used to add a sequence number to frames
count = 0

#set source and destination MAC addresses
g_ipv4_msg.ip_header.ip_address_source = Simulation.get_ip()
g_ipv4_msg.ip_header.ip_address_destination = Logging.get_ip()

#timer function
def on_elapsed(source, event_args):
    #inc counter
    global count
    count += 1
    #make message using value of count as it's first byte and then send it
    g_ipv4_msg.payload = System.Array[Byte](bytearray.fromhex('%02X'%count + "01 02 03"))
    g_ipv4_msg.send()
    #display a status message
    print("Sender: Frame" + '%02d'%count + " has been sent.")
    
try:
    #timer setup
    timer = andi.create_timer()
    timer.interval = 1000
    timer.on_time_elapsed += on_elapsed
    timer.start()
    #wait 20 seconds
    sleep(20)
    
finally:
    #send 'end of transfer' message : {0} this message ends receiver script
    print("Sender: Sending ""End of Transfer"" message to receiver...")
    g_ipv4_msg.payload = System.Array[Byte](bytearray.fromhex("00"))
    g_ipv4_msg.send()
    #different event
    timer.on_time_elapsed -= on_elapsed
    timer.stop()
    