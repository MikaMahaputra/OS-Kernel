import socket

HEADER = 64
PORT = 6050 #target port
FORMAT = 'utf-8' #message formatting
DISCONNECT_MESSAGE = "!DISCONNECT" #disconnect message
SERVER = "172.20.160.1" #target ip addess
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket type
client.connect(ADDR)

def send(msg): #message sender
    message = msg.encode(FORMAT) #encode messsage into utf
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) # padding to 64 for validation
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT)) # to recieve message from server

send("hello world")
input() #press enter to send next message
send("hello mada")
input()
send("hello mika")
send(DISCONNECT_MESSAGE) # disconnects server by sending the message
print("connection terminated")