import os

start_click = 0

def isFile(filename) :
    return int(os.path.isfile(filename.decode()))


def readFile(filename) :
    with open(filename.decode(), "r") as f:
        file = f.read()
    return file.encode()


def writeFile(filename, content):
    with open(filename.decode(), "w") as f:
        f.write(content.decode())
    
