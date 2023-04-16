import alldata as data


def app(arr, x):
    line = 0
    for i in arr:
        line += 1
    arr2 = [0 for i in range(line + 1)]
    for i in range(line):
        arr2[i] = arr[i]
    arr2[line] = x
    line += 1
    return arr2

def superadmin():
    print(data.user)
    print("role:", data.roleIn)
    print("elemuser:", data.elemUser)


# def noneFind(arr):
#     for i in arr:

def findUsername(inp):
    for i in range(data.elemUser[1]):
        if inp == data.user[i][0]:
            username = data.user[i][0]
            return username


def run(command):
    if command == "login":
        login()
    elif command == "logout":
        logout()
    elif command == "summonjin":
        summonjin()
    elif command == "hapusjin":
        hapusjin()
    elif command == "superadmin":
        superadmin()


def login():
    stateIn = True

    if data.roleIn == "":
        while stateIn:
            username = input("Username: ")
            password = input("Password: ")
            checkUser = False

            if not checkUser:
                for i in range(data.elemUser[1]):
                    if username == data.user[i][0]:
                        data.roleIn = data.user[i][2]
                        checkUser = True
                        break
                if not checkUser:
                    print("Username tidak ditemukan!")

            if checkUser:
                for i in range(data.elemUser[1]):
                    if password == data.user[i][1] and data.roleIn == data.user[i][2]:
                        print(f"""Selamat datang, {data.user[i][0]}!
Masukkan command \"help\" untuk daftar command yang dapat kamu panggil""")
                        stateIn = False
                        data.userIn = data.user[i][0]
                        break
                if stateIn:
                    print("Password salah!")

    else:
        print(f"""Login gagal!
Anda telah login dengan username {data.userIn}, silahkan lakukan \"logout\" sebelum melakukan login kembali.""")


def logout():
    if data.roleIn == "":
        print("""Logout gagal!
Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout""")
    else:
        data.roleIn = ""
        print("Logout berhasil!")


def summonjin():
    if data.roleIn == "bandung_bondowoso":
        rolejin = ""
        print(f"""Jenis jin yang dapat dipanggil:
(1) Pengumpul - Bertugas mengumpulkan bahan bangunan
(2) Pembangun - Bertugas membandung candi""")
        while True:
            jenisJin = int(input("Masukkan nomor jenis jin yang dipanggil: "))
            if jenisJin == 1:
                print("Memilih jin \"Pengumpul\".")
                rolejin = "Pengumpul"
                break
            elif jenisJin == 2:
                print("Memilih jin \"Pembangun\".")
                rolejin = "Pembangun"
                break
            else:
                print(f"Tidak ada jenis jin bernomor \"{jenisJin}\"!")

        if rolejin == "Pembangun" or rolejin == "Pengumpul":
            validasiUsernameJin = True
            while validasiUsernameJin:
                daftarUserJin = input("Masukkan username jin: ")
                for i in range(len(data.user)):
                    if daftarUserJin == data.user[i][0]:
                        print(f"Username \"{daftarUserJin}\" sudah diambil!")
                        validasiUsernameJin = True
                        break
                    else:
                        validasiUsernameJin = False

            while not validasiUsernameJin:
                daftarPassJin = input("Masukkan password jin: ")
                if len(daftarPassJin) >= 5 and len(daftarPassJin) <= 25:
                    data.user = app(data.user, [daftarUserJin, daftarPassJin, rolejin])
                    data.elemUser = (data.elemUser[0], data.elemUser[1] + 1)
                    print(data.elemUser[1])
                    validasiUsernameJin = True
                    break
                else:
                    print("Password panjangnya harus 5-25 karakter!")

    else:
        print("Anda tidak punya akses!")



def hapusjin():
    if data.roleIn == "bandung_bondowoso":
        validasiUsernameJin = True
        while validasiUsernameJin:
            deleteJin = input("Masukkan username jin : ")
            for i in range(data.elemUser[1]):
                if deleteJin == data.user[i][0] and deleteJin != "Bondowoso" and deleteJin != "Roro":
                    validasiUsernameJin = False
                    checkDeleteJin = input(f"Apakah anda yakin ingin menghapus jin dengan username {deleteJin} (Y/N)? ")
                    if checkDeleteJin == "Y":
                        print("Jin telah berhasil dihapus dari alam gaib.")
                        data.user[i][0], data.user[i][1], data.user[i][2] = None, None, None
                        break
                    elif checkDeleteJin == "N":
                        print("Jin tidak jadi dihapus")
                        break
                elif deleteJin == "Bondowoso" or deleteJin == "Roro":
                    print("Anda tidak bisa menghapus user!")
                    break
            else:
                print("Tidak ada jin dengan username tersebut.")
                break
