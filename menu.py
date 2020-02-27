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
    print ("\t3 - Mostrar vecinos")
    print ("\t4 - Mostrar version de los equipos")
    print ("\t5 - Aplicar configuración (Crear 20 VLANS)")
    print ("\t6 - Replicar configuración (VTP,SPT,Port-Channel,SNMP server,Port-security)")
    print ("\t7 - Salir")
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

with open('iosv_l2_access.txt') as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [iosv_l2_s2,iosv_l2_s1]

def interfaces():
    for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        net_connect.find_prompt()
        output = net_connect.send_command('show ip int brief')
        print ("============================================================================================") 
        print (output)
        print ("============================================================================================") 

def mostrar():
    for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        net_connect.find_prompt()
        output = net_connect.send_command('show run')
        print ("============================================================================================")
        print (output)
        print ("============================================================================================")
    

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

def detodounpoco():
    for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        output = net_connect.send_config_set(lines)
        print (output)
            
def vecinos():
    for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        net_connect.find_prompt()
        output = net_connect.send_command('show cdp neighbors')
        print ("============================================================================================")
        print (output)
        print ("============================================================================================")

def inventario():
    for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        net_connect.find_prompt()
        output = net_connect.send_command('show version')
        print ("============================================================================================")
        print (output)
        print ("============================================================================================")
      



 
while True:
    # Mostramos el menu
    menu()
 
    # solicituamos una opción al usuario
    opcionMenu = input("Selecciona una opción: ")
 
    if opcionMenu=="1":
        print ("")
        interfaces()
        print("Interfaces mostradas \nPulsa enter para continuar")
    elif opcionMenu=="2":
        print ("")
        mostrar()
        print("Configuración de los equipos\nPulsa enter para continuar")
    elif opcionMenu=="3":
        print ("")
        vecinos()
        input("Estos son tus vecinos\nPulsa enter para continuar")
    elif opcionMenu=="4":
        print ("")
        inventario()
        input("Estas son las versiones de tus equipos\nPulsa enter para continuar")
    elif opcionMenu=="5":
        print ("")
        configuracion()
        input("Han sio creada las 20 vlans en cada equipo\nPulsa enter para continuar")
    elif opcionMenu=="6":
        print ("")
        detodounpoco()
        input("Su configuración ha sido replicada en todos los equipos\nPulsa enter para continuar")	    		
    elif opcionMenu=="7":
        break
    else:
        print ("")
        input("No has seleccionado ninguna opción correcta...\nPulsa enter para continuar")