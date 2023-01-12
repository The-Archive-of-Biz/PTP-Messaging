import socket
import threading

IP = "192.168.1.1" #change this to the IP address of the device you want to connect to
PORT = 1234

def receive_message(s):
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(data.decode())

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    receive_thread = threading.Thread(target=receive_message, args=(s,))
    receive_thread.start()
    while True:
        message = input("Enter message: ")
        s.sendall(message.encode())
    s.close()

if __name__ == "__main__":
    main()
