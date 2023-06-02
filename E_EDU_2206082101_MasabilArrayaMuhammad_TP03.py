#Nama : Masabil Arraya Muhammad
#NPM : 2206082101
#goal : ABIL NO PLAGIARISME BOYSSS!!!!
#Asumsi asumsi : 1. Nama itu case sensitive 2. pengguna ditempatkan di meja terkecil dulu baru keatas, misal ada yg kosong di meja 2 dan 7, user akan ditempatkan di meja 2
#3. makanan case sensitive, Thai Beef Salad akan beda dengan ThaI BeEf SALAD 4. pengguna dapat membaca harga (25000 akan sama dengan 25.000)
#5. apabila ada pengguna dengan nama sama, akan dianggap memesan ulang padahal meja belum selesai, akan di arahkan kembali
#Kode menu panjangnya selalu 3, misal Meals ke dua, menjadi M02, SIDES ke 7 menjadi S07 dan seterusnya
#TP3 adalah tp paling nguli #BOCAH PACIL STRONGGG
import turtle
a_list = []
b_list = []
c_list = []
ingin=""
jumlahhhh3=[]
user_input = "menu.txt" #Nama file berasal dari sini, contohnya meals.txt, menu.txt
daftar_nama = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
daftar_harga = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
daftar_pesanan = {}
daftar_pesanan2={}
semua_total_pesanan = {}
semua_total_pesanan2 = {}
semua_pesanan = []
input_file = open(user_input, "r").readlines()
input_file2 = open(user_input, "r").read().split()
total_pesanan = {}
harga_semua = []
semua_daftar_harga = {}
nama=""
index_nama = 0
keinginan2=""
indxx=0
t={}
t2={} #Maafkan daku apabila kode kode aku ribet
semua_file = []
total_file=[]
jumlahhhh=0
for i in input_file:
    if "===" in i and "\n" in i:
        a_list.append(i[3:-1]+ ":")
    elif "===" in i:
        a_list.append(i[3:]+":")
    elif "\n" in i:
        a_list.append(i[:-1])
    else:
        a_list.append(i)
for t in range(len(a_list)):
    a_list[t] = a_list[t].split(";")
for j in a_list:
    c_list.append(' '.join(j))
