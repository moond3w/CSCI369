<b>Author: Chai Guo Liang</b>
<hr>
# To run the program:

1. On your Kali Linux, run the following command:
	nc -v -l -p 5555

2. On your Ubuntu, navigate to the this folder (Q1) and run the following command:
	python3 backdoor.py

3. Go back to your Kali Linux and start entering the commands.

4. To end the program, enter "&" on your Kali Linux.

<hr>
# Notes:

1. Ensure the IP address in "kali_ip" variable is set up to match your Kali IP.

2. Ensure Ubuntu and Kali Linux are sharing the same NAT Network.

<hr>
# Supported commands:

1. Non-interactive commands such as "ls", "pwd", "cat <text.txt>"...

2. Changing directories with "cd <dir>"
	Note: Commands to open text editors such as gedit will open in the target PC (Ubuntu) and can only be closed on their end!
