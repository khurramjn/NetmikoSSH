# Python3
from netmiko import ConnectHandler
import csv

iplist = []

# Read the CSV file and Column name is "iplist1"
with open('ipfile.csv') as fileName:
    readFile = csv.DictReader(fileName)
    for read in readFile:
        iplist.append(read['iplist1'])

def createVlan():
    for ipAddr in range(len(iplist)):
        device = ConnectHandler(ip=iplist [ipAddr], username='admin', password='123.com', device_type='cisco_ios')
        print(device.find_prompt())
        for x in range(2,5):
            print('Creating VLAN' + str(x))
            config_command = ['vlan ' + str(x), 'name Python-Created' + str(x)]
            print(device.send_config_set(config_command))
            print(config_command)
    print(device.disconnect())
createVlan()
