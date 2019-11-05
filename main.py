import connect_telnet
import telnetlib
import test
import time
import routerConfig
import os



class Main(object):
    def __init__(self):
        self.obj3 = routerConfig.RouterConfig()


    def menu_principal(self):
        op = 1

        while (op != 0):
            op = int(input("Digite a opcao o indice do caso de teste: "))
            if(op !=0):
                pass
            else:
                break

if __name__ == "__main__":
    obj = Main()
    obj.menu_principal()