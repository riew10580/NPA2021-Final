from netmiko import ConnectHandler
device_ip = '10.0.15.107'
username = 'admin'
password = 'cisco'

device_params = {'device_type': 'cisco_ios',
                 'ip': device_ip,
                 'username': username,
                 'password': password
                }

with ConnectHandler(**device_params) as ssh:
    result = ssh.send_command('sh ip int bri')

if 'Loopback' in result:
    with ConnectHandler(**device_params) as ssh:
        command_sequence = ['conf t', 'no int lo 62070138', 'end', 'sh ip int bri']
        output = ssh.send_config_set(command_sequence)
        print(output)
        
else:
    with ConnectHandler(**device_params) as ssh:
        command_sequence = ['conf t', 'int lo 62070138', 'ip addr 192.168.1.1 255.255.255.0', 'end', 'sh ip int bri']
        output = ssh.send_config_set(command_sequence)
        print(output)
        
