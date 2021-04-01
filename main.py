import os
import RegularExpression as re

path = 'C:/Users\estef\Documents\prueba'

def getRE(rule, dir):
    files = getFilesNames(dir)
    finalPaths = []
    if "+" in rule:
        words = getWordsInFiles(dir)
        for word in words:
            files.append(word)
    for file in files:
        if re.validateRE(rule, file):
            newPath = searchFile(file, dir)
            if newPath:
                for path in newPath:
                    if path not in finalPaths:
                        finalPaths.append(path)
    return finalPaths

def searchFile(word, path):
    files = []
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)) and word in i:
            newPath = path + str("/" + i)
            files.append(newPath)
    return files if len(files) != 0 else False

def getFilesNames(path):
    filesNames = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        filesNames.extend(filenames)
        break
    return filesNames

def getWordsInFiles(path):
    words = []
    files = os.listdir(path)
    for file in files:
        if re.isTextFile(file):
            with open(os.path.join(path, file), 'r') as f:
                content = f.read().split(" ")
                for i in content:
                    if i != "":
                        words.append(i)
    return words

#print(getRE("ab*", path))
#print(getWordsInFiles(path))
#print(re.isTextFile("hola.txt"))
