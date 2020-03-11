import os
from pathlib import Path
import subprocess
import shutil

class Fundus:
    fundusPath = "../../data/fundus"
    stockPath = "../../data/stock"
    dataPath = "../../data"
    binPath = "../../bin"
    tmpPath = "../../data/tmp"
    basketPath = "../../data/basket"

    def execute_put(self):
        item = input("Item: ")
        container = input("Container: ")
        print("put Item " + item + " into " + container)
        itemPath = self.find(item)
        containerPath = self.find(container)
        shutil.move(itemPath, containerPath)
        print(os.listdir(containerPath))

    def execute_take(self):
        item = input("Item: ")
        print("take Item " + item)
        itemPath = self.find(item)
        shutil.move(itemPath, self.basketPath)
        print(os.listdir(self.basketPat))

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

    def find(self, item):
        return subprocess.run(['find', self.dataPath, '-name', item], capture_output=True).stdout.decode(
            'utf-8').rstrip()

    def find_in(self, container):
        return subprocess.run(['find', container, '-name', '*-*'], capture_output=True).stdout.decode(
            'utf-8').rstrip()

    def show_item(self, item, itemPath):
        htmlPath = self.tmpPath + '/' + item + '.html'
        copyPath = shutil.copy(itemPath, htmlPath)
        print("Item: ", itemPath)
        subprocess.run([self.binPath + '/show', copyPath])

    def show_container(self, container, itemPath):
        itemlist = self.find_in(itemPath)
        htmlPath = self.tmpPath + '/' + container + '.html'
        pre_html = '<html lang = "de" ><head></head><body><pre>'
        foot_html = '</pre></body></html>'
        fobj_out = open(htmlPath, "w")
        fobj_out.write(pre_html)
        fobj_out.write(itemlist)
        fobj_out.write(foot_html)
        fobj_out.close()
        subprocess.run([self.binPath + '/show', htmlPath])

    def execute_show(self):
        print("SHOW")
        item = input("Item: ")
        itemPath = self.find(item)
        if os.path.isdir(itemPath):
            self.show_container(item, itemPath)
        elif os.path.isfile(itemPath):
            self.show_item(item, itemPath)
