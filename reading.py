def readFile(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    print lines
