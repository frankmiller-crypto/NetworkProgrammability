from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.10',
    'username': 'cisco',
    'password': 'class',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.0.20',
    'username': 'cisco2',
    'password': 'class',
}


all_devices = [iosv_l2_s2,iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
       print ("<=============== Creando VLAN " + str(n) + "===============>")
       print()
       config_commands = ['vlan ' + str(n), 'name Python_VLAN'+str(n)]
       output = net_connect.send_config_set(config_commands)
       print (output)
       print() 
       print ("<===============VLAN " + str(n) + " creada correctamente" + "===============>")
       print() 
