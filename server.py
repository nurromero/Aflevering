from socket import *
import threading
import random

def process_request(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data: 
                break

            command, number1, number2 = data.split(';')
            number1, number2 = int(number1), int(number2)

            if command == "Random":
                result = random.randint(number1, number2) 
            elif command == "Add":
                result = number1 + number2
            elif command == "Subtract":
                result = number1 - number2
            else:
                result = "Unknown command, try again."

            response = str(result)
            client_socket.send(response.encode())
        except ValueError:
            response = "Invalid request format. Write it like this: Add;1;6 'Add/Subtract;Number1;Number2'"
            client_socket.send(response.encode())

    client_socket.close()

server_port = 8080
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(5)
print('Server is ready.')

while True:
    connection_socket, addr = server_socket.accept()
    threading.Thread(target=process_request, args=(connection_socket,)).start()
