import ast
from time import sleep



def readFile(file):
    return open(file).readlines()


def moveTo(room):
    global currentRoom
    currentRoom = room
    print(places[currentRoom]["Des"])


JSON = ast.literal_eval(" \n ".join(readFile("World.json")))
commands = ast.literal_eval(" \n ".join(readFile("Commands.json")))
currentRoom = "unknown"
places = JSON["Places"]
startPlace = JSON["StartPlace"]
inventory = []
win = False
moveTo(startPlace)

print("Type 'help' for help.")





while not win:
    command = input("> ").lower().split(" ")
    if command[0] in commands:
        if len(command)-1 >= len(commands[command[0]]["args"]):
            code = " \n".join(commands[command[0]]["code"])
            code = code.replace("import","print('Security risk!')")
            code = code.replace("open","print('Security risk!')")
            code = code.replace("exec","print('Security risk!')")
            code = code.replace("eval","print('Security risk!')")
            newCommand = list(command)
            if len(commands[command[0]]["args"]) > 0:
                for i in range(len(commands[command[0]]["args"])):
                    del(newCommand[0])
                newCommand = " ".join(newCommand)
                if len(command)-1 > len(commands[command[0]]["args"]):
                    for i in range((len(command)-1)-len(commands[command[0]]["args"])):
                        del command[len(command)-len(commands[command[0]]["args"])]
                del command[len(command)-1]
                command.append(newCommand)
            if "Security risk!" in code:
                print("Sercurity risk!")
                print("Bad code: \n")
                print(" \n".join(commands[command[0]]["code"]))
                assert False, "Either import, open, exec or eval were used in Commands.txt"
            else:
                exec(code)
        else:
            print("Error: Missing " + str(len(commands[command[0]]["args"]) - (len(command)-1)) + " required argument(s).")
    else:
        print("Unknown command, type 'help' for help.")


