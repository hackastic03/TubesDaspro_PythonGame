def nElem(file):
    nkolom = 1
    for line in file:
        for char in line:
            if char == ";":
                nkolom += 1
        break

    nbaris = 0
    for line in file:
        nbaris += 1
    return nkolom, nbaris

def app(arr, x):
    line = 0
    for i in arr:
        line += 1
    arr2 = [0 for i in range(line+1)]
    for i in range(line):
        arr2[i] = arr[i]
    arr2[line] = x
    line += 1
    return arr2

def fromCSV(file):
    baris = []
    for line in file:
        column = []
        text = ""
        for char in line:
            if char == ";":
                column = app(column, text)
                text = ""
            elif char == "\n":
                break
            else:
                text += char
        column = app(column, text)
        baris = app(baris, column)
    return baris

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



