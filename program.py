import alldata as data
import parser as parse
import os

def isNone(file):
    for i in file:
        if i[0] == None and i[1] == None:
            return True


def app(file, x):
    line = 0
    for i in file:
        line += 1
    arr2 = [0 for i in range(line + 1)]
    for i in range(line):
        arr2[i] = file[i]
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
    elif command == "save":
        save()


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
# F07 Jin pengumpul
from random import randint
def jumlahbahan () :
    pasir = randint(0,5) 
    batu = randint(0,5)
    air = randint(0,5)
    jumlahterkumpul = (f'Jin menemukan {pasir} pasir. {batu} batu, {air}')
    return jumlahterkumpul
print (jumlahbahan())

# F12 Ayam berkokok
def ayamberkokok() :
    print ('Kukuruyuk.. Kukuruyuk..')
    if jumlahcandi == 100 :
        print (f'Jumlah Candi: {jumlahcandi}')
        print ('Yah, Bandung Bondowoso memenangkan permainan!')
    else :
        print (f'Jumlah Candi : {jumlahcandi}')
        print ('''Selamat, Roro Jonggrang memenangkan permainan!.

Bandung Bondowoso angry noise.
Roro Jonggrang dikutuk menjadi candi.''')       
(ayamberkokok())

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
    if  data.roleIn == 'bandung_bondowoso' :
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
        print
    elif data.roleIn == 'jin_pembangun' :
        print ('=========== HELP ===========')
        print (''' 1. logout
    Untuk keluar dari akun yang digunakan sekarang''')
        print (''' 2. Jin Pembangun
    Untuk membangun candi dengan jumlah bahan yang tersedia jika jumlahnya mencukupi''')
    elif data.roleIn == 'jin_pengumpul' :
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
(help())

#F16 EXIT
def exit () :
    pilihan = ("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? ")
    if pilihan == "n" or pilihan == "N" :
        run = False
    elif pilihan == "Y" or pilihan == "y" :
        save()
        run = False
    else :
        while pilihan != "n" or pilihan != "N" or pilihan != "y" or pilihan != "Y" :
            input ("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? ")




