#by BarCode221
#jumat 16 September 2022
import os,sys,time
data = []
#melihat data
def cek_nama():
    if len(data) <= 0:
        print("Tidak Ada Data")
    else:
        for indexs in range(len(data)):
            print("[%d] %s" % (indexs, data[indexs]))
def tambah_data():
    nama = input("Masukan Nama:")
    data.append(nama)
def edit_data():
    print(cek_nama())
    nama = int(input("Masukan ID:"))
    if(nama > len(data)):
        print("id salah")
    else:
        nama_baru = input("Masukan Nama Baru:")
        data[nama] = nama_baru
def hapus_data():
    print(cek_nama())
    nama = int(input("Masukan ID:"))
    if(nama > len(data)):
        print("id salah")
    else:
        data.remove(data[nama])

def menu():
    os.system("clear")
    print("         [|Program Absen By Bar|]")
    print("")
    print("            [1] Cek Absen")
    print("")
    print("            [2] Tambah Data Absen")
    print("")
    print("            [3] Edit Data Absen")
    print("")
    print("            [4] Hapus Data Nama Pada Absen")
    print("")
    print("            [5] Keluar Dari Program")
    print("")
    pilih = input("Masukan Pilihan (1/5):")

    if pilih=="1":
        print(cek_nama())
        input("Enter Untuk Kembali Ke Menu:")
    elif pilih=="2":
        print(str(tambah_data()))
    elif pilih=="3":
        print(edit_data())
        input("Enter Untuk Kembali Ke Menu:")
    elif pilih=="4":
        print(hapus_data())
        input("Enter Untuk Kembali Ke Menu:")
    elif pilih=="5":
        print(exit())
    else:
        print("Tidak Ada Dalam Pilihan")
if __name__=="__main__":
    while True:
              menu()
