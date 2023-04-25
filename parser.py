def nElem(file):
    nkolom = 1
    for line in file:
        for char in range(len(line)):
            if line[char] == ";":
                nkolom += 1
        break

    nbaris = 1
    for line in file:
        nbaris += 1
    return nkolom, nbaris

def app(file, x):
    line = 0
    for i in file:
        line += 1
    newfile = [0 for i in range(line+1)]
    for i in range(line):
        newfile[i] = file[i]
    newfile[line] = x
    line += 1
    return newfile

def fromCSV(file):
    baris = []
    for line in file:
        column = []
        text = ""
        for char in range(len(line)):
            if line[char] == ";":
                column = app(column, text)
                text = ""
            elif line[char] == "\n":
                break
            else:
                text += line[char]
        column = app(column, text)
        baris = app(baris, column)
    file.close()
    return baris

def toTuple(line):
    tuple = ()
    element = ""
    for char in range(len(line)):
        if char == ",":
            tuple = app(tuple, element)
            element = ""
        elif char == ")":
            break
        elif char == "(":
            continue
        else:
            element += str(line(char))
        tuple = app(tuple, element)
    return tuple

def fromMatrix(matrix, length, file):
    with open(file, "w") as filename:
        for i in range(length[1]):
            for j in range(length[0]):
                filename.write(str(matrix[i][j]))
                if j < len(matrix[i])-1:
                    filename.write(";")
            filename.write("\n")

    filename.close()


# def fromCSV(file):
#     baris = []
#     # test = False
#     for line in file:
#         column = []
#         text = ""
#         for char in line:
#             if char == ";":
#                 column.append(text)
#                 text = ""
#             elif char == "\n":
#                 break
#             else:
#                 text += char
#         column.append(text)
#         baris.append(column)
#     return baris



