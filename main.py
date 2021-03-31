import re
import os

path = 'C:/Users\estef\Documents\prueba'

def getRE(word,dir):
    rule = re.compile(word)
    files = getFilesNames(dir)
    finalPaths = []
    for file in files:
        names = rule.findall(file)
        for name in names:
                newPath = searchFile(name,dir)
                if newPath:
                    for path in newPath:
                        if path not in finalPaths:
                            finalPaths.append(path)
    return finalPaths

def searchFile(word,path):
    files = []
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)) and word in i:
            newPath = path + "/" + i
            files.append(newPath)
    return files if len(files) != 0 else False

def getFilesNames(path):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        f.extend(filenames)
        break
    return f

print(getRE('ab*',path))
