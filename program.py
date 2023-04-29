import alldata as data
import parser as parse
import os
from random import randint
import sys


# def toArray(line):
#     arr = []
#     num_str = ""
#     for char in range(len(line)):
#         if line[char] == "," or line[char] == "]" or line[char] == " ":
#             if num_str:
#                 arr += [int(num_str)]
#                 num_str = ""
#         elif line[char] == "[":
#             continue
#         else:
#             num_str += line[char]
#     if num_str:
#         arr += [int(num_str)]
#     return arr

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


def toArray(line):
    arr = []
    lenarr = 0
    num_str = ""
    for char in range(len(line)):
        if line[char] == "," or line[char] == "]" or line[char] == " ":
            if num_str:
                arr = app(arr, lenarr, int(num_str))[0]
                lenarr += 1
                num_str = ""
        elif line[char] == "[":
            continue
        else:
            num_str += line[char]
    if num_str:
        arr = app(arr, lenarr, int(num_str))[0]
        lenarr += 1
    return arr


def superadmin():
    print(data.user)
    print("role:", data.roleIn)
    print("elemuser:", data.elemUser)
    print(data.bahan)
    print("elembahan:", data.elemBahan)
    print(data.candi)
    print("elemcandi:", data.elemCandi)


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
        jumlahbahan(False)
    elif command == "bangun":
        banguncandi(False)
    elif command == "batchkumpul":
        batchkumpul()
    elif command == "batchbangun":
        batchbangun()
    elif command == "laporanjin":
        laporanjin()
    elif command == "laporancandi":
        laporancandi()
    elif command == "hancurkancandi":
        hancurkancandi()
    elif command == "ayamberkokok":
        ayamberkokok()
    elif command == "superadmin":
        superadmin()
    elif command == "save":
        save()
    elif command == "help":
        help()
    else:
        print("Command tidak ditemukan!")


#F01
def login():
    stateIn = True
    if data.userIn == "":
        while stateIn:
            username = input("Username: ")
            password = input("Password: ")
            checkUser = False

            if not checkUser:
                for i in range(1, data.elemUser[1]):
                    if username == data.user[i][0]:
                        data.userIn = data.user[i][0]
                        data.roleIn = data.user[i][2]
                        checkUser = True
                        break
                if not checkUser:
                    print("Username tidak ditemukan!")
                    data.userIn = ""

            if checkUser:
                for i in range(1, data.elemUser[1]):
                    if password == data.user[i][1] and data.userIn == data.user[i][0]:
                        print(f"""Selamat datang, {data.user[i][0]}!
Masukkan command \"help\" untuk daftar command yang dapat kamu panggil""")
                        stateIn = False
                        data.userIn = data.user[i][0]
                        break
                if stateIn:
                    print("Password salah!")
                    data.userIn = ""

    else:
        print(f"""Login gagal!
Anda telah login dengan username {data.userIn}, silahkan lakukan \"logout\" sebelum melakukan login kembali.""")
        data.userIn = ""


#F02
def logout():
    if data.roleIn == "":
        print("""Logout gagal!
Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout""")
    else:
        data.roleIn = ""
        data.userIn = ""
        print("Logout berhasil!")


#F03
def summonjin():
    if data.roleIn == "bandung_bondowoso":
        if data.elemUser[1] <= 103:
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
                    if daftarUserJin == "-":
                        print("Tidak bisa menggunakan karakter ini sebagai username!")
                    for i in range(1, data.elemUser[1]):
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
                            print("Jin berhasil di-summon.")
                            break

                    else:
                        print("Password panjangnya harus 5-25 karakter!")
        else:
            print("Jumlah jin sudah maksimal!")
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
                        for j in range(data.elemBahan[1]):
                            if deleteJin == data.bahan[j][0]:
                                data.bahan[j][0], data.bahan[j][1], data.bahan[j][2] = "-", "-", "[0, 0, 0]"
                        for j in range(data.elemCandi[1]):
                            if deleteJin == data.candi[j][1]:
                                data.candi[j][1], data.candi[j][2], data.candi[j][3], data.candi[j][4] = "-", 0, 0, 0
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
    else:
        print("Anda tidak bisa menghapus jin!")


#F05 Ubah Jin
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

        while not kondisi:
            print("Tidak ada jin dengan username tersebut")
            break
    else:
        print("Anda tidak bisa mengubah tipe jin!")


