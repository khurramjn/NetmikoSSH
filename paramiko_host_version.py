import paramiko
import time
import re


class SSH:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def terminal_length(self, device):
        output = device.send("terminal length 0\n")
        time.sleep(1)
        return output

    def ssh_command(self, command):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(self.hostname, self.port, self.username, self.password)
        device = ssh_client.invoke_shell()
        self.terminal_length(device)
        device.send(command)
        time.sleep(7)
        output = device.recv(65000).decode("ascii")
        print(output)
        hostname = re.search(r"(.+)#", output)
        ver = re.search(r"(Version\s+\S+),", output)

        with open("text.txt", "a") as file_name:
            print(
                "{0} {1} {4} {2} {4} {3} ".format(
                    "hostname: ",
                    hostname.group(0),
                    "Version: ",
                    ver.group(0)[:-1],
                    "\t",
                ),
                file=file_name,
            )


obj = SSH(hostname="IP", port=22, username="username", password="password")
obj.ssh_command("show version \n")
