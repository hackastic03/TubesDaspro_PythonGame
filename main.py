import parser as parse
import alldata as data
import program as prog
import argparse
import os
import sys

#F013 LOAD FUNCTION

parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('folder', nargs='?', default=None, help='folder where the file is located')

# Parse the arguments
args = parser.parse_args()

# Check if folder is specified
if args.folder is None:
    print("Tidak ada nama folder yang diberikan!")
    sys.exit()

# Check if folder exists
if not os.path.exists(args.folder):
    print(f"Folder \"{args.folder}\" tidak ditemukan!")
    sys.exit()


# Build the file path
def filepath(arg, filename):
    file = os.path.join(arg, filename)
    return file

print("Selamat datang di program \"Manajerial Candi\"")
print("Silahkan masukkan username Anda")

data.user = parse.fromCSV(open(filepath(args.folder, "user.csv"), "r"))
data.bahan = parse.fromCSV(open(filepath(args.folder, "bahan_bangunan.csv"), "r"))
data.candi = parse.fromCSV(open(filepath(args.folder, "candi.csv"), "r"))
data.elemUser = parse.nElem(open(filepath(args.folder, "user.csv"), "r"))
data.elemBangunan = parse.nElem(open(filepath(args.folder, "bahan_bangunan.csv"), "r"))
data.elemCandi = parse.nElem(open(filepath(args.folder, "candi.csv"), "r"))

while True:
    command = input(">>> ")
    if command == "exit":
        break
    else:
        prog.run(command)
