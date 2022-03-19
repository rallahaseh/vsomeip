from globals import *

someip_msg = message_builder.create_someip_message()

# set source and destination IP and Mac addresses
someip_msg.ip_header.ip_address_source = "192.168.0.210"
someip_msg.ip_header.ip_address_destination = "192.168.0.28"
someip_msg.ethernet_header.mac_address_source = "00:13:3B:B0:11:0A"
someip_msg.ethernet_header.mac_address_destination = "08:00:27:6B:2A:9E"

#set source and destination port numbers
someip_msg.transport_header.port_destination = 30509
someip_msg.transport_header.port_source = 30610

#set important header filds
someip_msg.someip_header.message_id = 0x11113333
someip_msg.someip_header.request_id = 0x44440001
someip_msg.someip_header.protocol_version = 0x01
someip_msg.someip_header.interface_version = 0x00
someip_msg.someip_header.message_type = MessageType.REQUEST
someip_msg.someip_header.return_code = ReturnCode.E_OK

#set payload data to send "World"
someip_msg.payload = System.Array[Byte]([0x57, 0x6f, 0x72, 0x6c, 0x64])

#send message
someip_msg.send()
