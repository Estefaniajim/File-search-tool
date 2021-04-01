import os

path = 'C:/Users\estef\Documents\prueba'


def getRE(rule, dir):
    files = getFilesNames(dir)
    finalPaths = []
    for file in files:
        if validateRE(rule, file):
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
            newPath = path + "/" + i
            files.append(newPath)
    return files if len(files) != 0 else False

def getFilesNames(path):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        f.extend(filenames)
        break
    return f

def validateRE(rule, word):
    patron = ""
    stackLetters = []
    currentState = True
    reState = True
    re = False
    for i, char in enumerate(rule):
        if char == "+":
            re = True
            if not (validateRE(rule[i + 2::], word)):
                reState = False
        elif char == "(":
            for letter in stackLetters:
                patron += letter
            stackLetters = []
        elif char == "*":
            if not isOnTheWord(stackLetters, word):
                currentState = False
            else:
                stackLetters = []
        else:
            if char != ")":
                stackLetters.append(char)
    if stackLetters:
        for letter in stackLetters:
            patron += letter

    if patron != "" and len(patron) < len(word):
        for i in range(len(patron)):
            if word[i] != patron[i]:
                currentState = False

    if currentState:
        return True
    else:
        if reState and re:
            return True
        else:
            return False

def isOnTheWord(pattern, word):
    newPattern = ""
    for letter in pattern:
        newPattern += letter
    if newPattern in word:
        return True
    else:
        return False


print(getRE("ab*", path))
