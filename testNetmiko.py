from netmiko import ConnectHandler

sshovercli = ConnectHandler(device_type='cisco_ios', host='192.168.56.101', port=22, username='cisco', password='cisco123!')
#ssh por puerto 22

#Configuracion de la interfaz de loopback
configCommands = ['int loopback1','ip address 1.2.3.4 255.255.255.0', 'description loopback over ssh']
outputConfig = sshovercli.send_config_set(configCommands)
print("Config output from device:\n{}".format(outputConfig))

# Sacamos por pantalla el resumen de las interfaces
output = sshovercli.send_command("show ip interface brief")   # Tambien funciona con la forma abreviada
print("show ip interface brief: \n{}".format(output))

