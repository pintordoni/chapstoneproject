hotel = {"h01":{"nama hotel":"fairmont", "nomor telepon hotel":"02187654321", "alamat hotel":"jakarta", "website hotel":"www.fairmont.com"}, 
        "h02":{"nama hotel":"borobudur", "nomor telepon hotel":"02186754321", "alamat hotel":"jakarta", "website hotel":"www.borobudur.com"}}
hotel_dummy = {}
def read():
    if len(hotel) <= 0:
        print("tidak ada nama hotel")
        readmenu()
    else:
        for i in hotel:
            print("Kode Hotel : {}, Nama hotel : {}, Nomor telepon hotel : {}, Alamat hotel : {}, Website : {}".format(i,hotel[i]["nama hotel"], hotel[i]["nomor telepon hotel"], hotel[i]["alamat hotel"], hotel[i]["website hotel"]) )
        readmenu()
def read1():
    idhotel = input("masukkan id hotel :")
    if idhotel not in hotel :
        print("tidak ada data hotel")
        readmenu()
    else:
        print("Kode Hotel : {}, Nama hotel : {}, Nomor telepon hotel : {}, Alamat hotel : {}, Website : {}".format(idhotel,hotel[idhotel]["nama hotel"], hotel[idhotel]["nomor telepon hotel"], hotel[idhotel]["alamat hotel"], hotel[idhotel]["website hotel"]) )
        readmenu()

def readmenu():
    print("-------Report Data Hotel-------")
    print("")
    print("1. Report Data Hotel")
    print("2. Report Data Hotel Tertentu")
    print("3. Kembali Ke Menu Utama")
    print("")
    report= input("Silahkan pilih sub menu data hotel :")
    if report == "1":
        read()
    elif report == "2":
        read1()
    elif report == "3":
        menuutama()
    else:
        readmenu()

def menuutama():
    print("-------Data Hotel Di Indonesia-------")
    print("")
    print("1. Menampilkan Data Hotel")
    print("2. Menambah Data Hotel")
    print("3. Mengubah Data Hotel")
    print("4. Menghapus Data Hotel")
    print("5. Exit")
    datahotel = input("Silahkan pilih menu utama :")
    if datahotel == "1":
        readmenu()
    elif datahotel == "2":
        createmenu()
    elif datahotel == "3":
        update_menu()
    elif datahotel == "4":
        deletemenu()
    elif datahotel == "5":
        print("Thank you for coming")
    else:
        print("Pilihan yang anda masukkan salah")
        menuutama()

def createmenu():
    print("-------Menambah Data Hotel-------")
    print("")
    print("1. Menambah data hotel")
    print("2. Kembali ke menu utama")
    print("")
    createhotel = input("Silahkan pilih sub menu create :")
    if createhotel == "1":
        tambahdata()
    elif createhotel == "2":
        menuutama()
    else:
        createmenu()

def tambahdata():
    global databaru
    databaru = input("Masukkan id hotel :").lower()
    global hotel

    if databaru in hotel:
        print("Data sudah ada")
        createmenu()
    else:
        namahotelbaru = input("Masukkan nama hotel :")
        nomorteleponbaru = input("Masukkan nomor telepon hotel :")
        alamatbaru = input("Masukkan alamat hotel :")
        websitehotelbaru = input("Masukkan website hotel :")
       
        m = 1
        while m != 0:
            notifdatabaru = input("Apakah data akan disimpan? (Y/N) :").capitalize()
            if notifdatabaru == 'Y':
                hotel_dummy["nama hotel"]=namahotelbaru
                hotel_dummy["nomor telepon hotel"]=nomorteleponbaru
                hotel_dummy["alamat hotel"]=alamatbaru
                hotel_dummy["website hotel"]=websitehotelbaru
                hotel[databaru] = hotel_dummy
                print("Data Tersimpan")
                m = 0
            elif notifdatabaru == 'N':
                print("Data tidak tersimpan")
                hotel = hotel
                m = 0
            else:
                m = 1
    createmenu()

def update_menu():
    print("-------Mengubah Data Hotel-------")
    print("")
    print("1. Mengubah data hotel")
    print("2. Kembali ke menu utama")
    print("")
    updatemenu = input("Silahkan pilih sub menu update :")
    if updatemenu == "1":
        ubahdata()
    elif updatemenu == "2":
        menuutama()
    else:
        update_menu()

def ubahdata():
    databaru = input("Masukkan id hotel :")
    global hotel
    if databaru in hotel:
        print("Nama hotel : {}, Nomor telepon hotel : {}, Alamat hotel : {}, Website : {}".format(databaru,hotel[databaru]["nama hotel"], hotel[databaru]["nomor telepon hotel"], hotel[databaru]["alamat hotel"], hotel[databaru]["website hotel"]) )
        m = 1
        while m != 0:
            notif = input("Tekan Y jika ingin Update Data atau N jika ingin cancel Update data (Y/N) :").capitalize()
            if notif == 'Y':
                kolom = input("Masukkan kolom/keterangan yang ingin di Update : ").lower()
                kolombaru = input("Masukkan {} baru : ".format(kolom))
                m = 1
                while m != 0:
                    notifupdate = input("Apakah Data akan di Update? (Y/N) : ").capitalize()
                    if notifupdate == 'Y':
                        print("Data Updated")
                        hotel[databaru][kolom] = kolombaru
                        m =0
                    elif notifupdate == 'N':
                        print("Data Tidak Terupdate")
                        m =0
                    else:
                        m = 1
                update_menu()
            elif notif == 'N':
                print("Data Tidak TerUpdate")
                m = 0
            else:
                m= 1
        update_menu()
    else:
        print("Data Tidak Ada")
        update_menu()
        
def deletemenu():
    print("-------Menghapus Data Hotel-------")
    print("")
    print("1. Menghapus data hotel")
    print("2. Kembali ke menu utama")
    print("")
    hapusmenu = input("Silahkan pilih sub menu delete : ").capitalize()
    if hapusmenu == "1":
        hapusdata()
    elif hapusmenu == "2":
        menuutama()
    else:
        deletemenu()

def hapusdata():
    datahotel = input("Masukkan id hotel : ")
    if datahotel in hotel:
        m = 1
        while m != 0:
            notifhapus = input("Apakah Data akan Dihapus (Y/N) : ").capitalize()
            if notifhapus == 'Y' :
                print("Data Terhapus")
                hotel.pop(datahotel)
                m = 0
            elif notifhapus == 'N':
                print("Data Tidak Terhapus")
                m = 0
            else:
                m = 1
        deletemenu()
    else: 
        print("Data Tidak Ada")
        deletemenu()
menuutama()