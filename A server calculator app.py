def calc(string):
    array = []
    output = ""
    for c in string:
        array.append(c)
    if array[0] == '+':
        output = int(array[2]) + int(array[4])
    elif array[0] == '-':
        output = int(array[2]) - int(array[4])
    elif array[0] == '*':
        output = int(array[2]) * int(array[4])
    elif array[0] == '/':
        output = int(array[2]) / int(array[4])
    
    return output

def count_case(string):
    letters, digits = 0, 0
    for i in string:
        if i.isalpha() == True:
            letters = letters + 1
        elif i.isdigit() == True:
            digits = digits + 1
    return letters, digits


IP_ADDR = '127.0.0.1'
PORT = 65432
BUF_SIZE = 1024
stop_mes = {'', 'quit', 'Quit', 'QUIT', 'stop', 'Stop', 'STOP'}

from socket import socket, AF_INET, SOCK_STREAM

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((IP_ADDR, PORT))
    s.listen()
    while True:
        print("Waiting for a new connection")
        conn, addr = s.accept()
        print(f"Accepted conn req from {addr}")
        data = conn.recv(BUF_SIZE)
        c = count_case(data.decode('utf-8'))
        if data not in stop_mes:
            if c[0] == 0 and c[1] != 0:
                cal = str(calc(data.decode('utf-8')))
                conn.send(cal.encode)
            else:
                print(f"Recv message:   {data.decode()}")
                conn.send(data)
                print(f"Echoed message:   {data.decode()}")
        else:
            print("The client finished sending.\t\n Closing the connection.")
            conn.close()
            break
    print("Server is shutting down.")

