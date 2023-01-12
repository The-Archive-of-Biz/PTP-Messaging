# PTP-Messaging
This script allows for sending and receiving messages between two devices over a Wi-Fi network. It uses the built-in socket and threading modules in Python.

## Requirements
Python 3.x
## Usage
Update the IP address in line 8 to the IP address of the device you want to connect to.
Run the script on both devices: python p2p_messaging.py
On one device, enter a message and press enter to send it to the other device. The message will be displayed on the receiving device's console.
The script will continue to run until the connection is closed or the script is interrupted.
## Note
This script is intended to be used as an example, it is not guaranteed to work in every situation. It is recommended to test the script in a controlled environment before using it in a production environment. 
