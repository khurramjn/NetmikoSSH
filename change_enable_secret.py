from netmiko import ConnectHandler
import csv

ip_list = ['10.0.1.1', '10.0.1.20']
send_config_commands = ['enable secret secret_here']
send_write_memory = 'wr mem'

def ssh_begin():

    for devices in ip_list:
        print(devices)
        device = ConnectHandler(ip = devices, 
                                username = 'admin', 
                                password = 'password', 
                                device_type = 'cisco_ios')
        print(device.find_prompt())
        print('#' * 80)
        print(device.send_config_set(send_config_commands))
        print(device.send_command(send_write_memory))
        print('#' * 80, '\n')


if __name__ == "__main__":
    ssh_begin()

    
