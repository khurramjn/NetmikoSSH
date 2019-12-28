# Python 3
# print(netmiko.__version__)
# 2.3.3

from netmiko import ConnectHandler

device = ConnectHandler(
    ip="10.0.8.18",
    username="admin",
    password="Your-Password",
    device_type="cisco_ios_telnet",
)

print(device.find_prompt())
print(device.send_command("sh ip int bri"))
device.disconnect()
