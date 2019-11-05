
import json

class Test(object):
    def __init__(self, type_test = "ssid", case_test = 'CASO_3', command_test = "wlctl set 2g --ssid Teste_3"):
        self._case_test = case_test
        self._command_test = command_test
        self._type_test = type_test
        self.dict_test = {}
        self.list_test = []
        self.command_test = command_test


    def read_json(self):
        with open("Comandos.json", "r") as f:
            self.dict_test = json.load(f)
            self.list_test = self.dict_test["{}".format(self._type_test)]
            for x in range(len(self.list_test)):
                comandos = self.list_test
                for comando in comandos:
                     if self._case_test in comando:
                         return comando[self._case_test]

    def write_json(self):

        try:
            with open("Comandos.json", "r") as f:
                self.dict_test = json.load(f)
                self.list_test = self.dict_test["{}".format(self._type_test)]
                comandos = self.list_test
                label_test = str(self._case_test)
                comandos_test = str(self._command_test)
                list_test = {"{}".format(self._case_test): "{}".format(self._command_test)}
                comandos.append(list_test)
                f.close()
        except:
            print("Erro ao ler arquivo")
        try:
            with open("Comandos.json", "w") as f:
                json.dump(self.dict_test, f)
        except:
            print("Erro ao escrever no arquivo")


if __name__ == "__main__":

    op = 1

    while op != 99:
        op = input(("Digite 1 para editar e 99 para sair: "))
        if op == "99":
            break
        elif op == "1":
            print("Entre com os parâmetros")
            type = input("Entre com  tipo de teste (ex. ssid, wep, wpa, wpa2):")
            case = input("Entre com o caso de teste (ex. CASO_1):")
            command = input("Entre com o comando CLI do roteador:")
            obj = Test(type, case, command)

    #obj.read_json()

