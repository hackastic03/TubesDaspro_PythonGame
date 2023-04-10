import alldata as data
# import parser as parse
# users = parse.fromCSV(open("user.csv", "r"))


def run(command):
    if command == "login":
        login()
    elif command == "logout":
        logout()
    # elif command == "summonjin":
    #     summonjin()


def login():
    stateIn = False; stateUser = False; statePass = False
    userIn = ""
    roleIn = ""
    username = input("Username: ")
    password = input("Password: ")

    for i in range(len(data.user)):
        if (username == data.user[i][0]) and (password == data.user[i][1]):
            stateIn = True; statePass = True; stateUser = True
            userIn = data.user[i][0]
            roleIn = data.user[i][2]
            print(f"""Selamat datang, {userIn}!
Masukkan command \"help\" untuk daftar command yang dapat kamu panggil""")
            break
        else:
            if username == data.user[i][0]:
                stateUser = True
            elif password == data.user[i][1]:
                statePass = True

    if not stateUser:
        print("Username tidak terdaftar!")
    if not statePass:
        print("Password salah!")
    return userIn, stateIn, roleIn


def logout():
    state = 0
    userIn = ""
    roleIn = ""
    return userIn, state, roleIn

# def summonjin():
#     if roleIn == "bandung_bondowoso":
#         rolejin = ""
#         print(f"""Jenis jin yang dapat dipanggil:
#     (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
#     (2) Pembangun - Bertugas membandung candi""")
#         jenisJin = input("Masukkan nomor jenis jin yang dipanggil: ")
#         if jenisJin == 1:
#             print("Memilih jin \"Pengumpul\".")
#             rolejin = "Pengumpul"
#         elif jenisJin == 2:
#             print("Memilih jin \"Pembangun\".")
#             rolejin = "Pembangun"
#         else:
#             print(f"Tidak ada jenis jin bernomor {jenisJin}")
#
#     if rolejin == "":

