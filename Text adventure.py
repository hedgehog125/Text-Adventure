import os
from AutoUpdate import AutoUpdate
AutoUpdate.database = "https://raw.githubusercontent.com/hedgehog125/Text-Adventure-Database/master/database/"
AutoUpdate.path = "AutoUpdate/"
AutoUpdate.init()

def runFile(file):
    exec(open(file, "r").read(), globals())

os.chdir("Assets/")
import Code
