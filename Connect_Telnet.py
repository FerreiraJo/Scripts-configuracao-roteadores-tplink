import telnetlib
import time


class ConnectTelnet(object):
    def __init__(self, ip="192.168.0.1", user_name="admin", password="admin", port=23):
        self._ip = ip
        self._user_name = user_name
        self._password = password
        self._port = port
        self._timeout = 20
        self._tn = None

    @property
    def ip(self):
        return self.ip

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
        return self.password

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

    def connect(self):
        try:
            self._tn = telnetlib.Telnet(self.ip)
        except:
            print("Connect error")
            return 1
        return 0

    def login(self):
        self._tn.write(self._user_name.encode('ascii') + b"\n")   #DEBUG
        time.sleep(1)
        print('Log: {}'.format(self._tn.read_until(b'password:')))     #DEBUG
        self._tn.write(self._password.encode('ascii') + b"\n")
        return self._tn, self._tn.read_until(b'TP-LINK(conf)#')   #DEBUG


if __name__ == "__main__":
    obj = ConnectTelnet()
    print(obj._ip)
    obj.connect()
    obj.login()
