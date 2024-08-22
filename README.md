# CSCI369 Practice Codes
Collection of practice code used in CSCI369 Ethical Hacking. <br>
More information can be found in the respective folders.

# System Setup
The following systems are used for the collection of codes.
1. Kali Linux 2024.2 (https://www.kali.org/get-kali/#kali-installer-images)
2. Ubuntu 22.04 (https://releases.ubuntu.com/jammy/)
3. Metasploitable 2 (https://sourceforge.net/projects/metasploitable/files/Metasploitable2/)

Virtual Box was used to host the virtual machines found above.
<br>(https://www.virtualbox.org/wiki/Downloads)

# Connecting to the same NAT Network
For the program to work, having the 3 machines connected via the same NAT Network is necessary. This can be easily achieved through the use of VirtualBox.
1. Navigate to the Tools > Network > NAT Network.
2. Create a new NAT Network.
3. Go to the settings of each VM > Network > Attached to: > NAT Network and select the newly created NAT Network.
4. Boot up two different VMs and attempt to ping each other to test if the VMs share the same network.
