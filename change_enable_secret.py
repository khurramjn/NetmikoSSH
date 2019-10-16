from netmiko import ConnectHandler

ip_list = ["192.1.1.1", "192.1.1.2"]
send_config_commands = ["enable secret secret_here"]
send_write_memory = "wr mem"


def ssh_begin():

    for devices in ip_list:
        print(devices)
        device = ConnectHandler(
            ip=devices, username="admin", password="admin", device_type="cisco_ios"
        )
        print(device.find_prompt())
        print("#" * 80)
        print(device.send_config_set(send_config_commands))
        print(device.send_command(send_write_memory))
        print("#" * 80, "\n")


if __name__ == "__main__":
    ssh_begin()
