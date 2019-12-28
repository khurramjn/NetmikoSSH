#!/usr/bin/env python

import concurrent.futures
import csv
import os.path
import time

from netmiko import ConnectHandler

username = input("Enter the username: ")
password = input("Enter the password: ")
device_type = input("Enter the device_type: ")
file_path = input("Provide the full csv file path: ")
column_name = input("Provide the column name: ")


def ips_from_file(file_path, column_name):
    """
    Requires user to provide full file path and csv column name.
    """
    ip_list = list()

    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            ip_list.append(row[column_name])

    return list(filter(None, ip_list))


def ssh_connection(ip):
    """
    Establishes SSH session to the devices using netmiko module.
    """
    device = ConnectHandler(
        ip=ip,
        username=username,
        password=password,
        device_type=device_type,
        timeout=20,
    )
    output = device.send_command("sh run")
    with open("DEVICES_{}".format(ip), "w") as save_run:
        print(output, file=save_run)
    return output


def main():

    try:
        ips = ips_from_file(file_path, column_name)
    except FileNotFoundError:
        print("Please provide a valid IP file path")
        exit(1)
    except KeyError:
        print("Please provide a valid column name")
        exit(1)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(ssh_connection, devices) for devices in ips]

        for results in concurrent.futures.as_completed(results):
            print(results.result())


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"\n Time to complete: {end - start:.2f}s\n")
