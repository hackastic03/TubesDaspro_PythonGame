import parser as parse
import alldata as data
import program as prog



data.user = parse.fromCSV(open("user.csv", "r"))
data.bahan = parse.fromCSV(open("bahan_bangunan.csv", "r"))
data.candi = parse.fromCSV(open("candi.csv", "r"))
data.elemUser = parse.nElem(open("user.csv", "r")); print(data.elemUser)
data.elemCandi = parse.nElem(open("candi.csv", "r"))
data.elemBangunan = parse.nElem(open("bahan_bangunan.csv", "r"))

print(data.user)
print(data.bahan)
while True:
    command = input(">>> ")
    if command == "exit":
        break
    else:
        prog.run(command)


