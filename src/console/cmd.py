import Token

userInput = ""
quitConsole = False;

def executePut():
    print("PUT")

def executeCreateContainer():
    print("CREATE_CONTAINER")

def executeCreateItem():
    print("CREATE_ITEM")

def executeShow():
    print("SHOW")

def executeHelp():
    print("HELP")

def executeFail():
    print("FAIL")

def parse(cmd):
    # print(cmd)
    global quitConsole
    if cmd == Token.QUIT:
        quitConsole = True
    elif cmd == Token.PUT:
        executePut()
    elif cmd == Token.CREATE_CONTAINER:
        executeCreateContainer()
    elif cmd == Token.CREATE_ITEM:
        executeCreateItem()
    elif cmd == Token.SHOW:
        executeShow()
    elif cmd == Token.HELP:
        executeHelp()
    else:
        executeFail()


while not quitConsole:
    userInput = input("Enter Command: ")
    parse(userInput)

