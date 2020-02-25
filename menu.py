import os
from netmiko import ConnectHandler

 
def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system("cls")
    print ("==============================================") 
    print ("Selecciona una opción")
    print ("\t1 - Mostrar interfaces")
    print ("\t2 - Mostrar configuración de los equipos")
    print ("\t3 - Aplicar configuración (Crear 20 VLANS)")
    print ("\t4 - Salir")
    print ("==============================================") 


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

def interfaces():
    for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        net_connect.find_prompt()
        output = net_connect.send_command('show ip int brief')
        print (output)

def mostrar():
    for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        net_connect.find_prompt()
        output2 = net_connect.send_command('show run')
        print (output2)
    

def configuracion():
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



 
while True:
    # Mostramos el menu
    menu()
 
    # solicituamos una opción al usuario
    opcionMenu = input("Selecciona una opción: ")
 
    if opcionMenu=="1":
        print ("")
        interfaces()
        input("Interfaces mostradas \nPulsa enter para continuar")
    elif opcionMenu=="2":
        print ("")
        mostrar()
        input("Configuración de los equipos\nPulsa enter para continuar")
    elif opcionMenu=="3":
        print ("")
        configuracion()
        input("Se han configurado exitosamente\nPulsa enter para continuar")	
    elif opcionMenu=="4":
        break
    else:
        print ("")
        input("No has seleccionado ninguna opción correcta...\nPulsa enter para continuar")