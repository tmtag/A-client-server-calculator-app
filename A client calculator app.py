DEST_IP_ADDR = '127.0.0.1'
DEST_PORT = 65432
BUF_SIZE = 1024
stop_mes = {'', 'quit', 'Quit', 'QUIT', 'stop', 'Stop', 'STOP'}

from socket import socket, AF_INET, SOCK_STREAM

with socket(AF_INET, SOCK_STREAM) as s:
    s.connect((DEST_IP_ADDR, DEST_PORT))
    sent_message = input("Your message: ")
    s.send(sent_message.encode())
    print(f"Sent message: {sent_message}")
    if sent_message not in stop_mes:
        message = s.recv(BUF_SIZE)
        print(f"Recv message: {message.decode()}")
    else:
            print("Stoped.")
