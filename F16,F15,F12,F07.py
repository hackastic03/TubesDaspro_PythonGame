# F07 Jin pembangun
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

# F15 HELP
def help() :
    if  role == 'bandung_bondowoso' :
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
        
    elif role == 'roro_jonggrang' :
        print ('=========== HELP ===========')
        print (''' 1. logout
    Untuk keluar dari akun yang digunakan sekarang''')
        print (''' 2. Hancurkan Candi
    Untuk menghancurkan candi agar menggagalkan rencana Bandung Bondowoso dan data candi terhapus''')
        print (''' 3. Ayam Berkokok
    Untuk menyelesaikan permainan dengan memalsukan pagi hari''')
        print
    elif role == 'jin_pembangun' :
        print ('=========== HELP ===========')
        print (''' 1. logout
    Untuk keluar dari akun yang digunakan sekarang''')
        print (''' 2. Jin Pembangun
    Untuk membangun candi dengan jumlah bahan yang tersedia jika jumlahnya mencukupi''')
    elif role == 'jin_pengumpul' :
        print ('=========== HELP ===========')
        print (''' 1. logout
    Untuk keluar dari akun yang digunakan sekarang''')
        print (''' 2. Jin Pengumpul
    Untuk mengumpulkan bahan untuk membangun candi berupa pasir,batu dan air''')
    elif role == ' ' :
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
