contents = {}

def filereader(filename):
    global contents
    with open(filename) as bunchoflines:
        for lines in bunchoflines:
            newline = bunchoflines.readline()
            contents = {'Key': newline[0:5]}