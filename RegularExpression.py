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

def isTextFile(fileName):
    lenght = len(fileName)
    if fileName[lenght-1] == "t":
        if fileName[lenght-2] == "x":
            if fileName[lenght-3] == "t":
                if fileName[lenght-4] == ".":
                    return True
    return False