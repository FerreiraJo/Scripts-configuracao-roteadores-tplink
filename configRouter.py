''' Script de configuração do roteador TL-WR849N '''


import getpass
import sys
import telnetlib
import time



HOST = input("Entre com o endereco de IP: ")
user = input("Entre com o username: ")
password = input("Entre com o password: ")

tn = telnetlib.Telnet(HOST)

def login():
    time.sleep(1)
    print(tn.read_until(b"username:"))
    tn.write(user.encode('ascii') + b"\n")
    time.sleep(1)
    print(tn.read_until(b"password:"))
    tn.write(password.encode('ascii') + b"\n")

def set_config(c):
    time.sleep(3)
    tn.write(c.encode('ascii') + b"\n")
    time.sleep(15)
    tn.close()

def teste():
    tn.write(b"wlctl set --sec none\n")
    time.sleep(15)
    tn.close()
    

''' lista de comandos wifi '''

'''comando set - serve para definir uma configuracao wifi '''
comando0 = "wlctl set "

'''comando ssid '''
comando1 = "--ssid "

''' lista de parametros de criptografia '''
par0 = "--sec none"
par1 = "--sec wep auto 1111111111 1"
par2 = "--sec wep open 1111111111 2"
par3 = "--sec wep shared 1111111111 3"
par4 = "--sec psk auto auto 12345678"
par5 = "--sec psk wpa tkip 12345678"
par6 = "--sec psk wpa2 aes 12345678"


opcao=1
print("0 - SEM CRIPTOGRAFIA")
print("1 - Crip. WEP, OPEN, 4")
print("2 - Crip. WEP, OPEN, 4")
print("3 - Crip. WEP, SHARED, 4")
print("4 - PSK, crip. AUTO, chave AUTO")
print("5 - PSK, crip. WPA, chave TKIP")
print("6 - PSK, crip. WPA2, chave AES")
print("7 - Teste")
print("99- sair")

while (opcao != 99):
    opcao=int(input("Digite a opcao desejada: "))
    if(opcao == 99):
        break
    login()
    if(opcao == 99):
        break
    elif(opcao == 0):
        set_config(comando0+par0)
    elif(opcao == 1):
        set_config(comando0+par1)
    elif(opcao == 2):
        set_config(comando0+par2)
    elif(opcao == 3):
        set_config(comando0+par3)
    elif(opcao == 4):
        set_config(comando0+par4)
    elif(opcao == 5):
        set_config(comando0+par5)
    elif(opcao == 6):
        set_config(comando0+par6)
    elif(opcao ==7):
        teste()
    else:
        print("Opcao invalida")
        
        






