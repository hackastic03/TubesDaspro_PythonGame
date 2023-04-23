import alldata as data
import parser as parse
import os
from random import randint


def isNone(file):
    for i in file:
        if i[0] == None and i[1] == None:
            return True


def toTuple(line):
    tuple_values = ()
    num_str = ""
    for char in range(len(line)):
        if line[char] == "," or line[char] == ")" or line[char] == " ":
            if num_str:
                tuple_values += (int(num_str),)
                num_str = ""
        elif line[char] == "(":
            continue
        else:
            num_str += line[char]
    if num_str:
        tuple_values += (int(num_str),)
    return tuple_values


def app(arr, length, x):
    # line = 0
    # for i in arr:
    #     line += 1
    arr2 = [0 for i in range(length+1)]
    for i in range(length):
        arr2[i] = arr[i]
    arr2[length] = x
    length += 1
    return arr2, length

def superadmin():
    print(data.user)
    print("role:", data.roleIn)
    print("elemuser:", data.elemUser)
    print(data.bahan)
    print("elembahan:", data.elemBahan)

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
    elif command == "ubahjin":
        ubahjin()
    elif command == "kumpul":
        jumlahbahan()
    elif command == "superadmin":
        superadmin()
    elif command == "save":
        save()
    elif command == "help":
        help()


#F01
def login():
    stateIn = True

    if data.roleIn == "":
        while stateIn:
            username = input("Username: ")
            password = input("Password: ")
            checkUser = False

            if not checkUser:
                for i in range(1, data.elemUser[1]):
                    if username == data.user[i][0]:
                        data.roleIn = data.user[i][2]
                        checkUser = True
                        break
                if not checkUser:
                    print("Username tidak ditemukan!")

            if checkUser:
                for i in range(1, data.elemUser[1]):
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


#F02
def logout():
    if data.roleIn == "":
        print("""Logout gagal!
Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout""")
    else:
        data.roleIn = ""
        print("Logout berhasil!")


#F03
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
                for i in range(1,data.elemUser[1]):
                    if daftarUserJin == data.user[i][0]:
                        print(f"Username \"{daftarUserJin}\" sudah diambil!")
                        validasiUsernameJin = True
                        break
                    else:
                        validasiUsernameJin = False

            while not validasiUsernameJin:
                daftarPassJin = input("Masukkan password jin: ")
                if len(daftarPassJin) >= 5 and len(daftarPassJin) <= 25:
                    for j in range(1, data.elemUser[1]):
                        if data.user[j][0] == "-" and data.user[j][1] == "-" and data.user[j][2] == "-":
                            data.user[j][0], data.user[j][1], data.user[j][2] = daftarUserJin, daftarPassJin, rolejin
                            validasiUsernameJin = True
                            print("Jin berhasil di-summon.")
                            break
                    else:
                        data.user = app(data.user, data.elemUser[1], [daftarUserJin, daftarPassJin, rolejin])[0]
                        data.elemUser = (data.elemUser[0], data.elemUser[1]+1)
                        validasiUsernameJin = True
                        break

                else:
                    print("Password panjangnya harus 5-25 karakter!")

    else:
        print("Anda tidak punya akses!")


#F04
def hapusjin():
    if data.roleIn == "bandung_bondowoso":
        validasiUsernameJin = True
        while validasiUsernameJin:
            deleteJin = input("Masukkan username jin : ")
            for i in range(1, data.elemUser[1]):
                if deleteJin == data.user[i][0] and deleteJin != "Bondowoso" and deleteJin != "Roro":
                    validasiUsernameJin = False
                    checkDeleteJin = input(f"Apakah anda yakin ingin menghapus jin dengan username {deleteJin} (Y/N)? ")
                    if checkDeleteJin == "Y" or checkDeleteJin == "y":
                        print("Jin telah berhasil dihapus dari alam gaib.")
                        data.user[i][0], data.user[i][1], data.user[i][2] = "-", "-", "-"
                        break
                    elif checkDeleteJin == "N" or checkDeleteJin == "n":
                        print("Jin tidak jadi dihapus")
                        break
                elif deleteJin == "Bondowoso" or deleteJin == "Roro":
                    print("Anda tidak bisa menghapus user!")
                    break
            else:
                print("Tidak ada jin dengan username tersebut.")
                break


#F05
def ubahjin():
    if data.roleIn == "bandung_bondowoso":
        kondisi = True
        daftarUserJin = input("Masukkan username jin: ")
        for i in range(1, data.elemUser[1]):
            if daftarUserJin == data.user[i][0]:
                if data.user[i][2] == "Pembangun":
                    while True:
                        checkYesNo = input(
                            "Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? ")
                        if checkYesNo == "Y" or checkYesNo == "y":
                            print("Jin berhasil diubah")
                            data.user[i][2] = "Pengumpul"
                            break
                        elif checkYesNo == "N" or checkYesNo == "n":
                            print("Jin tidak jadi diubah")
                            break
                        else:
                            print("Silahkan pilih Y atau N")
                    break
                if data.user[i][2] == "Pengumpul":
                    while True:
                        checkYesNo = input(
                            "Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)?")
                        if checkYesNo == "Y" or checkYesNo == "y":
                            print("Jin telah berhasil diubah")
                            data.user[i][2] = "Pembangun"
                            break
                        elif checkYesNo == "N" or checkYesNo == "n":
                            print("Jin tidak jadi diubah")
                            break
                        else:
                            print("Silahkan pilih Y atau N")
                        break
        for j in range(1, data.elemUser[1]):
            if daftarUserJin == data.user[j][0]:
                kondisi = True
                break
            else:
                kondisi = False

        while kondisi == False:
            print("Tidak ada jin dengan username tersebut")
            break

    else:
        print("Anda tidak punya akses!")