def pesan(): #menggunakan def
    nama = ""
    ingin = ""
    while ingin != "SELESAI":
        print("\n---\nSelamat datang di Kafe Daun Daun Pacilkom")
        ingin = input("Apa yang ingin anda lakukan? ")
        total_pesanan={}
        total_pesanan2={}
        harga_semua=[]
        semua_pesanan = []
        if ingin == "SELESAI":
            return
        if ingin == "BUAT PESANAN":
            if daftar_nama[9]!="":
                print("Mohon maaf meja sudah penuh, silakan kembali nanti.")
                continue
            nama = input("Siapa nama anda? ")
            if nama in daftar_pesanan:
                print("Anda sudah pernah Membuat pesanan sebelumnya,\nSilahkan ubah pesanan atau SELESAI")
                continue
            asu=0
            while asu==0:
                for i in range(0,10):
                    if nama in list(daftar_nama.values()):
                        asu +=1
                        break
                    if list(daftar_nama.values())[i] == "":
                        daftar_nama[i]= nama
                        asu+=1
                        index_nama=i
                        daftar_pesanan[nama]=""
                    if asu != 0:
                        break
                print("\nBerikut ini adalah menu yang kami sediakan:")
                for i in c_list:
                    print(i)
                pesanan=""
                while pesanan != "SELESAI":
                    f=0
                    pesanan = input("Masukkan menu yang ingin Anda pesan: ")
                    if pesanan == "SELESAI":
                        break
                    for c in a_list:
                        g=0
                        if pesanan in c:
                            print("Berhasil memesan " + c[1] + ".")
                            g+=1
                            if c[1] not in total_pesanan:
                                total_pesanan[c[1]] = 1
                                total_pesanan2[c[0]]=1
                                harga_semua.append([c[2]])
                                daftar_pesanan[nama] = c[0]
                                semua_pesanan.append(c[1])
                            else:
                                total_pesanan[c[1]] += 1
                                total_pesanan2[c[0]]+=1
                                daftar_pesanan[nama] += c[0]
                                semua_pesanan.append(c[1])
                            break
                    if g==0:
                        print(f"Menu " + pesanan + " tidak ditemukan")
                if len(total_pesanan)>=1:
                    print("\nBerikut ini adalah pesanan Anda:")
                    f=0
                    for i, j, k in zip(list(total_pesanan.items()),list(total_pesanan.items()),harga_semua):
                        print(f"{i[0]}" + " " + f"{j[1]} Buah, total Rp{int(k[0])*j[1]}")
                        f += int(k[0])*j[1]
                    for i,k in zip(daftar_nama.items(),daftar_harga):
                        if nama==i[1]:
                            print(f"Total pesanan: Rp{f}\nPesanan akan kami proses, Anda bisa menggunakan meja nomor {i[0]+1}. Terima kasih.")
                            daftar_harga[k]=f
                elif len(total_pesanan)==0:
                    print("u must choose something, silahkan kembali :)")
                daftar_pesanan[nama]=semua_pesanan
                semua_daftar_harga[nama]=harga_semua
                semua_total_pesanan[nama] = total_pesanan
                semua_total_pesanan2[nama]= total_pesanan2
        if ingin == "UBAH PESANAN":
            try:
                nomor_meja=int(input("Nomor meja berapa? "))
            except ValueError:
                print("harus berupa angka bulat, silahkan kembali")
                continue
            print("\nBerikut ini adalah menu yang kami sediakan:")
            for i in c_list:
                print(i)
            print("\nBerikut ini adalah pesanan Anda:")
            index_nama2= 0
            t = list(semua_total_pesanan.values())[nomor_meja-1]
            t2 = list(semua_total_pesanan2.values())[nomor_meja-1]
            for i,j,k in zip(list(semua_total_pesanan.values())[nomor_meja-1],t.values(),list(semua_daftar_harga.values())[nomor_meja-1]):
                print(f"{i} {j} buah, total Rp{int(k[0])*j}")
            keinginan2=""
            while keinginan2!="SELESAI":
                keinginan2 = input("Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN?")
                nama = daftar_nama[nomor_meja-1]
                if keinginan2 == "GANTI JUMLAH":
                    menu = input("Menu apa yang ingin anda ganti jumlahnya: ")
                    nama_pesanan=[]
                    jumllah=0
                    if len(menu)!=3:
                        g=0
                        bukti = 0
                        for i,c in zip(t,t2):
                            if menu == i:
                                try:
                                    jumllah = int(input("Masukkan jumlah pesanan yang baru: "))
                                except ValueError:
                                    print("Harus berupa angka, silahkan kembali\n")
                                    break
                                if jumllah<1:
                                    print("Jumlah harus bilangan positif!")
                                    break
                                t[i]=jumllah
                                t2[c]=jumllah
                                nama = daftar_nama[nomor_meja-1]
                                semua_pesanan=semua_total_pesanan[nama]
                                daftar_pesanan[nama]=""
                                nama_pesanan = []
                                for i,c in zip(t.values(),t.keys()):
                                    for g in range(0,i):
                                        nama_pesanan.append(c)
                                daftar_pesanan[nama]=[]
                                daftar_pesanan[nama]=nama_pesanan
                                g+=1
                                print(f"Berhasil mengubah pesanan {menu} {jumllah} buah")
                    elif len(menu)==3: #bila berupa kode
                        g=0
                        bukti = 0
                        jumllah = 0
                        for i,c in zip(t,t2):
                            if menu == c:
                                try:
                                    jumllah = int(input("Masukkan jumlah pesanan yang baru: "))
                                except ValueError:
                                    print("Harus berupa angka, silahkan kembali\n")
                                    break
                                if jumllah<1:
                                    print("Jumlah harus bilangan positif")
                                    break
                                t[i]=jumllah
                                t2[c]=jumllah
                                nama = daftar_nama[nomor_meja-1]
                                semua_pesanan=semua_total_pesanan[nama]
                                semua_pesanan2=semua_total_pesanan2[nama]
                                daftar_pesanan[nama]=""
                                nama_pesanan = []
                                for i,c in zip(t.values(),t.keys()):
                                    for g in range(0,i):
                                        nama_pesanan.append(c)
                                daftar_pesanan[nama]=nama_pesanan
                                g+=1
                                print(f"Berhasil mengubah pesanan {menu} {jumllah} buah")
                    if g==0 and jumllah<1:
                        print(f"Menu {menu} tidak Anda pesan sebelumnya.")
                        continue
                    for het in a_list:
                        if menu in het:
                            bukti+=1
                    if bukti==0:
                        print(f"Menu {menu} tidak ditemukan")
                        continue
                elif keinginan2=="HAPUS":
                    menu=""
                    bukti=0
                    menu = input("Menu apa yang ingin Anda hapus dari pesanan: ")
                    for t in a_list:
                        if menu in t:
                            bukti+=1
                    if bukti==0:
                        print(f"Menu {menu} tidak ditemukan!")
                        continue
                    if len(menu)>3:
                        if menu not in semua_total_pesanan[nama]:
                            print(f"Menu {menu} tidak anda pesan sebelumnya!")
                            continue
                        else:
                            try:
                                for i,c,y in zip(semua_total_pesanan[nama],semua_total_pesanan2[nama],semua_total_pesanan[nama].values()):
                                    if i == menu:
                                        print(f"{y} {menu} dihapus dari pesanan.")
                                        jeka = semua_total_pesanan[nama]
                                        jeka2=semua_total_pesanan2[nama]
                                        del jeka[menu]
                                        del jeka2[c]
                                        semua_total_pesanan[nama]=jeka
                                        semua_total_pesanan2[nama]=jeka2
                                        bukti+=1
                            except RuntimeError:
                                continue
                    elif len(menu)==3:
                        if menu not in semua_total_pesanan2[nama]:
                            print(f"Menu {menu} tidak anda pesan sebelumnya!")
                            continue
                        else:
                            try:
                                for c,i,y,se,xoxo in zip(semua_total_pesanan[nama],semua_total_pesanan2[nama],semua_total_pesanan[nama].values(),daftar_pesanan[nama],semua_daftar_harga[nama]):
                                    if i == menu:
                                        print(f"{y} {menu} dihapus dari pesanan.")
                                        jeka = semua_total_pesanan[nama]
                                        jeka2=semua_total_pesanan2[nama]
                                        del jeka2[menu]
                                        del jeka[c]
                                        semua_total_pesanan[nama]=jeka
                                        semua_total_pesanan2[nama]=jeka2
                                        bukti+=1
                                        daftar_pesanan[nama].remove(se)
                                        semua_daftar_harga[nama].remove(xoxo)
                            except RuntimeError:
                                continue
                    if bukti==0:
                        print(f"Menu {menu} tidak ditemukan!")
                elif keinginan2=="TAMBAH PESANAN": #prinsip tambah pesanan mirip dengan buat pesanan
                    pesanan=""
                    f=0
                    semua_pesanan= daftar_pesanan[nama]
                    total_pesanan=semua_total_pesanan[nama]
                    total_pesanan2=semua_total_pesanan2[nama]
                    harga_semua = semua_daftar_harga[nama]
                    pesanan = input("Masukkan menu yang ingin Anda pesan: ")
                    if pesanan == "SELESAI":
                        break   
                    for c in a_list:
                        g=0
                        if pesanan in c:
                            print("Berhasil memesan " + c[1] + ".")
                            g+=1
                            if c[1] not in total_pesanan:
                                total_pesanan[c[1]] = 1
                                total_pesanan2[c[0]]=1
                                harga_semua.append([c[2]])
                                semua_pesanan.append(c[1])
                            else:
                                total_pesanan[c[1]] += 1
                                total_pesanan2[c[0]]+=1
                                semua_pesanan.append(c[1])
                            break
                    if g==0:
                        print(f"Menu " + pesanan + " tidak ditemukan")
                    daftar_pesanan[nama]=semua_pesanan
                    semua_daftar_harga[nama]=harga_semua
                    semua_total_pesanan[nama] = total_pesanan
                    semua_total_pesanan2[nama]= total_pesanan2
            t2 = list(semua_total_pesanan2.values())[nomor_meja-1]
            t = list(semua_total_pesanan.values())[nomor_meja-1]
            print("\nBerikut ini adalah pesanan terbaru Anda:")
            kapi = semua_total_pesanan.values()
            f=0
            for i,j,k in zip(list(semua_total_pesanan.values())[nomor_meja-1],t.values(),list(semua_daftar_harga.values())[nomor_meja-1]):
                print(f"{i} {j} buah, total Rp{int(k[0])*j}")
                f+= int(k[0])*j
                daftar_harga[nomor_meja-1]=f
            print(f"\nTotal pesanan: Rp{f}")
        elif ingin=="SELESAI MENGGUNAKAN MEJA":
            try:
                nomor_meja=int(input("Nomor meja berapa? "))
            except ValueError:
                print("harus berupa nomor")
                continue
            if nomor_meja<1 or nomor_meja>10:
                print("Nomor meja hanya 1 - 10")
            else:
                nama = daftar_nama[nomor_meja-1]
                print(f"Pelanggan atas nama {nama} selesai menggunakan meja {nomor_meja}")
                faya = semua_total_pesanan[nama]
                faya2 = semua_total_pesanan2[nama]
                tete=semua_daftar_harga[nama]
                yoyo=[]
                for i in tete:
                    yoyo.append(i[0])
                with open(f"receipt_{nama}.txt", "w") as f:
                    for a,b,c,d in zip(faya2,faya,faya.values(),yoyo):
                        totalyeh= f";{d}"*c
                        f.write(f"{a};{b};{c}{totalyeh}\n")
                    f.write(f"\nTotal {daftar_harga[nomor_meja-1]}") #membuat file
                daftar_nama[nomor_meja-1]=""
                daftar_harga[nomor_meja-1] = 0
                del daftar_pesanan[nama]
                del semua_daftar_harga[nama]
                del semua_total_pesanan[nama]
                del semua_total_pesanan2[nama] #Menghapus data data
x=0
if len(c_list)!=len(set(c_list)): #Pengecekan apabila ada yg sama atau ada daftar menu lagi dibawah, misal meals satu diatas, dibawah ada lagi
    print("Daftar menu tidak valid, cek kembali menu.txt!")
    exit
elif x!=0:
    print("Daftar menu tidak valid, cek kembali menu.txt!")
    exit
else:
    pesan()                    
    print("\nTerimakasih telah berbelanja, silahkan datang kembali\nTerimakasih udah mau berjuang sampai sini <33")





