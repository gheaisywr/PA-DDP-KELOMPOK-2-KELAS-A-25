# PA DDP KELOMPOK 2 KELAS A'2025
# Project Akhir DDP: Sistem Pengiriman Barang Antar Pulau & Luar Pulau 
Disusun oleh:
> 1. Alya Hauranisa Nugroho NIM (2509116005)
> 2. Alif Anugrah Ramadhan NIM (2509116019)
> 3. Ghea Aisyah Windraswari NIM (2509116022)

Praktikum : **Dasar Dasar Pemrograman**  

---

# Deskripsi Program
Program ini merupakan program Python sederhana bertemakan "Sistem Pengiriman Barang Antar Pulau & Luar Pulau" yang dimanfaatkan pengguna (admin dan user)  untuk mengelola pengiriman barang dengan menu dan fitur-fitur yang disesuaikan dengan haknya.

### Menu utama, meliputi:
1. Login untuk Admin
2. Login untuk User
3. Keluar

### Menu admin, meliputi:
1. Tambah data pengiriman
2. Lihat data pengiriman
3. Ubah data pengiriman
4. Hapus data pengiriman
5. Kembali ke menu utama

### Menu user, meliputi:
1. Tambah pengiriman barang
2. Lihat pengiriman barang anda
3. ShipPay
4. Kembali ke menu utama

### Pada menu user, terdapat ShipPay yang merupakan saldo atau E-Money pada program ini. Menu ShipPay, meliputi:
1. Lihat saldo
2. Top-up saldo
3. Upgrade ke akun GOLD
4. Kembali ke menu user

---

# Konsep yang Digunakan
1. **Fungsi (`def`)** untuk membuat kode lebih terstruktur.  
2. **Perulangan (`for`)** untuk menelusuri elemen dalam list.  
3. **Percabangan (`if-else`)** untuk menentukan kondisi data ditemukan atau tidak.  
4. **Input dan Output** untuk interaksi dengan pengguna.
5. **Struktur Data (`List-Dictionary`)**
6. **JSON Read & Write**
7. **Error Handling (`Try-Except`)**
8. **Library (`os-json-pwinput-time-sys-prettytable`)**
9. **Logika Bisnis (`Sistem Saldo-Poin-Ongkir-Akun GOLD`)**
10. **Manajemen User (`Login-Registrasi-Validasi`)**
11. **Variabel**

---

# Flowchart
### Menu Utama
<img width="8720" height="6810" alt="PROJECT AKHIR DDP-MENU UTAMA drawio (2)" src="https://github.com/user-attachments/assets/d1a566a4-5780-4949-89c4-e1a68672d15b" />

### Login Admin
<img width="7230" height="6840" alt="PROJECT AKHIR DDP-LOGIN drawio (1)" src="https://github.com/user-attachments/assets/d930bcf5-1214-48e0-85aa-aa579dfd4802" />

### Login dan Registrasi User
<img width="11339" height="16384" alt="PROJECT AKHIR DDP-LOGIN drawio (2)" src="https://github.com/user-attachments/assets/eaa3c996-ad31-45d6-bdba-dbc944a2e290" />

### Menu Admin
<img width="16384" height="11492" alt="PROJECT AKHIR DDP-MENU ADMIN drawio (4)" src="https://github.com/user-attachments/assets/f5f731f4-ae5a-42d7-b4a5-311aa6b0fabf" />

### Menu User dan Menu ShipPay
<img width="16384" height="10038" alt="PROJECT AKHIR DDP-MENU USER drawio" src="https://github.com/user-attachments/assets/b1c960d5-61bf-4523-ab64-1f7f6fe951b3" />

---

# Alur dan Outut Program
## Menu Utama
- Saat program pertama kali di *run*, program akan menampilkan menu utama dengan 3 pilihan menu
<img width="611" height="294" alt="image" src="https://github.com/user-attachments/assets/587a2a05-afb0-4860-a8a4-92c80ae2df03" />

- Apabila salah memasukkan input, maka akan muncul output "Masukkan angka 1-3!" dan pengguna diminta untuk memasukkan input kembali
<img width="618" height="342" alt="image" src="https://github.com/user-attachments/assets/fe578065-1d2c-41f0-bf34-bb6e8612cf9f" />

### 1. Login sebagai Admin
#### Akun Admin
``` ruby
akunadmin = [
    {"username": "alya",   "password": "admin123"},
    {"username": "alip", "password": "admin456"},
    {"username": "ghea", "password": "admin789"}
]
```

- Apabila memilih "1" pada menu utama, maka pengguna akan masuk ke panel login admin dan diminta untuk memasukkan username serta password admin
<img width="633" height="107" alt="image" src="https://github.com/user-attachments/assets/c71ec3c0-0977-4c66-99f1-aba64d591862" />

