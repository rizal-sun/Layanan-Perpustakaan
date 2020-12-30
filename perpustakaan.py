#%%
#import module
import os
import datetime

#starter variable
Arsip=["Hansel and Gretel","Pengetahuan Umum"]
NIM="Unknown"
Nama="Unknown"
Kelas="Unknown"
Buku="Unknown"
Durasi=int
Tanggal=datetime.datetime.now()
konf="Unknown"
X=-1
Peminjam=[["12201099","12234567","12234567"],
          ["Fahri Rahman Hardi","Bambang Sutarto","Udin"],
          ["12.1A.39","12.1C.69","12.1A.39"],
          ["Rashoumon","Little Red Riding Hood","Pengetahuan Umum"],
          ["1-1-2021","1-3-2020","08-12-2020"],
          ["1","2","3"]]

#MAIN MENU
def Jenis_Layanan():
	print("     MENU UTAMA     ")
	print("Pilih layanan perpustakaan dengan memasukkan nomor berikut:")
	print(" [1]Peminjaman \n [2]Pengembalian \n [3]Kelola katalog buku")
	Layanan=input("\nLayanan : ")
	if Layanan=="1":
		print("\n-------------------------")
		print(" LAYANAN PEMINJAMAN BUKU ")
		print("-------------------------")
		Peminjaman()
	elif Layanan=="2":
		print("\n---------------------------")
		print(" LAYANAN PENGEMBALIAN BUKU ")
		print("---------------------------")
		Pengembalian()
	elif Layanan=="3":
		print("\n---------------------")
		print(" KELOLA KATALOG BUKU ")
		print("---------------------")
		Katalog()
	else:
		print("\nLayanan",Layanan,"tidak ditemukan.\nmasukkan nomor layanan yang sudah tersedia [1/2/3]. \n Contoh: \n Layanan : 1 \n")
		Jenis_Layanan()

#LAYANAN PEMINJAMAN
def Peminjaman():
	print("Pilih menu berikut: \n [1]Tambahkan Peminjam \n [2]Daftar Riwayat Peminjaman \n [0]Kembali")
	Menu1=input("Menu : ")
	if Menu1=="1":
		print("\n----------------------------")
		print("    MENAMBAHKAN PEMINJAM    ")
		print("----------------------------")
		Tambah_Peminjam()
	elif Menu1=="2":
		print("\n----------------------------------------------------------------------------------------------------------------------------------")
		print(" NIM\t\t NAMA\t\t\t KELAS\t\t BUKU YANG DIPINJAM\t\t TANGGAL PEMINJAMAN\t LAMA PEMINJAMAN")
		print("----------------------------------------------------------------------------------------------------------------------------------")
		for i in range(len(Peminjam[0])):
			print("",Peminjam[0][i],"\t",Peminjam[1][i],"\t",Peminjam[2][i],"\t",Peminjam[3][i],"\t",Peminjam[4][i],"\t\t",Peminjam[5][i],"minggu")
		print("\n Kembali ke menu peminjaman...")
		print("\n-------------------------")
		print(" LAYANAN PEMINJAMAN BUKU ")
		print("-------------------------")
		Peminjaman()
	elif Menu1=="0":
		Jenis_Layanan()
	else:
		print("Menu", Menu1, "tidak ditemukan.\n")
		Peminjaman()
#Menu[1]
def Tambah_Peminjam():
	#INPUT NIM
	NIM=input("NIM Peminjam : ")
	while NIM=="" or len(NIM)!=8:
		print("Input salah.\n")
		NIM=input("NIM Peminjam : ")
	#INPUT NAMA
	Nama=input("Nama Peminjam : ")
	while Nama=="":
		print("Input salah.\n")
		Nama=input("Nama Peminjam : ")
	#INPUT KELAS
	Kelas=input("Kelas Peminjam : ")
	while Kelas=="" or len(Kelas)!=8:
		print("Input salah.\n")
		Kelas=input("Kelas Peminjam : ")
	#INPUT BUKU
	Buku=input("Buku yang dipinjam : ")
	while (Buku.lower() not in str(Arsip).lower()) or Buku=="":
		if Buku=="":
			print("Input tidak boleh kosong.\n")
		else:
			print("Buku", Buku, "Tidak Ditemukan.\n")
		Buku=input("Buku yang dipinjam : ")
	#INPUT LAMA PEMINJAMAN
	Durasi=input("Catatan: Lama peminjaman tidak boleh dari 4 minggu\nLama Peminjaman(Minggu) : ")
	while (Durasi=="") or (Durasi not in range(5)):
		print("Input salah.\nPeminjaman tidak boleh lebih dari sebulan.\nInput tidak boleh kosong dan harus angka.\n")
		Durasi=int(input("Lama Peminjaman : "))
	print("\n-----------------")
	print(" DATA PEMINJAMAN ")
	print("-----------------")
	print("NIM Peminjam\t\t:", NIM)
	print("Nama Peminjam\t\t:", Nama)
	print("Kelas Peminjam\t\t:", Kelas)
	print("Nama Buku\t\t:", Buku)
	print("Tanggal Peminjaman\t:", Tanggal.strftime("%a, %d %b %Y"))
	print("Lama Peminjaman(Minggu)\t:", Durasi)
	Konfirmasi1(NIM,Nama,Kelas,Buku,Tanggal,Durasi)