# F07 Jin pengumpul
def jumlahbahan(batch):
    if data.roleIn == "Pengumpul":
        pasir = randint(0, 5)
        batu = randint(0, 5)
        air = randint(0, 5)
        for i in range(data.elemBahan[1]):
            if data.userIn == data.bahan[i][0]:
                bahanAda = toArray(data.bahan[i][2])
                data.bahan[i][2] = str([bahanAda[0] + pasir, bahanAda[1] + batu, bahanAda[2] + air])
                break
        else:
            data.bahan = app(data.bahan, data.elemBahan[1], [data.userIn, "-", str([pasir, batu, air])])[0]
            data.elemBahan = (data.elemBahan[0], data.elemBahan[1] + 1)
        if not batch:
            print(f'Jin menemukan {pasir} pasir, {batu} batu, {air} air.')
        else:
            data.totalBahan = [data.totalBahan[0] + pasir, data.totalBahan[1] + batu, data.totalBahan[2] + air]
    else:
        print("Anda tidak punya akses!")


#F06 Jin Pembangun
def banguncandi(batch):
    if data.roleIn == "Pembangun":
        found = False
        material_required = [randint(0, 5), randint(0, 5), randint(0, 5)] #pasir, batu, air
        # print("material:", material_required)
        material_required0 = tuple(material_required)
        jumlahada = [0, 0, 0]
        substract = []
        lenx = 0
        for j in range(1, data.elemBahan[1]):
            for i in range(3):
                tempbahan = toArray(data.bahan[j][2])
                jumlahada[i] += tempbahan[i]
            substract = app(substract, lenx, toArray(data.bahan[j][2]))[0]
            lenx += 1

        enough_materials = True
        for i in range(3):
            if material_required[i] > jumlahada[i]:
                enough_materials = False
                break

        if enough_materials:
            for k in range(3):
                i = 0
                while material_required[k] > 0 and i < data.elemBahan[1]:
                    if substract[i][k] <= material_required[k]:
                        material_required[k] -= substract[i][k]
                        substract[i][k] = 0
                    else:
                        substract[i][k] -= material_required[k]
                        material_required[k] = 0
                    i += 1

            for i in range(1, data.elemBahan[1]):
                data.bahan[i][2] = str(substract[i-1])

            if data.elemBahan[1] <= 101:
                for i in range(data.elemCandi[1]):
                    if data.candi[1] == "-":
                        data.candi[i] = [i, data.userIn, material_required0[0], material_required0[1], material_required0[2]]
                        break
                else:
                    data.candi = app(data.candi, data.elemCandi[1], [data.elemCandi[1], data.userIn, material_required0[0], material_required0[1], material_required0[2]])[0]
                    data.elemCandi = (data.elemCandi[0], data.elemCandi[1] + 1)

            if not batch:
                print("Candi berhasil dibangun!")
                if data.elemCandi[1] < 101:
                    print(f"Sisa candi yang perlu dibangun: {101 - data.elemCandi[1]}.")
                else:
                    print("Sisa candi yang perlu dibangun: 0.")
            else:
                data.totalBangun += 1
                data.totalBahan = [data.totalBahan[0] + material_required0[0], data.totalBahan[1] + material_required0[1], data.totalBahan[2] + material_required0[2]]
        else:
            print("""Bahan bangunan tidak mencukupi.
Candi tidak bisa dibangun!""")
    else:
        print("Anda tidak punya akses!")


#F08
def batchkumpul():
    data.totalBahan = [0, 0, 0]
    data.totalBangun = 0
    if data.userIn == "Bondowoso":
        s = 0
        for i in range(1, data.elemUser[1]):
            if data.user[i][2] == "Pengumpul":
                s += 1
                data.roleIn = data.user[i][2]
                data.userIn = data.user[i][0]
                jumlahbahan(True)
        data.roleIn = "bandung_bondowoso"
        data.userIn = "Bondowoso"
        if s == 0:
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        else:
            print(f"Mengerahkan {s} jin untuk mengumpulkan bahan.")
            print(f"Jin menemukan total {data.totalBahan[0]} pasir, {data.totalBahan[1]} batu, dan {data.totalBahan[2]} air.")
    else:
        print("Anda tidak punya akses!")


