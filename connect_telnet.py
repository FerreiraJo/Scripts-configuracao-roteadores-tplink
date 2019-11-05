import telnetlib
import time
import test


class ConnectTelnet(object):
    def __init__(self, ip="192.168.0.1", user_name="admin", password="admin", port=23):
        self._ip = ip
        self._user_name = str(user_name)
        self._password = str(password)
        self._port = port
        self._timeout = 20

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, ip_address):
        self._ip = ip_address

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, n):
        self._user_name = n

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pas):
        self._password = pas

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, p):
        self._port = p

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, t):
        self._timeout = t

    def login(self):
        try:
            tn = telnetlib.Telnet(self._ip)
        except:
            tn = None
            print("Connect error")

        time.sleep(1)
        print(tn.read_until(b"username:"))
        tn.write(self._user_name.encode('ascii') + b"\n")
        time.sleep(1)
        print(tn.read_until(b"password:"))
        tn.write(self._password.encode('ascii') + b"\n" )
        tn.write(b"\n")
        time.sleep(1)
        print(tn.read_until(b"TP-LINK(conf)#"))
        time.sleep(1)

        return tn


if __name__ == "__main__":
    obj = ConnectTelnet()
    print(obj._ip)
    obj.login()

