def openFile(path):
    #Opening the file and setting it up for reading
    file = open(path, "r")

    #Reading the file
    return file.read()