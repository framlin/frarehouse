import Token
import os
from pathlib import Path
import subprocess
import shutil

class Cmd:
    quitConsole = False
    userInput = ""
    fundusPath = "../../data/fundus"
    stockPath = "../../data/stock"
    dataPath = "../../data"

    def execute_put(self):
        item = input("Item: ")
        container = input("Container: ")
        print("put Item " + item + " into " + container)
        itemPath = subprocess.run(['find', self.dataPath, '-name', item], capture_output=True).stdout.decode('utf-8').rstrip()
        containerPath = subprocess.run(['find', self.dataPath, '-name', container], capture_output=True).stdout.decode('utf-8').rstrip()
        shutil.move(itemPath, containerPath)
        print(os.listdir(containerPath))

    def execute_create_container(self):
        print("CREATE_CONTAINER")
        container = input('Container: ')
        container_path = self.stockPath + "/" + container

        if not os.path.exists(container_path):
            os.makedirs(container_path)
            print("Container " + container_path + " created")

    def execute_create_Item(self):
        print("CREATE_ITEM")
        item = input('Item: ')
        item_path = self.stockPath + "/" + item

        Path(item_path).touch()
        print("Item " + item_path + " created")


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