#F08
def batchbangun():
    if data.userIn == "Bondowoso":
        data.totalBahan = [0, 0, 0]
        data.totalBangun = 0
        s = 0
        for i in range(1, data.elemUser[1]):
            if data.user[i][2] == "Pembangun":
                s += 1
                data.roleIn = data.user[i][2]
                data.userIn = data.user[i][0]
                banguncandi(True)
        data.roleIn = "bandung_bondowoso"
        data.userIn = "Bondowoso"
        if s == 0:
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        else:
            print(f"Mengerahkan {s} jin untuk membangun candi dengan total bahan {data.totalBahan[0]} pasir, {data.totalBahan[1]} batu, dan {data.totalBahan[2]} air.")
            print(f"Jin berhasil membangun total {data.totalBangun} candi.")
    else:
        print("Anda tidak punya akses")


#F09 Laporan Jin
def sumbahan():
    sbahan = [0, 0, 0]
    for i in range(1, data.elemCandi[1]):
        sbahan = [sbahan[j - 2] + int(data.candi[i][j]) for j in range(2, 5)]
    return sbahan


def sumcandi():
    s = 0
    for i in range(1, data.elemCandi[1]):
        if data.candi[i][1] != "-" and data.candi[i][1] != "":
            s += 1
    return s


def laporanjin():
    if data.roleIn == "bandung_bondowoso":
        ban = 0
        kum = 0
        for i in range(data.elemUser[1]):
            if data.user[i][2] == "Pembangun":
                ban += 1
            elif data.user[i][2] == "Pengumpul":
                kum += 1
        print("Total jin:", ban + kum)
        print("Total jin pengumpul:", kum)
        print("Total jin pembangun:", ban)

        if data.elemCandi[1] > 1:
            #MAX
            jinmaks = data.candi[1][1]
            countmax = 0

            for i in range(1, data.elemCandi[1]):
                count = 0
                if data.candi[i][1] != '-':
                    for j in range(1, data.elemCandi[1]):
                        if data.candi[i][1] == data.candi[j][1] and data.candi[i][1] != '-':
                            count += 1
                    if count > countmax or (count == countmax and data.candi[i][1] <     jinmaks):
                        jinmaks = data.candi[i][1]
                        countmax = count

            #MIN
            check = True
            jinmin = data.candi[1][1]
            countmin = data.elemCandi[1]

            for i in range(1, data.elemCandi[1]):
                count = 0
                if data.candi[i][1] != '-':
                    for j in range(1, data.elemCandi[1]):
                        if data.candi[i][1] == data.candi[j][1] and data.candi[i][1] != '-':
                            count += 1
                    if count < countmin or (count == countmin and data.candi[i][1] > jinmin):
                        jinmin = data.candi[i][1]
                        countmin = count
        else:
            jinmaks = "-"
            jinmin = "-"

        print("Jin Terajin:", jinmaks)
        print("Jin Termalas:", jinmin)

        bah = [0, 0, 0]
        for i in range(1, data.elemBahan[1]):
            bah = [bah[j] + int(toArray(data.bahan[i][2])[j]) for j in range(3)]
        print("Jumlah pasir:", bah[0])
        print("Jumlah batu:", bah[1])
        print("Jumlah air:", bah[2])

    else:
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")


#F10
def biaya(i):
    return int(data.candi[i][2]) * 10000 + int(data.candi[i][3]) * 15000 + int(data.candi[i][4]) * 7500


def laporancandi():
    if data.roleIn == "bandung_bondowoso":
        print("Total candi:", sumcandi())
        print("Total pasir yang digunakan:", sumbahan()[0])
        print("Total batu yang digunakan:", sumbahan()[1])
        print("Total air yang digunakan:", sumbahan()[2])
        if data.elemUser[1] > 1:
            s = biaya(1)
            ind = 1
            for i in range(1, data.elemCandi[1]):
                if biaya(i) > s:
                    print(f"biaya({i}) = {biaya(i)}")
                    s = biaya(i)
                    ind = i
            print("ID Candi Termahal:", ind, f"Rp {s}")
            s = biaya(1)
            ind = 1
            for i in range(1, data.elemCandi[1]):
                if biaya(i) < s:
                    print(f"biaya({i}) = {biaya(i)}")
                    s = biaya(i)
                    ind = i
            print("ID Candi Termurah:", ind, f"Rp {s}")
        else:
            print('ID Candi Termahal: -')
            print('ID Candi Termurah: -')
    else:
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")


