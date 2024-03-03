from socket import *

def ask_user_input():
    command = input("Enter command (Random/Add/Subtract): ")
    number1 = input("Enter first number: ")
    number2 = input("Enter second number: ")
    return f"{command};{number1};{number2}"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('localhost', 8080))

while True:
    try:
        user_input = ask_user_input()
        clientSocket.send(user_input.encode())
        response = clientSocket.recv(1024).decode()
        print("Server response:", response)
    except KeyboardInterrupt:
        print("Closing client...")
        break

clientSocket.close()