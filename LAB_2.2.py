from netmiko import ConnectHandler


sshCli = ConnectHandler(
        device_type= 'cisco_ios',
        host='10.10.20.70',
        port= 2221,
        username='admin',
        password= 'admin'
        )

output = sshCli.send_command("show ip int brief", read_timeout=15, expect_string=r"#")
print("show ip int brief:\n{}\n".format(output))

config_commands = [
    'int loopback 1',
    'ip address 2.2.2.2 255.255.255.0',
    'description WHATEVER'
    ]

output = sshCli.send_config_set(config_commands, read_timeout=15)
print(output)
