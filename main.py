import parser as parse
import alldata as data
import program as prog

data.users = parse.fromCSV(open("user.csv", "r"))
bahan = parse.fromCSV(open("bahan_bangunan.csv", "r"))
candi = parse.fromCSV(open("candi.csv", "r"))


print(data.users)
while True:
    command = input(">>> ")
    if command == "exit":
        break
    else:
        prog.run(command)


