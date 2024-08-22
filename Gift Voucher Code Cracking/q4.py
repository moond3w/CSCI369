from scapy.all import *

# Executable Server details
dst_ip = "10.0.2.15"
dst_port = 12449

# Client ID
client_id = "7910939"

# Crafting the UDP packet
source_port = 54321 # random sport
packet = IP(dst=dst_ip)/UDP(sport=source_port, dport=dst_port)/Raw(load=client_id)

# Send a packet and wait for response
response = sr1(packet, timeout=3)

if response:
    print(response.show())
else:
    print("No response received.")