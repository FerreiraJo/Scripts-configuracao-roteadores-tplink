import connect_telnet
import telnetlib
import test
import time

class RouterConfig(connect_telnet.ConnectTelnet):
    def __init__(self):
        super().__init__()
        obj2 = connect_telnet.ConnectTelnet()
        self.tn = obj2.login()

    def send_command(self, c):
        time.sleep(3)
        self.tn.write(c.encode('ascii') + b"\n" )
        time.sleep(15)
        print(self.tn.read_until(b"TP-LINK(conf)#"))

    def get_command(self, type, case):
        te = test.Test(type, case)
        print(te)
        return te.read_json()


if __name__ == "__main__":
    obj = RouterConfig()

