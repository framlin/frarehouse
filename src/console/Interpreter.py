import Token

class Cmd:
    quitConsole = False
    userInput = ""

    def execute_put(self):
        print("PUT")

    def execute_create_container(self):
        print("CREATE_CONTAINER")

    def execute_create_Item(self):
        print("CREATE_ITEM")

    def execute_show(self):
        print("SHOW")

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
            self.execute_put()
        elif cmd == Token.CREATE_CONTAINER:
            self.execute_create_container()
        elif cmd == Token.CREATE_ITEM:
            self.execute_create_Item()
        elif cmd == Token.SHOW:
            self.execute_show()
        elif cmd == Token.HELP:
            self. execute_help()
        else:
            self. execute_fail()

    def command_loop(self):
        while not self.quitConsole:
            self.userInput = input("Enter Command: ")
            self.parse(self.userInput)
