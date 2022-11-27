from netmiko import ConnectHandler

sshCli = ConnectHandler(
        device_type= 'cisco_ios',
        host='10.10.20.70',
        port= 2221,
        username='admin',
        password= 'admin'
        )

output = sshCli.send_command("show ip int brief")
print("show ip int brief:\n{}\n".format(output))
