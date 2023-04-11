import parser as parse
import alldata as data
import program as prog

data.user = parse.fromCSV(open("user.csv", "r"))
data.bahan = parse.fromCSV(open("bahan_bangunan.csv", "r"))
data.candi = parse.fromCSV(open("candi.csv", "r"))

while True:
    command = input(">>> ")
    if command == "exit":
        break
    else:
        prog.run(command)


