import Token
import Fundus

class Cmd:
    quitConsole = False
    userInput = ""
    fundus = Fundus.Fundus()

    def execute_help(self):
        print("HELP")

    def execute_fail(self):
        print("FAIL")

    def parse(self, cmd):
        # print(cmd)
        global quitConsole
        if cmd == Token.QUIT:
            self.quitConsole = True
        elif cmd == Token.PUT:
            self.fundus.execute_put()
        elif cmd == Token.CREATE_CONTAINER:
            self.fundus.execute_create_container()
        elif cmd == Token.CREATE_ITEM:
            self.fundus.execute_create_Item()
        elif cmd == Token.SHOW:
            self.fundus.execute_show()
        elif cmd == Token.HELP:
            self. execute_help()
        else:
            self. execute_fail()

    def command_loop(self):
        while not self.quitConsole:
            self.userInput = input("Enter Command: ")
            self.parse(self.userInput)
