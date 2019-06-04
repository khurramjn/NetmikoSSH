ou can use below script and it will disconnect the session after iterating over the list you have provided.

Assuming your passwords are same for all of the routers. This is just a basic script you can improve per your requirements.

from netmiko import ConnectHandler
import time
import csv
 
# yourbox is your Jump Box, in your case it's your Cisco Router 1
# ip is your JumpBox IP
# username is your JumpBox username
# Password is your JumpBox password
 
yourbox = {
    'device_type':'cisco_ios',
    'ip':'JumpBoxIP',
    'username':'admin',
    'password':'YourJumpBoxPassword',
    }
 
iplist = []
 
#def sshFunction():
device = ConnectHandler(**yourbox)
print(device.find_prompt())
	
with open('D:\\list_ip.csv') as fileName:
    read_File = csv.DictReader(fileName)
			
    for read in read_File:
        iplist.append(read['iplist1'])
		
for x in range(len(iplist)):
    time.sleep(2)
    device.write_channel("ssh -l admin " + iplist [x] + "\n")
    print("SSH connection established %s" % iplist [x], time.sleep(1), "\n")
    output = device.read_channel()
    print(output)
 
    if "Password: " in output:
        print(device.write_channel("YourCiscoRouter2Password\n"))
	time.sleep(2)
	
    print("Sending SSH command to the router", time.sleep(1), "\n")
    print(device.send_command("sh ip int bri"))
    time.sleep(2)
    print("Exiting the SSH Session for %s" % iplist [x], time.sleep(1), "\n")
    print(device.write_channel("exit\n"))
 
device.disconnect()
#sshFunction()
