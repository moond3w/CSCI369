<b>Author: Chai Guo Liang</b>

<h2>To run the program:</h2>

1. On your Kali Linux, run the following command:
<br><code>nc -v -l -p 5555</code>

2. On your Ubuntu, navigate to the this folder (Q1) and run the following command:
<br><code>python3 backdoor.py</code>

3. Go back to your Kali Linux and start entering the commands. The available commands can be found below.

4. To end the program, enter <code>&</code> on your Kali Linux.


<h2>Notes:</h2>

1. Ensure the IP address in "kali_ip" variable is set up to match your Kali IP.

2. Ensure Ubuntu and Kali Linux are sharing the same NAT Network.

<h2>Supported Commands:</h2>

1. Non-interactive linux commands such as <code>ls</code>, <code>pwd</code>, <code>cat <text.txt></code>...

2. Changing directories with <code>cd \<dir\></code>

Note: Commands to open text editors such as gedit will open in the target PC (Ubuntu) and can only be closed on their end!
