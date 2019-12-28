# Python3
import netmiko

device = ConnectHandler(ip='192.168.1.172', username='admin', password='Your-Password', device_type='cisco_ios')
print(device.find_prompt())

if x in range(2,10):
     print('Creating VLAN' +str(x))
     config_command = ['vlan ' + str(x)]
     print(device.send_config_command(config_command))

print(device.disconnect())
