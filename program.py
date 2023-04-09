import alldata as data
import parser as parse
users = parse.fromCSV(open("user.csv", "r"))


def run(command):
    if command == "login":
        state = 0
        userin = ""
        username = input("Username: ")
        password = input("Password: ")

        for i in range(len(users)):
            if (username == users[i][0]) and (password == users[i][1]):
                state = i
                userin = users[i][0]
                break
            else:
                if username != users[i][0]:
                    state = -1
                if password != users[i][1]:
                    state = -2

        if state > 0:
            print("Selamat datang,", userin)
            print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil")
        else:
            if state == -1:
                print("Username tidak terdaftar!")
            elif state == -2:
                print("Password salah!")

    elif command == "logout":
        state = 0
        userin = ""


    return state, userin
