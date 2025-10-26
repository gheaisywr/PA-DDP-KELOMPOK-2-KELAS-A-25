'''=================================================================================================================================='''


'''========================================  SISTEM PENGIRIMAN BARANG ANTAR PULAU DAN LUAR PULAU  ==================================='''


'''=================================================================================================================================='''
# Kelompok 2 PA DDP 2025
# 1. Alya Hauranisa Nugroho
# 2. Alif Anugrah Ramadhan
# 3. Ghea Aisyah Windraswari

import os
import sys
import json
import pwinput
import time
from prettytable import PrettyTable

'''=================================================================================================================================='''

'''                                                          JSON AKUN USER                                                          '''

'''=================================================================================================================================='''
def BacaDataAkun():
    try:
        with open('akunuser.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def SimpanDataAkun(data):
    with open('akunuser.json', 'w') as file:
        json.dump(data, file, indent=4)

'''=================================================================================================================================='''

'''                                                         JSON DATA PENGIRIMAN                                                     '''

'''=================================================================================================================================='''
def BacaDataPengiriman():
    try:
        with open('datapengiriman.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"Antar Pulau": [], "Luar Pulau": []}

def SimpanDataPengiriman(data):
    with open('datapengiriman.json', 'w') as file:
        json.dump(data, file, indent=4)

'''=================================================================================================================================='''

'''                                                                FUNGSI                                                            '''

'''=================================================================================================================================='''
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def animasiloading():
    bar_length = 40
    for i in range(bar_length + 1):
        progress = "=" * i + "-" * (bar_length - i)
        percent = (i / bar_length) * 100
        sys.stdout.write(f"\rTransaksi Pembelian [{progress}] {percent:.0f}%")
        sys.stdout.flush()
        time.sleep(0.10)
    print()

def enter(isi):
    while True:
        try:
            input(isi)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        except KeyboardInterrupt:
            print()
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue

def tabelpilihan(judul, list):
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = ["No", "Pilihan"]
    for i, item in enumerate(list, start=1):
        tabel.add_row([i, item])
    print(tabel)

def banner(isi):
    clear()
    print("╔" + "═"*80 + "╗")
    print("║" + isi.center(80) + "║")
    print("╚"+ "═"*80 + "╝")

def banners(isi):
    print("╔" + "═"*80 + "╗")
    print("║" + isi.center(80) + "║")
    print("╚"+ "═"*80 + "╝")

'''=================================================================================================================================='''

'''                                                            LOGIN ADMIN                                                           '''

'''=================================================================================================================================='''
akunadmin = [
    {"username": "alya",   "password": "admin123"},
    {"username": "alip", "password": "admin456"},
    {"username": "ghea", "password": "admin789"}
]

def login_admin():
    banner("LOGIN ADMIN")
    kesempatan = 3
    while kesempatan > 0:
        try:
            username = input("Masukkan username admin: ").strip()
            password = pwinput.pwinput("Masukkan password admin: ").strip()
            if any(admin["username"] == username and admin["password"] == password for admin in akunadmin):
                banner(f"LOGIN BERHASIL! Selamat datang {username}!")
                enter("Tekan ENTER untuk melanjutkan..")
                menu_admin()
                return True
            else:
                kesempatan -= 1
                banner(f"Username atau password salah! Sisa Kesempatan: {kesempatan}")
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue

    banner("Terlalu banyak percobaan! Kembali ke menu utama dalam 5 detik...")
    time.sleep(5)
    return False


'''=================================================================================================================================='''

'''                                                            LOGIN USER                                                            '''

'''=================================================================================================================================='''
def login_user():
    akunuser = BacaDataAkun()
    clear()
    while True:
        try:
            tabelpilihan("SUDAH PUNYA AKUN?", ["Ya, Saya sudah punya akun", "Belum, Saya ingin daftar akun"])
            punya_akun = input("Pilihan (1/2): ").strip()
            if punya_akun == "1":
                banner("LOGIN USER")
                kesempatan = 3
                while kesempatan > 0:
                    try:
                        username = input("Masukkan username: ").strip()
                        password = pwinput.pwinput("Masukkan password: ").strip()
                        if any(user["username"] == username and user["password"] == password for user in akunuser):
                            banner(f"LOGIN BERHASIL! Selamat datang {username}!")
                            enter("Tekan ENTER untuk melanjutkan..")
                            menu_user(username)
                            return True
                        else:
                            kesempatan -= 1
                            banner(f"Username atau password salah! Sisa Kesempatan: {kesempatan}")
                    except KeyboardInterrupt:
                        print("\n")
                        banner("MOHON TIDAK MENEKAN CTRL+C!")
                        continue
                banner("Terlalu banyak percobaan! Kembali ke menu utama dalam 5 detik...")
                time.sleep(5)
                break

            elif punya_akun == "2":
                regis_akun()

            else:
                banner("PILIHAN TIDAK VALID! Silahkan pilih 1 atau 2.")

        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue

'''=================================================================================================================================='''

'''                                                       REGISTRASI AKUN USER                                                       '''

'''=================================================================================================================================='''
def regis_akun():
    akunuser = BacaDataAkun()
    banner("REGISTRASI AKUN USER")
    while True:
        try:
            username = input("Buat username: ").strip()
            if any(user["username"] == username for user in akunuser):
                banner("Username sudah terdaftar! Silahkan coba username lain.")
                continue
            if " " in username:
                banner("USERNAME TIDAK BOLEH MENGANDUNG SPASI!")
                continue
            if len(username) < 3 or len(username) > 10:
                banner("USERNAME HARUS MEMILIKI 3-10 KARAKTER!")
                continue

            password = pwinput.pwinput("Buat password: ").strip()
            if " " in password:
                banner("PASSWORD TIDAK BOLEH MENGANDUNG SPASI!")
                continue
            if len(password) < 6 or len(password) > 12:
                banner("PASSWORD HARUS MEMILIKI 6-12 KARAKTER!")
                continue
            verif_password = pwinput.pwinput("Konfirmasi password: ").strip()
            if password != verif_password:
                banner("PASSWORD TIDAK SESUAI! Silahkan coba lagi!")
                continue

            akunuser.append({
                "username": username, 
                "password": password, 
                "saldo": 0,
                "akun": "bronze",
                "poin": 0})
            SimpanDataAkun(akunuser)

            banner("Registrasi berhasil! Kembali ke menu utama...")
            time.sleep(3)
            menu_utama()
            return

        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue

'''=================================================================================================================================='''

'''                                               MENU ADMIN (1) TAMBAH DATA PENGIRIMAN                                              '''

'''=================================================================================================================================='''
def idpengiriman(data, jenis):
    if jenis == "Antar Pulau":
        label = "A"
    elif jenis == "Luar Pulau":
        label = "L"
    else:
        print("Tidak Diketahui")
    datapengiriman = data[jenis]
    if not datapengiriman:
        return f"{label}001"
    else:
        id = [int(d["id_pengiriman"][1:]) for d in datapengiriman]
        idbaru = max(id) + 1
        return f"{label}{idbaru:03d}"


def tambah_pengiriman():
    banner("TAMBAH DATA PENGIRIMAN BARANG")
    data = BacaDataPengiriman()

    while True:
        try:
            pengirim = input("Nama Pengirim: ").strip()
            if pengirim == "":
                banner("NAMA PENGIRIM TIDAK BOLEH KOSONG!")
                continue

            penerima = input("Nama Penerima: ").strip()
            if penerima == "":
                banner("PENGISIAN DIULANG! NAMA PENERIMA TIDAK BOLEH KOSONG!")
                continue

            asal = input("Alamat Asal: ").strip()
            if asal == "":
                banner("PENGISIAN DIULANG! ALAMAT ASAL TIDAK BOLEH KOSONG!")
                continue

            tujuan = input("Alamat Tujuan: ").strip()
            if tujuan == "":
                banner("PENGISIAN DIULANG! ALAMAT TUJUAN TIDAK BOLEH KOSONG!")
                continue
            break
        except KeyboardInterrupt:
            print("\n")
            banner("PENGISIAN DIULANG. MOHON TIDAK MENEKAN CTRL+C!")


    clear()
    while True:
        try:
            tabelpilihan("Jenis Pengiriman", ["Antar Pulau (+Rp5.000)", "Luar Pulau (+Rp15.000)"])
            pilih = input("Pilih (1/2): ").strip()
            if pilih == "1":
                jenis = "Antar Pulau"
                tarif = 5000
                break
            elif pilih == "2":
                jenis = "Luar Pulau"
                tarif = 15000
                break
            else:
                banner("MASUKKAN ANGKA 1 ATAU 2!")
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")


    clear()
    while True:
        try:
            barang = input("Barang: ").strip()
            if barang == "":
                banner("NAMA BARANG TIDAK BOLEH KOSONG!")
                continue
            break
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")

    while True:
        try:
            berat = float(input("Berat Barang (kg): ").strip())
            if berat <= 0 or berat > 100:
                banner("BERAT HARUS LEBIH DARI 0 DAN MAKSIMAL 100 KG!")
                continue
            break
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
        except ValueError:
            banner("MASUKKAN ANGKA!")

    clear()
    while True:
        try:
            tabelpilihan("Layanan Pengiriman", ["Reguler (Rp4000/kg)", "Express (Rp6000/kg)", "Kargo (Rp3500/kg)"])
            pilih = input("Pilih (1/2/3): ").strip()
            if pilih == "1":
                layanan = "Reguler"
                faktor = 4000
                break
            elif pilih == "2":
                layanan = "Express"
                faktor = 6000
                break
            elif pilih == "3":
                layanan = "Kargo"
                faktor = 3500
                break
            else:
                banner("MASUKKAN ANGKA 1 SAMPAI 3!")
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")

    clear()
    while True:
        try:
            estimasi = input("Estimasi (DD/MM/YYYY): ").strip()
            if len(estimasi) != 10 or estimasi[2] != '/' or estimasi[5] != '/':
                banner("MASUKKAN SESUAI FORMAT TANGGAL! (DD/MM/YYYY)")
                continue
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue
        break

    ongkir = int(berat * faktor + tarif)
    id = idpengiriman(data, jenis)
    user = "-"

    data[jenis].append({
        "user" : user,
        "id_pengiriman": id,
        "nama_pengirim": pengirim,
        "nama_penerima": penerima,
        "alamat_asal": asal,
        "alamat_tujuan": tujuan,
        "jenis_pengiriman": jenis,
        "barang": barang,
        "berat_barang": berat,
        "layanan_pengiriman": layanan,
        "ongkir": ongkir,
        "status_pengiriman": "Diproses",
        "estimasi": estimasi,
    })

    SimpanDataPengiriman(data)

    tabel = PrettyTable()
    tabel.title = "RINGKASAN DATA PENGIRIMAN BARU"
    tabel.field_names = ["ID", "Detail Pengiriman"]
    detail_pengiriman = (
                        f"Pengirim     : {pengirim}\n"
                        f"Penerima     : {penerima}\n"
                        f"Asal         : {asal}\n"
                        f"Tujuan       : {tujuan}\n"
                        f"Jenis        : {jenis}\n"
                        f"Barang       : {barang}\n"
                        f"Berat        : {berat}kg\n"
                        f"Layanan      : {layanan}\n"
                        f"Ongkir       : Rp{ongkir}\n"
                        f"Status       : Diproses\n"
                        f"Estimasi     : {estimasi}"
                        )
    tabel.align["Detail Pengiriman"] = "l"
    tabel.add_row([id, detail_pengiriman])
    clear()
    print(tabel)
    banners("DATA PENGIRIMAN BERHASIL DITAMBAHKAN!")
    enter("Tekan ENTER untuk kembali ke menu..")

'''=================================================================================================================================='''

'''                                                    MENU ADMIN (2) LIHAT PENGIRIMAN                                               '''

'''=================================================================================================================================='''
def lihat_pengiriman():
    data = BacaDataPengiriman()
    if not data:
        banners("BELUM ADA DATA PENGIRIMAN")
        enter("Tekan ENTER untuk kembali ke menu..")
        return None
    
    while True:
        try:
            tabelpilihan("PILIH JENIS PENGIRIMAN", ["Antar Pulau", "Luar Pulau"])
            pilihan = input("Pilih (1/2): ").strip()
            if pilihan == '1':
                jenis = "Antar Pulau"
                break
            elif pilihan == '2':
                jenis = "Luar Pulau"
                break
            else:
                banner("MASUKKAN ANGKA 1 ATAU 2!")
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue  

    if jenis not in data or not data[jenis]:
        banner(f"TIDAK ADA DATA PENGIRIMAN UNTUK {jenis.upper()}")
        enter("Tekan ENTER untuk kembali ke menu..")
        return None
    
    banner(f"DATA PENGIRIMAN JENIS {jenis.upper()}")
    tabel = PrettyTable()
    tabel.field_names = [
        "ID", "Nama Pengirim", "Nama Penerima", "Asal", 
        "Tujuan", "Jenis", "Barang", "Berat", 
        "Layanan", "Ongkir", "Status", "Estimasi"
    ]
    for i in data[jenis]:
        tabel.add_row([
            i["id_pengiriman"],
            i["nama_pengirim"],
            i["nama_penerima"],
            i["alamat_asal"],
            i["alamat_tujuan"],
            i["jenis_pengiriman"],
            i["barang"],
            f"{i['berat_barang']} kg",
            i["layanan_pengiriman"],
            f"Rp{i['ongkir']}",
            i["status_pengiriman"],
            i["estimasi"]
        ])
    while True:
        try:
            print(tabel)
            input("Tekan ENTER untuk melanjutkan..")
        except KeyboardInterrupt:
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue
        return jenis

'''=================================================================================================================================='''

'''                                                 MENU ADMIN (3) UBAH DATA PENGIRIMAN                                              '''

'''=================================================================================================================================='''
def ubah_data_pengiriman():
    banner("UBAH DATA PENGIRIMAN")
    data = BacaDataPengiriman()
    if not data:
        banner("BELUM ADA DATA PENGIRIMAN")
        enter("Tekan ENTER untuk kembali ke menu..")
        return
    
    jenis = lihat_pengiriman()
    if not jenis:
        return
    datajenis = data[jenis]

    id = input("Masukkan ID Pengiriman yang ingin diubah: ").strip().upper()
    pengiriman = None
    for d in datajenis:
        if d["id_pengiriman"] == id:
            pengiriman = d
            break

    if not pengiriman:
        banner("ID PENGIRIMAN TIDAK DITEMUKAN!")
        enter("Tekan ENTER untuk kembali ke menu..")
        return

    clear()
    while True:
        try:
            tabelpilihan("PILIH JENIS PERUBAHAN", ["Ubah Detail Pengiriman", "Ubah Status Pengiriman", "Ubah Estimasi Pengiriman"])
            pilih_ubah = input("Pilih (1/2/3): ").strip()
            if pilih_ubah in ['1', '2', '3']:
                break
            else:
                banner("MASUKKAN ANGKA 1 SAMPAI 3!")
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue

    if pilih_ubah == '1':
        clear()
        while True:
            try:
                banners("UBAH DATA PENGIRIMAN (Kosongkan jika tidak ingin mengubah)")
                nama_pengirim = input(f"Nama Pengirim [{pengiriman['nama_pengirim']}]: ").strip() or pengiriman['nama_pengirim']
                nama_penerima = input(f"Nama Penerima [{pengiriman['nama_penerima']}]: ").strip() or pengiriman['nama_penerima']
                alamat_asal = input(f"Alamat Asal [{pengiriman['alamat_asal']}]: ").strip() or pengiriman['alamat_asal']
                alamat_tujuan = input(f"Alamat Tujuan [{pengiriman['alamat_tujuan']}]: ").strip() or pengiriman['alamat_tujuan']
            except KeyboardInterrupt:
                print("\n")
                banner("PENGISIAN DIULANG. MOHON TIDAK MENEKAN CTRL+C!")
                continue
            break

        pengiriman.update({
            "nama_pengirim": nama_pengirim,
            "nama_penerima": nama_penerima,
            "alamat_asal": alamat_asal,
            "alamat_tujuan": alamat_tujuan,
        })
        SimpanDataPengiriman(data)
        banner(f"DATA PENGIRIMAN DENGAN ID {id} BERHASIL DIUBAH!")
        enter("Tekan ENTER untuk kembali ke menu..")

    elif pilih_ubah == '2':
        clear()
        while True:
            try:
                tabelpilihan("STATUS PENGIRIMAN", ["Diproses", "Dikirim", "Selesai"])
                pilih_status = input("Pilih (1/2/3): ").strip()
                if pilih_status == '1':
                    pengiriman["status_pengiriman"] = "Diproses"
                    break
                elif pilih_status == '2':
                    pengiriman["status_pengiriman"] = "Dikirim"
                    break
                elif pilih_status == '3':
                    pengiriman["status_pengiriman"] = "Selesai"
                    break
                else:
                    banner("MASUKKAN ANGKA 1 SAMPAI 3!")
            except KeyboardInterrupt:
                print("\n")
                banner("MOHON TIDAK MENEKAN CTRL+C!")
                continue
        SimpanDataPengiriman(data)
        banner(f"STATUS PENGIRIMAN DENGAN ID {id} BERHASIL DIUBAH!")
        enter("Tekan ENTER untuk kembali ke menu..")

    elif pilih_ubah == '3':
        banner("UBAH ESTIMASI PENGIRIMAN (DD/MM/YYYY)")
        while True:
            try:
                estimasi = input(f"Estimasi Pengiriman [{pengiriman['estimasi']}]: ").strip()
                if len(estimasi) != 10 or estimasi[2] != '/' or estimasi[5] != '/':
                    banner("MASUKKAN SESUAI FORMAT TANGGAL! (DD/MM/YYYY)")
                    continue
            except KeyboardInterrupt:
                print("\n")
                banner("MOHON TIDAK MENEKAN CTRL+C!")
                continue
            break

        pengiriman.update({
            "estimasi": estimasi,
            })

        SimpanDataPengiriman(data)
        banner(f"ESTIMASI PENGIRIMAN DENGAN ID {id} BERHASIL DIUBAH!")
        enter("Tekan ENTER untuk kembali ke menu..")

'''=================================================================================================================================='''

'''                                                 MENU ADMIN (4) HAPUS DATA PENGIRIMAN                                              '''

'''=================================================================================================================================='''
def hapus_pengiriman():
    banner("HAPUS DATA PENGIRIMAN")
    data = BacaDataPengiriman()

    if not data:
        banner("BELUM ADA DATA PENGIRIMAN")
        enter("Tekan ENTER untuk kembali ke menu..")
        return
    
    jenis = lihat_pengiriman()
    if not jenis:
        return
    datajenis = data[jenis]

    while True:
        try:
            idp = input("Masukkan ID Pengiriman yang ingin dihapus: ").strip().upper()
            for d in datajenis:
                if d["id_pengiriman"] == idp:
                    datajenis.remove(d)
                    SimpanDataPengiriman(data)
                    banner(f"DATA PENGIRIMAN DENGAN ID: {idp} BERHASIL DIHAPUS!")
                    input("Tekan ENTER untuk kembali ke menu..")
                    return
            else:
                banner("ID TIDAK DITEMUKAN!")
                enter("Tekan ENTER untuk kembali ke menu..")
                break
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue

'''=================================================================================================================================='''

'''                                                 MENU USER (1) TAMBAH PENGIRIMAN BARANG                                           '''

'''=================================================================================================================================='''
def tambah_pengiriman_user(username):
    banner("TAMBAH PENGIRIMAN BARANG")
    data = BacaDataPengiriman()
    akunuser = BacaDataAkun()

    user = None
    for u in akunuser:
        if u["username"] == username:
            user = u
            break


    while True:
        try:
            pengirim = input("Nama Pengirim: ").strip()
            if pengirim == "":
                banner("NAMA PENGIRIM TIDAK BOLEH KOSONG!")
                continue

            penerima = input("Nama Penerima: ").strip()
            if penerima == "":
                banner("PENGISIAN DIULANG. NAMA PENERIMA TIDAK BOLEH KOSONG!")
                continue

            asal = input("Alamat Asal: ").strip()
            if asal == "":
                banner("PENGISIAN DIULANG. ALAMAT ASAL TIDAK BOLEH KOSONG!")
                continue

            tujuan = input("Alamat Tujuan: ").strip()
            if tujuan == "":
                banner("PENGISIAN DIULANG. ALAMAT TUJUAN TIDAK BOLEH KOSONG!")
                continue
            break
        except KeyboardInterrupt:
            print("\n")
            banner("PENGISIAN DIULANG. MOHON TIDAK MENEKAN CTRL+C!")


    clear()
    while True:
        try:
            tabelpilihan("Jenis Pengiriman", ["Antar Pulau (+Rp5.000)", "Luar Pulau (+Rp15.000)"])
            pilih = input("Pilih (1/2): ").strip()
            if pilih == "1":
                jenis = "Antar Pulau"
                tarif = 5000
                break
            elif pilih == "2":
                jenis = "Luar Pulau"
                tarif = 15000
                break
            else:
                banner("MASUKKAN ANGKA 1 ATAU 2!")
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")


    clear()
    while True:
        try:
            barang = input("Barang: ").strip()
            if barang == "":
                banner("NAMA BARANG TIDAK BOLEH KOSONG!")
                continue
            break
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")

    while True:
        try:
            berat = float(input("Berat Barang (kg): ").strip())
            if berat <= 0 or berat > 100:
                banner("BERAT HARUS LEBIH DARI 0 DENGAN MAKSIMAL 100 KG!")
                continue
            break
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
        except ValueError:
            banner("MASUKKAN ANGKA!")


    clear()
    while True:
        try:
            tabelpilihan("Layanan Pengiriman", ["Reguler (Rp4000/kg)", "Express (Rp6000/kg)", "Kargo (Rp3500/kg)"])
            pilih = input("Pilih (1/2/3): ").strip()
            if pilih == "1":
                layanan = "Reguler"
                faktor = 4000
                break
            elif pilih == "2":
                layanan = "Express"
                faktor = 6000
                break
            elif pilih == "3":
                layanan = "Kargo"
                faktor = 3500
                break
            else:
                banner("MASUKKAN ANGKA 1 SAMPAI 3!")
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")

    ongkir = int(berat * faktor + tarif)

    jenisakun = user.get("akun")
    if jenisakun == "gold":
        diskon = ongkir * 0.1
        ongkir_setelah_diskon = int(ongkir - diskon)
    else:
        diskon = 0
        ongkir_setelah_diskon = ongkir

    id = idpengiriman(data, jenis)
    estimasi = "Belum ditentukan"
    waktu_transaksi = time.strftime("%d/%m/%Y %H:%M:%S")


    tabel = PrettyTable()
    tabel.title = "RINGKASAN DATA PENGIRIMAN ANDA"
    tabel.field_names = ["ID", "Detail Pengiriman"]
    detail = (
        f"Pengirim     : {pengirim}\n"
        f"Penerima     : {penerima}\n"
        f"Asal         : {asal}\n"
        f"Tujuan       : {tujuan}\n"
        f"Jenis        : {jenis}\n"
        f"Barang       : {barang}\n"
        f"Berat        : {berat}kg\n"
        f"Layanan      : {layanan}"
    )
    tabel.align["Detail Pengiriman"] = "l"
    tabel.add_row([id, detail])


    clear()
    saldo_user = user["saldo"]
    while True:
        try:
            print(tabel)
            banners("KONFIRMASI PEMBAYARAN")
            if jenisakun == "gold":
                print(f"Akun Anda     : GOLD (Diskon 10%)")
                print(f"Ongkir        : Rp{ongkir}")
                print(f"Potongan      : Rp{int(diskon)}")
                print(f"Total Ongkir  : Rp{ongkir_setelah_diskon}")
                print(f"Saldo Anda    : Rp{saldo_user}")
            else:
                print(f"Akun Anda     : BRONZE")
                print(f"Total Ongkir  : Rp{ongkir_setelah_diskon}")
                print(f"Saldo Anda    : Rp{saldo_user}")

            konfirmasi = input("Lanjutkan pembayaran? (1. Ya / 2. Tidak): ").strip()

            if konfirmasi == "1":
                if saldo_user < ongkir_setelah_diskon:
                    banner("SALDO TIDAK MENCUKUPI! SILAKAN TOP UP DI MENU SHIPPAY.")
                    enter("Tekan ENTER untuk kembali ke menu..")
                    return
                else:
                    user["saldo"] -= ongkir_setelah_diskon
                    user["poin"] = user.get("poin") + 250
                    SimpanDataAkun(akunuser)
                    animasiloading()
                    banner("PEMBAYARAN BERHASIL! PESANAN DIPROSES..")
                    time.sleep(3)
            elif konfirmasi == "2":
                banners("PESANAN DIBATALKAN.")
                enter("Tekan ENTER untuk kembali ke menu..")
                return
            else:
                banner("PILIHAN TIDAK VALID. MASUKKAN ANGKA 1 ATAU 2!")
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue
        break


    data[jenis].append({
        "user": username,
        "id_pengiriman": id,
        "nama_pengirim": pengirim,
        "nama_penerima": penerima,
        "alamat_asal": asal,
        "alamat_tujuan": tujuan,
        "jenis_pengiriman": jenis,
        "barang": barang,
        "berat_barang": berat,
        "layanan_pengiriman": layanan,
        "ongkir": ongkir_setelah_diskon,
        "status_pengiriman": "Diproses",
        "estimasi": estimasi
    })
    SimpanDataPengiriman(data)


    clear()
    invoice = PrettyTable()
    invoice.title = "INVOICE PESANAN ANDA"
    invoice.field_names = ["ID", "Detail Pengiriman"]
    detail = (
        f"Pengirim       : {pengirim}\n"
        f"Penerima       : {penerima}\n"
        f"Asal           : {asal}\n"
        f"Tujuan         : {tujuan}\n"
        f"Jenis          : {jenis}\n"
        f"Barang         : {barang}\n"
        f"Berat          : {berat}kg\n"
        f"Layanan        : {layanan}\n"
        f"Ongkir         : Rp{ongkir_setelah_diskon}\n"
        f"Status         : Diproses\n"
        f"Estimasi       : {estimasi}\n"
        f"Waktu Transaksi: {waktu_transaksi}"
    )
    invoice.align["Detail Pengiriman"] = "l"
    invoice.add_row([id, detail])

    print(invoice)
    banners("PENGIRIMAN BERHASIL DIBUAT!")
    banners(f"ANDA MENDAPATKAN 250 POIN! Poin anda sekarang: {user['poin']}")
    enter("Tekan ENTER untuk kembali ke menu..")

'''=================================================================================================================================='''

'''                                                 MENU USER (2) LIHAT PENGIRIMAN ANDA                                              '''

'''=================================================================================================================================='''
def lihat_pengiriman_anda(username):
    data = BacaDataPengiriman()
    banner(f"DATA PENGIRIMAN ANDA")

    semuapengiriman = data["Antar Pulau"] + data["Luar Pulau"]

    pengiriman_user = [p for p in semuapengiriman if p["user"] == username]

    if not pengiriman_user:
        banner("ANDA BELUM MEMILIKI DATA PENGIRIMAN.")
        enter("Tekan ENTER untuk kembali ke menu...")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID", "DETAIL PENGIRIMAN"]
    tabel.align["ID PENGIRIMAN"] = "l"
    tabel.align["DETAIL PENGIRIMAN"] = "l"

    for p in pengiriman_user:
        detail = (
            f"Pengirim: {p['nama_pengirim']}\n"
            f"Penerima: {p['nama_penerima']}\n"
            f"Asal: {p['alamat_asal']}\n"
            f"Tujuan: {p['alamat_tujuan']}\n"
            f"Barang: {p['barang']}\n"
            f"Berat: {p['berat_barang']} kg\n"
            f"Layanan: {p['layanan_pengiriman']}\n"
            f"Ongkir: Rp{p['ongkir']}\n"
            f"Status: {p['status_pengiriman']}\n"
            f"Estimasi: {p['estimasi']}"
            "\n-------------------------------------------------------------"
        )
        tabel.add_row([p["id_pengiriman"], detail])

    print(tabel)
    enter("Tekan ENTER untuk kembali ke menu...")


'''=================================================================================================================================='''

'''                                                 MENU USER (3) LOGIN SHIP-PAY                                                     '''

'''=================================================================================================================================='''
def login_shippay(username):
    datauser = BacaDataAkun()
    banner(f"LOGIN SHIPPAY │ USER: {username}")
    kesempatan = 3

    while kesempatan > 0:
        try:
            password = pwinput.pwinput("Masukkan password akun Anda: ").strip()
            for user in datauser:
                if user["username"] == username and user["password"] == password:
                    banner(f"LOGIN BERHASIL! Selamat datang di Ship-Pay, {username}!")
                    enter("Tekan ENTER untuk masuk ke menu Ship-Pay..")
                    menu_shippay(user)
                    return True

            kesempatan -= 1
            banner(f"Password salah! Sisa Kesempatan: {kesempatan}")

        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue

    banner("Terlalu banyak percobaan! Kembali ke menu user dalam 5 detik...")
    time.sleep(5)
    return False

'''=================================================================================================================================='''

'''                                                 MENU USER (3) MENU SHIP-PAY                                                     '''

'''=================================================================================================================================='''
def menu_shippay(user):
    datauser = BacaDataAkun()
    usershippay = user["username"]
    banner("MENU ShipPay")

    while True:
        try:
            for u in datauser:
                if u["username"] == usershippay:
                    jenisakun = u["akun"]
                    saldo = u["saldo"]
                    poin = u["poin"]
                    break

            tabelpilihan(
                f"MENU ShipPay │ USER: {usershippay} │ AKUN: {jenisakun.upper()} │ POIN: {poin}",
                ["Lihat Saldo", "Top Up Saldo", "Upgrade ke Akun GOLD", "Kembali ke Menu User"]
            )
            pilihan = input("Pilih menu (1/2/3/4): ").strip()

            if pilihan == "1":
                banner(f"Saldo ShipPay Anda saat ini: Rp{saldo}")
                enter("Tekan ENTER untuk kembali ke menu..")


            elif pilihan == "2":
                banner(f"Saldo ShipPay Anda saat ini: Rp{saldo}")
                while True:
                    try:
                        topup = int(input("Masukkan jumlah top up: ").strip())
                        if topup < 10000:
                            banner("MINIMAL TOP-UP RP 10.000!")
                            continue
                        if topup > 200000:
                            banner("MAKSIMAL TOP-UP RP 200.000!")
                            continue
                        for u in datauser:
                            if u["username"] == usershippay:
                                u["saldo"] += topup
                                SimpanDataAkun(datauser)
                                banner(f"TOP-UP BERHASIL! Saldo saat ini: Rp{u['saldo']}")
                                enter("Tekan ENTER untuk kembali ke menu..")
                        break
                    except ValueError:
                        banner("MASUKKAN ANGKA!")
                        continue
                    except KeyboardInterrupt:
                        print("\n")
                        banner("MOHON TIDAK MENEKAN CTRL+C!")
                        continue


            elif pilihan == "3":
                clear()
                while True:
                    try:
                        banners(f"Poin Anda saat ini: {poin}")
                        if jenisakun.lower() == "gold":
                            banner("ANDA SUDAH MEMILIKI AKUN GOLD!")
                            enter("Tekan ENTER untuk kembali ke menu..")
                            break
                        konfirmasi = input("Apakah Anda ingin upgrade ke akun GOLD (1000 poin)? (1. Ya / 2. Tidak): ").strip()
                        if konfirmasi == "1":
                            if poin >= 1000:
                                for u in datauser:
                                    if u["username"] == usershippay:
                                        u["poin"] -= 1000
                                        u["akun"] = "gold"
                                        SimpanDataAkun(datauser)
                                        banner("SELAMAT! AKUN ANDA TELAH DI-UPGRADE KE GOLD :D")
                                        enter("Tekan ENTER untuk kembali ke menu..")
                                break
                            else:
                                banner("POIN ANDA TIDAK CUKUP UNTUK UPGRADE KE AKUN GOLD!")
                                enter("Tekan ENTER untuk kembali ke menu..")
                                break
                        elif konfirmasi == "2":
                            banner("Upgrade akun dibatalkan.")
                            enter("Tekan ENTER untuk kembali ke menu..")
                            break
                        else:
                            banner("PILIHAN TIDAK VALID! MASUKKAN 1 ATAU 2!")
                    except KeyboardInterrupt:
                        print("\n")
                        banner("MOHON TIDAK MENEKAN CTRL+C!")
                        continue


            elif pilihan == "4":
                banner("Kembali ke menu user dalam 3 detik..")
                time.sleep(3)
                break

            else:
                banner("PILIHAN TIDAK VALID! MASUKKAN ANGKA 1 SAMPAI 4!")

        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue

'''=================================================================================================================================='''

'''                                                               MENU UTAMA                                                         '''

'''=================================================================================================================================='''
def menu_utama():
    clear()
    while True:
        try:
            banners("SISTEM PENGIRIMAN BARANG ANTAR PULAU & LUAR PULAU")
            banners("Selamat Datang! Silahkan login terlebih dahulu")
            pilihan = ["Login sebagai Admin", "Login sebagai User", "Keluar >>>"]
            tabelpilihan("MENU UTAMA", pilihan)
            pilih = input("Pilih menu (1/2/3): ").strip()
            if pilih == '1':
                login_admin()
            elif pilih == '2':
                login_user()
            elif pilih == '3':
                banner("TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM KAMI!")
                exit()
            else:
                banner("MASUKKAN ANGKA 1 SAMPAI 3!")
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue

'''=================================================================================================================================='''

'''                                                                MENU ADMIN                                                        '''

'''=================================================================================================================================='''
def menu_admin():
    while True:
        try:
            pilihan = [
                "Tambah Data Pengiriman",
                "Lihat Data Pengiriman",
                "Ubah Data Pengiriman",
                "Hapus Data Pengiriman",
                "Kembali ke Menu Utama"
            ]
            tabelpilihan("MENU ADMIN", pilihan)
            pilih = input("Pilih menu (1/2/3/4/5): ").strip()
            if pilih == '1':
                clear()
                tambah_pengiriman()
                clear()
            elif pilih == '2':
                clear()
                lihat_pengiriman()
                clear()
            elif pilih == '3':
                clear()
                ubah_data_pengiriman()
                clear()
            elif pilih == '4':
                clear()
                hapus_pengiriman()
                clear()
            elif pilih == '5':
                banner("TERIMA KASIH! Kembali ke menu utama dalam 3 detik...")
                time.sleep(3)
                break
            else:
                banner("MASUKKAN ANGKA 1 SAMPAI 5!")
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue

'''=================================================================================================================================='''

'''                                                                MENU USER                                                         '''

'''=================================================================================================================================='''
def menu_user(username):
    while True:
        try:
            pilihan = [
                "Tambah Pengiriman Barang",
                "Lihat Pengiriman Anda",
                "ShipPay",
                "Kembali ke Menu Utama"
            ]
            tabelpilihan("MENU USER", pilihan)
            pilih = input("Pilih menu (1/2/3/4): ").strip()
            if pilih == '1':
                clear()
                tambah_pengiriman_user(username)
                clear()
            elif pilih == '2':
                clear()
                lihat_pengiriman_anda(username)
                clear()
            elif pilih == '3':
                clear()
                login_shippay(username)
                clear()
            elif pilih == '4':
                banner("TERIMA KASIH! Kembali ke menu utama dalam 3 detik...")
                time.sleep(3)
                break
            else:
                banner("MASUKKAN ANGKA 1 SAMPAI 4!")
        except KeyboardInterrupt:
            print("\n")
            banner("MOHON TIDAK MENEKAN CTRL+C!")
            continue

menu_utama()