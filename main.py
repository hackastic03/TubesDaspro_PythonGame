import parser as parse
import alldata as data
import program as prog
import argparse
import os
import sys

#F013 LOAD FUNCTION

parser = argparse.ArgumentParser(description='Buka folder.')
parser.add_argument('folder', nargs='?', default=None, help='Spesifikasikan folder csv berlokasi')
args = parser.parse_args()

if args.folder is None:
    print("Tidak ada nama folder yang diberikan!")
    sys.exit()

if not os.path.exists(args.folder):
    print(f"Folder \"{args.folder}\" tidak ditemukan!")
    sys.exit()

def filepath(arg, filename):
    file = os.path.join(arg, filename)
    return file

#F014 SAVE FUNCTION



print("Selamat datang di program \"Manajerial Candi\"")
print("Silahkan masukkan username Anda")

data.user = parse.fromCSV(open(filepath(args.folder, "user.csv"), "r"))
data.bahan = parse.fromCSV(open(filepath(args.folder, "bahan_bangunan.csv"), "r"))
data.candi = parse.fromCSV(open(filepath(args.folder, "candi.csv"), "r"))
data.elemUser = parse.nElem(open(filepath(args.folder, "user.csv"), "r"))
data.elemBahan = parse.nElem(open(filepath(args.folder, "bahan_bangunan.csv"), "r"))
data.elemCandi = parse.nElem(open(filepath(args.folder, "candi.csv"), "r"))


while True:
    command = input(">>> ")
    if command == "exit":
        break
    # elif command == "save":
    #     save()
    else:
        prog.run(command)