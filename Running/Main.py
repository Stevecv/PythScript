from OpenFile import openFile

def runFile(name):
    #Getting the code
    code = openFile(name)

    #Remove spaces and other tabs
    noWhiteSpace = code.replace(" ", "").replace("  ", "")

    