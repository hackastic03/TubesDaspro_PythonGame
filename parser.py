def fromCSV(file):
    baris = []
    # test = False
    for line in file:
        column = []
        text = ""
        for char in line:
            if char == ";":
                column.append(text)
                text = ""
            elif char == "\n":
                break
            else:
                text += char
        column.append(text)
        text = ""
        baris.append(column)
    return baris