# F07 Jin pengumpul


def jumlahbahan():
    if data.userIn != "Bondowoso" or data.userIn != "Roro":
        pasir = randint(0,5)
        batu = randint(0,5)
        air = randint(0,5)
        for i in range(data.elemBahan[1]):
            if data.userIn == data.bahan[i][0]:
                bahanAda = toTuple(data.bahan[i][2])
                data.bahan[i][2] = (bahanAda[0] + pasir, bahanAda[1] + batu, bahanAda[2] + air)
                break
        else:
            data.bahan = app(data.bahan, data.elemBahan[1], [data.userIn, "-", [pasir, batu, air]])[0]
            data.elemBahan = (data.elemBahan[0], data.elemBahan[1] + 1)
        print(f'Jin menemukan {pasir} pasir, {batu} batu, {air} air.')

#


# # F12 Ayam berkokok
# def ayamberkokok() :
#     print ('Kukuruyuk.. Kukuruyuk..')
#     if jumlahcandi == 100 :
#         print (f'Jumlah Candi: {jumlahcandi}')
#         print ('Yah, Bandung Bondowoso memenangkan permainan!')
#     else :
#         print (f'Jumlah Candi : {jumlahcandi}')
#         print ('''Selamat, Roro Jonggrang memenangkan permainan!.
#
# Bandung Bondowoso angry noise.
# Roro Jonggrang dikutuk menjadi candi.''')
# (ayamberkokok())


def save():
    savefolder = input("Masukkan nama folder: ")
    if os.path.exists(savefolder):
        print('Saving...')
        parse.fromMatrix(data.user, data.elemUser, os.path.join(savefolder, "user.csv"))
        parse.fromMatrix(data.bahan, data.elemBahan, os.path.join(savefolder, "bahan_bangunan.csv"))
        parse.fromMatrix(data.candi, data.elemCandi, os.path.join(savefolder, "candi.csv"))
        print(f"Berhasil menyimpan data di folder {savefolder}!")
    else:
        os.makedirs(savefolder)
        print(f"Membuat folder {savefolder}...")
        parse.fromMatrix(data.user, data.elemUser, os.path.join(savefolder, "user.csv"))
        parse.fromMatrix(data.bahan, data.elemBahan, os.path.join(savefolder, "bahan_bangunan.csv"))
        parse.fromMatrix(data.candi, data.elemCandi, os.path.join(savefolder, "candi.csv"))
        print(f"Berhasil menyimpan data di folder {savefolder}!")



# F15 HELP
def help() :
    if data.roleIn == 'bandung_bondowoso' :
        print ('=========== HELP ===========')
        print (''' 1. logout
    Untuk keluar dari akun yang digunakan sekarang''')
        print (''' 2. summonjin
    Untuk memanggil jin''')
        print (''' 3. Hilangkan Jin
    Untuk menghapus jin dan candi yang telah dibangun oleh jin yang di hapus''')
        print (''' 4. Ubah Tipe Jin
    Untuk mengubah tipe jin pengumpul menjadi jin pembangun atau sebaliknya''')
        print (''' 5. Batch Kumpul/Bangun
    Untuk mengerahkan semua jin sesuai tipenya untuk melakukan tugasnya masing-masing''')
        print (''' 6. Ambil Laporan Jin
    Untuk mengambil laporan jin untuk mengetahui kinerja dari para jin''')
        print (''' 7. Ambil Laporan Candi
    Untuk mengambil laporan candi untuk mengetahui progress pembangunan candi ''')
        
    elif data.roleIn == 'roro_jonggrang' :
        print ('=========== HELP ===========')
        print (''' 1. logout
    Untuk keluar dari akun yang digunakan sekarang''')
        print (''' 2. Hancurkan Candi
    Untuk menghancurkan candi agar menggagalkan rencana Bandung Bondowoso dan data candi terhapus''')
        print (''' 3. Ayam Berkokok
    Untuk menyelesaikan permainan dengan memalsukan pagi hari''')

    elif data.roleIn == 'Pembangun':
        print ('=========== HELP ===========')
        print (''' 1. logout
    Untuk keluar dari akun yang digunakan sekarang''')
        print (''' 2. Jin Pembangun
    Untuk membangun candi dengan jumlah bahan yang tersedia jika jumlahnya mencukupi''')
    elif data.roleIn == 'Pengumpul':
        print ('=========== HELP ===========')
        print (''' 1. logout
    Untuk keluar dari akun yang digunakan sekarang''')
        print (''' 2. Jin Pengumpul
    Untuk mengumpulkan bahan untuk membangun candi berupa pasir,batu dan air''')
    elif data.roleIn == ' ' :
        print ('=========== HELP ===========')
        print ('''1. login
   Untuk masuk menggunakan akun''')
        print ('''2. exit
   Untuk keluar dari program dan kembali ke terminal''')




#F16 EXIT
# def exit () :
#     pilihan = ("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? ")
#     if pilihan == "n" or pilihan == "N" :
#         run = False
#     elif pilihan == "Y" or pilihan == "y" :
#         save()
#         run = False
#     else :
#         while pilihan != "n" or pilihan != "N" or pilihan != "y" or pilihan != "Y" :
#             input ("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? ")