def Konfirmasi1(NIM,Nama,Kelas,Buku,Tanggal,Durasi):
	Konf=input("\nApakah data ini sudah benar? [ya/tidak] \n\n > ")
	if konf=="Ya" or Konf=="ya":
		Peminjam[0].append(NIM)
		Peminjam[1].append(Nama)
		Peminjam[2].append(Kelas)
		Peminjam[3].append(Buku)
		Peminjam[4].append(Tanggal.strftime("%d-%m-%Y"))
		Peminjam[5].append(Durasi)
		print(" Berhasil menyimpan.\n Kembali ke menu peminjaman...\n")
		Peminjaman()
	elif Konf=="Tidak" or Konf=="tidak":
		print(" Kembali Menambahkan...\n")
		Tambah_Peminjam()
	else:
		print(" Input salah.\n")
		Konfirmasi1(NIM,Nama,Kelas,Buku,Tanggal,Durasi)

#LAYANAN PENGEMBALIAN
def Pengembalian():
	print("Pilih menu berikut: \n [1]Pengembalian Buku \n [2]Buku yang belum dikembalikan \n [0]Kembali")
	Menu2=input("Menu : ")
	if Menu2=="1":
		print("\n---------------------------")
		print("     PENGEMBALIAN BUKU     ")
		print("---------------------------")
		Pengembalian_Buku(X)
	elif Menu2=="2":
		print("\n---------------------------")
		print("      DAFTAR PEMINJAM      ")
		print("---------------------------")
		print("\n----------------------------------------------------------------------------------------------------------------------------------")
		print(" NIM\t\t NAMA\t\t\t KELAS\t\t BUKU YANG DIPINJAM\t\t TANGGAL PEMINJAMAN\t LAMA PEMINJAMAN")
		print("----------------------------------------------------------------------------------------------------------------------------------")
		for i in range(len(Peminjam[0])):
			print("",Peminjam[0][i],"\t",Peminjam[1][i],"\t",Peminjam[2][i],"\t",Peminjam[3][i],"\t",Peminjam[4][i],"\t\t",Peminjam[5][i],"minggu")
		print("\n Kembali ke menu pengembalian...")
		print("\n---------------------------")
		print(" LAYANAN PENGEMBALIAN BUKU ")
		print("---------------------------")
		Pengembalian()
	elif Menu2=="0":
		Jenis_Layanan()
	else:
		print("Menu", Menu2, "tidak ditemukan.\n")
		Pengembalian()
#menu [1]
def Pengembalian_Buku(X):
	while X==-1:
		Pengembali=input("Masukkan Nama Lengkap Peminjam : ")
		if Pengembali in Peminjam[1]:
			for i in range(len(Peminjam[1])):
				if Peminjam[1][i]==Pengembali:
					X=i
		else:
			print("Pengembali bernama",Pengembali,"tidak ditemukan")
	print("\n          DATA PEMINJAM")
	print("NIM Peminjam\t\t:", Peminjam[0][X])
	print("Nama Peminjam\t\t:", Peminjam[1][X])
	print("Kelas Peminjam\t\t:", Peminjam[2][X])
	print("Nama Buku\t\t:", Peminjam[3][X])
	print("Tanggal Peminjaman\t:", Peminjam[4][X])
	print("Lama Peminjaman(Minggu)\t:", Peminjam[5][X])
	Konfirmasi2(X)
def Konfirmasi2(X):
	Konf=input("\nApa benar peminjamnya memiliki data diatas? [ya/tidak] \n\n > ")
	if Konf=="Ya" or Konf=="ya":
		print(" Silahkan kembalikan buku yang dipinjam. \n Peminjam akan dihapus dari daftar.")
		Peminjam[0].pop(X)
		Peminjam[1].pop(X)
		Peminjam[2].pop(X)
		Peminjam[3].pop(X)
		Peminjam[4].pop(X)
		Peminjam[5].pop(X)
		print(" Kembali ke menu peminjaman... \n")
		Pengembalian()
	elif Konf=="Tidak" or Konf=="tidak":
		print(" Kembali Menambahkan...\n")
		X=-1
		Pengembalian_Buku(X)
	else:
		print(" Input salah.\n")
		Konfirmasi2(X)

#MANAGE KATALOG
def Katalog():
	print("Pilih menu berikut: \n [1]Tambahkan buku baru \n [2]Lihat katalog \n [0]Kembali")
	Menu3=input("Menu : ")
	if Menu3=="1":
		print("\n			TAMBAHKAN BUKU BARU")
		Tambah_Buku()
	elif Menu3=="2":
		print("\n			KATALOG")
		for BookLog in Arsip:
			print("\t",BookLog)
		print("\nKembali ke menu Katalog...\n")
		Katalog()
	elif Menu3=="0":
		Jenis_Layanan()
	else:
		print("Menu", Menu3, "tidak ditemukan.\n")
		Katalog()
#Menu[1]
def Tambah_Buku():
	Buku=input("Masukkan judul buku : ")
	print("\nJudul buku : ", Buku)
	Konfirmasi3(Buku)
def Konfirmasi3(Buku):
	Konf=input("\nApa judul buku sudah benar? [ya/tidak] \n\n > ")
	if Konf=="Ya" or Konf=="ya":
		Arsip.append(Buku)
		print(" Menambahkan buku berhasil.")
		print(" Kembali ke menu Katalog... \n")
		Katalog()
	elif Konf=="Tidak" or Konf=="tidak":
		Tambah_Buku()
	else:
		print(" Input salah.\n")
		Konfirmasi3(Buku)

#EXECUTE PROGRAM
os.system("cls")
print("---------------------------------")
print(" LAYANAN PERPUSTAKAAN KELOMPOK 3 ")
print("---------------------------------")
Jenis_Layanan()