- Pengguna diberikan 3 kesempatan untuk memasukkan password dan username yang benar. Apabila salah, maka kesempatan diulang dan program akan menampilkan "Username atau Password
  salah!" serta jumlah kesempatan yang tersisa
<img width="624" height="83" alt="image" src="https://github.com/user-attachments/assets/7a64475c-0a4b-4f9a-9210-8cdd01a142ac" />

- Apabila kesempatan habis, pengguna akan kembali ke menu utama dengan *delay* 5 detik
<img width="618" height="68" alt="image" src="https://github.com/user-attachments/assets/a9e3cb98-9c2f-43e8-9208-aa9f23388184" />

- Apabila pengguna berhasil memasukkan username atau password yang tepat, maka program akan menyimpan role sebagai "admin" dan pengguna akan masuk ke menu admin
<img width="604" height="81" alt="image" src="https://github.com/user-attachments/assets/cfaef823-abac-42f3-ad8d-e60a5d9bc3f4" />


### 2. Login  sebagai User
- Pada panel login sebagai user, program akan menampilkan tabel "Sudah Punya Akun?" dan pengguna dihadapkan dengan 2 pilihan, yaitu: "1. Ya, saya sudah punya akun" dan "2. Belum, saya ingin daftar akun".
<img width="295" height="167" alt="image" src="https://github.com/user-attachments/assets/c5bdd23f-e4b1-4f03-b877-73d71c2f7a89" />

- Apabila salah memasukkan input, maka akan muncul output "Pilihan tidak valid! Silahkan pilih 1 atau 2." dan pengguna diminta untuk memasukkan input kembali
<img width="624" height="220" alt="image" src="https://github.com/user-attachments/assets/b757095c-816a-4667-af4d-e522cdd6c190" />

- Jika memilih "1" maka pengguna langsung masuk ke panel login user dan diminta untuk memasukkan username dan password
<img width="607" height="100" alt="image" src="https://github.com/user-attachments/assets/35f892c0-8925-419d-bf7a-53ea9333c0ab" />

- Pengguna diberikan 3 kesempatan untuk memasukkan password dan username yang benar. Apabila salah, maka kesempatan diulang dan program akan menampilkan "Username atau Password salah!" serta jumlah kesempatan yang tersisa
<img width="604" height="79" alt="image" src="https://github.com/user-attachments/assets/6460f5af-419a-4d65-afd3-206479d843b8" />

- Apabila kesempatan habis, pengguna akan kembali ke menu utama dengan *delay* 5 detik
<img width="605" height="62" alt="image" src="https://github.com/user-attachments/assets/12b51812-a88e-4f8a-91d2-653582c8f4ec" />

- Apabila pengguna berhasil memasukkan username atau password yang tepat, maka program akan menyimpan role sebagai "user" dan pengguna akan masuk ke menu user

- Jika memilih "2" maka user akan melakukan registrasi akun dengan membuat username dan password, serta melakukan verifikasi password
<img width="606" height="118" alt="image" src="https://github.com/user-attachments/assets/2228a3c5-bc41-4b55-8ca1-e7e4463c3d90" />

- Pada saat membuat username dan password, pengguna tidak dapat memasukkan username yang sudah ada. Selain itu, username tidak bisa kurang dari 3 dan lebih dari 10, serta password tidak bisa kurang dari 6 dan lebih dari 12. Apabila tidak memenuhi kondisi, registrasi akun akan diulang dari awal
<img width="606" height="87" alt="image" src="https://github.com/user-attachments/assets/b5079af5-3a5d-4f7c-bebd-8fe7bf659793" />

<img width="603" height="85" alt="image" src="https://github.com/user-attachments/assets/1f39bd9f-335d-4020-ad3c-a2dd020563e0" />

<img width="609" height="75" alt="image" src="https://github.com/user-attachments/assets/1582afb2-2be8-47d5-9923-32ea3047210f" />

- Apabila verifikasi password tidak sesuai dengan password yang dibuat, maka pengguna akan mengulang proses registrasi akun dari awal
<img width="605" height="88" alt="image" src="https://github.com/user-attachments/assets/585d96df-b38c-4cce-8554-b0e943341ce3" />

- Apabila password berhasil dibuat, maka akun user akan tersimpan ke dalam JSON dan pengguna kembali ke menu utama
<img width="613" height="66" alt="image" src="https://github.com/user-attachments/assets/67fad740-1a4d-40df-952b-51a8efe2fe2d" />


### 3. Keluar

## Menu Admin

### 1. Tambah Data Pengiriman

### 2. Lihat data pengiriman

### 3. Ubah data pengiriman

### 4. Hapus data pengiriman

### 5. Kembali ke menu utama

## Menu User

### 1. Tambah pengiriman barang

### 2. Lihat pengiriman barang anda

### 3. ShipPay

### 4. Kembali ke menu utama

## Menu ShipPay

