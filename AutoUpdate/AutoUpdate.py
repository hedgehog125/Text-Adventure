# Released under cc licence: https://creativecommons.org/
# Made by @hedgehog125 on github.com and scratch.mit.edu
import urllib.request, os, shutil, ast
from time import sleep
database = "unknown"
FileList = ""
new = []
Updates = ""
FileList = ""
path = ""
def Get_Web_Info(Address, decode=True):
    url = Address
    response = urllib.request.urlopen(url)
    data = response.read()      # a `bytes` object
    if not decode:
        return data
    text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    return (text)

def Open_File(File,Write,Text):
    if Write:
        f = open(path + File,'w')
        f.write(Text)
    else:
        f = open(path + File)
        text = f.readlines()
        f.close()
        return (text)
    f.close()


def GetFileList():
    global FileList
    global updates
    print("Retrieving file list...")
    FileList = Get_Web_Info(database + "Files.txt")
    FileList = ast.literal_eval(FileList)
    
def CheckForUpdates():
    global Updates
    global Latest
    global Downloaded
    global new
    print("Checking for updates...")
    Updates = Get_Web_Info(database + "Versions.txt")
    Updates = Updates.split(",")
    Latest = Updates[len(Updates)-1]
    Downloaded = Open_File("Versions.txt",False,"")[0]
    if len(Downloaded) > 0:
        Downloaded = ast.literal_eval(Downloaded)
    else:
        Downloaded = []
    new = []
    if Downloaded != Updates:
        for i in range(len(Updates) - len(Downloaded)):
            new.append(Updates[i + len(Downloaded)])
    if len(new) > 0:
        if len(new) == 1:
            print("1 update found!")
        else:
            print(str(len(new)) + " updates found!")
    else:
        print("No updates found.")

def GetFiles():
    print("Downloading files...")
    for v in new:
        ver = str(v)
        if ver in FileList:
            for i in range(len(FileList[ver])):
                if FileList[ver][i][0]:
                    if FileList[ver][i][3]:
                        g = urllib.request.urlopen(FileList[ver][i][2])
                        with open("Assets/" + FileList[ver][i][1], 'b+w') as f:
                            f.write(g.read())
                    else:
                        Open_File("Assets/" + FileList[ver][i][1],True,FileList[ver][i][2])                        
                else:
                    try:
                        os.makedirs("Assets/" + FileList[ver][i][1])
                    except:
                        print("Tampered files detected.")
                        print("Restoring...")
                        print("")
                        shutil.rmtree("Assets")
                        sleep(0.5)
                        os.makedirs("Assets")
                        return True

    if len(new) == 1:
        print("Update installed!")
    else:
        print("Updates installed!")
    print("Updating installed file...")
    Open_File("Versions.txt",True,str(Updates))
    print("Done!")
    return False

def init():
    if (database == "unknown"):
        return
    CheckForUpdates()
    sleep(0.5)
    if len(new) > 0:
        GetFileList()
        if GetFiles():
            init()