#F11
def hancurkancandi():
    if data.roleIn == "roro_jonggrang":
        index = int(input("Masukkan id candi: "))
        for i in range(data.elemCandi[1]):
            if index == data.candi[i][0]:
                loop = True
                while loop:
                    val = input(f"Apakah anda yakin ingin menghancurkan candi ID: {index} (Y/N)? ")
                    if val == "Y" or val == "y":
                        data.candi[i] = [data.candi[i][0], "-", 0, 0, 0]
                        print("Candi telah berhasil dihancurkan.")
                        break
                    elif val == "N" or val == "n":
                        print("Candi tidak jadi dihancurkan.")
                        break
                    else:
                        loop = True
                break
        else:
            print("Tidak ada candi dengan ID tersebut.")
    else:
        print("Anda tidak bisa menghancurkan candi!")


# F12 Ayam berkokok
def ayamberkokok():
    if data.roleIn == "roro_jonggrang":
        print('Kukuruyuk.. Kukuruyuk..')
        if sumcandi() >= 100:
            print(f'Jumlah Candi: {sumcandi()}')
            print('Yah, Bandung Bondowoso memenangkan permainan!')
        else:
            print(f'Jumlah Candi: {sumcandi()}')
            print('''Selamat, Roro Jonggrang memenangkan permainan!.
    
Bandung Bondowoso angry noise.
Roro Jonggrang dikutuk menjadi candi.''')
        sys.exit()
    else:
        print("Kamu gapunya akses!")


#F14
def save():
    savefolder = input("Masukkan nama folder: ")
    if os.path.exists(savefolder):
        print('Saving...')

    else:
        os.makedirs(savefolder)
        print(f"Membuat folder {savefolder}...")

    parse.fromMatrix(data.user, data.elemUser, os.path.join(savefolder, "user.csv"))
    parse.fromMatrix(data.bahan, data.elemBahan, os.path.join(savefolder, "bahan_bangunan.csv"))
    parse.fromMatrix(data.candi, data.elemCandi, os.path.join(savefolder, "candi.csv"))
    print(f"Berhasil menyimpan data di folder {savefolder}!")


# F15 HELP
def help():
    if data.roleIn == 'bandung_bondowoso':
        print('=========== HELP ===========')
        print(''' 1. logout
Untuk keluar dari akun yang digunakan sekarang''')
        print(''' 2. summonjin
Untuk memanggil jin''')
        print(''' 3. hapusjin
Untuk menghapus jin dan candi yang telah dibangun oleh jin yang di hapus''')
        print(''' 4. ubahjin
Untuk mengubah tipe jin pengumpul menjadi jin pembangun atau sebaliknya''')
        print(''' 5. batchkumpul / batchbangun
Untuk mengerahkan semua jin sesuai tipenya untuk melakukan tugasnya masing-masing''')
        print(''' 6. laporanjin
Untuk mengambil laporan jin untuk mengetahui kinerja dari para jin''')
        print(''' 7. laporancandi
Untuk mengambil laporan candi untuk mengetahui progress pembangunan candi ''')
        
    elif data.roleIn == 'roro_jonggrang':
        print('=========== HELP ===========')
        print(''' 1. logout
Untuk keluar dari akun yang digunakan sekarang''')
        print(''' 2. hancurkancandi
Untuk menghancurkan candi agar menggagalkan rencana Bandung Bondowoso dan data candi terhapus''')
        print(''' 3. ayamberkokok
Untuk menyelesaikan permainan dengan memalsukan pagi hari''')

    elif data.roleIn == 'Pembangun':
        print('=========== HELP ===========')
        print(''' 1. logout
Untuk keluar dari akun yang digunakan sekarang''')
        print(''' 2. bangun
Untuk membangun candi dengan jumlah bahan yang tersedia jika jumlahnya mencukupi''')

    elif data.roleIn == 'Pengumpul':
        print('=========== HELP ===========')
        print(''' 1. logout
Untuk keluar dari akun yang digunakan sekarang''')
        print(''' 2. kumpul
Untuk mengumpulkan bahan untuk membangun candi berupa pasir, batu, dan air''')

    elif data.roleIn == '':
        print('=========== HELP ===========')
        print('''1. login
Untuk masuk menggunakan akun''')
        print('''2. exit
Untuk keluar dari program dan kembali ke terminal''')


