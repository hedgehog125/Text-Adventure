import os
from AutoUpdate import AutoUpdate
AutoUpdate.database = "https://raw.githubusercontent.com/hedgehog125/Text-Adventure-Database/master/database/"
AutoUpdate.path = "AutoUpdate/"
AutoUpdate.init()

os.chdir("Assets/")
from Assets import Code
