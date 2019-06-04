from netmiko import ConnectHandler
import time
 
# yourbox is your Jump Box, in your case it's your Cisco Router 1
# ip is your JumpBox IP
# username is your JumpBox username
# Password is your JumpBox password
 
yourbox = {
    'device_type':'cisco_ios',
    'ip':'192.168.1.166',
    'username':'admin',
    'password':'YourJumpBoxPassword',
    }
	
def sshFunction():
    device = ConnectHandler(**yourbox)
    print(device.find_prompt())
    device.write_channel("ssh -l admin 192.168.1.167 \n")
    time.sleep(1)
    output = device.read_channel()
    print(output)
 
    if "Password: " in output:
        print(device.write_channel("YourCiscoRouter2Password\n"))
    time.sleep(1)
 
    print(device.send_command("sh ip int bri"))
    device.disconnect()
 
sshFunction()
