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

# Fitur
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
<img width="16384" height="11492" alt="PROJECT AKHIR DDP-MENU ADMIN drawio (5)" src="https://github.com/user-attachments/assets/3dfdc0cc-8c79-4d6c-b41c-ae9deb1229e3" />

### Menu User dan Menu ShipPay
<img width="16384" height="10035" alt="PROJECT AKHIR DDP-MENU USER drawio (1)" src="https://github.com/user-attachments/assets/9d777e97-24b2-4382-a554-500642a9ecda" />

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
<img width="602" height="78" alt="image" src="https://github.com/user-attachments/assets/6251a836-7709-4055-86db-09c50ce7bbcf" />

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
- Apabila pada menu utama pengguna memasukkan input "3", maka program akan berakhir
<img width="606" height="80" alt="image" src="https://github.com/user-attachments/assets/f2a0bca9-1e00-4bba-8e4a-64d795d9e402" />

## Menu Admin
- Setelah berhasil melakukan *login* sebagai admin, maka pengguna akan masuk ke menu admin dengan 5 pilihan menu dan diminta untuk memilih menu yang tersedia
<img width="274" height="216" alt="image" src="https://github.com/user-attachments/assets/72420ac5-ff6f-4db6-b945-5697413ce1d2" />

- Apabila salah memasukkan input, maka akan muncul output "Masukkan angka 1-5!" dan pengguna diminta untuk memasukkan input kembali
<img width="610" height="266" alt="image" src="https://github.com/user-attachments/assets/751bd2b8-c635-49e3-bf5b-38899ec65d22" />

### 1. Tambah Data Pengiriman
- Saat masuk ke menu "Tambah Data Pengiriman" pengguna diminta untuk input nama pengirim, nama penerima, alamat asal, dan alamat tujuan
<img width="606" height="139" alt="image" src="https://github.com/user-attachments/assets/4600f4aa-8828-43b0-a096-38420cbe8831" />

- Apabila salah satu dari 4 input tersebut ada yang dikosongkan, maka akan terulang dari awal input nama pengirim
<img width="603" height="77" alt="image" src="https://github.com/user-attachments/assets/5d0eb9a7-b625-4e0f-b384-f08ed3cc9378" />

- Selanjutnya, pengguna akan diminta untuk memilih jenis pengiriman "Antar Pulau" atau "Luar Pulau"
<img width="260" height="159" alt="image" src="https://github.com/user-attachments/assets/679d81cb-7b02-49e2-9ad1-c8a430fe9f22" />

- Setelah itu, pengguna diminta untuk memasukkan barang yang akan dikirim dan berat barang tersebut dalam satuan kg
<img width="231" height="47" alt="image" src="https://github.com/user-attachments/assets/d0e828cf-711b-4a5c-a296-4a775a13664d" />

- Apabila berat barang yang diinput < 0 kg atau > 100 kg, maka akan diulang dan menampilkan "Berat barang harus lebih dari 0 dengan maksimal 100kg!"
<img width="602" height="83" alt="image" src="https://github.com/user-attachments/assets/c7f05e58-ff9f-4c67-b331-58eeb52a8534" />

- Selanjutnya pengguna diminta untuk memilih layanan pengiriman, diataranya; "Reguler", "Express", dan "Kargo"
<img width="311" height="187" alt="image" src="https://github.com/user-attachments/assets/9a7a50f2-5b55-4f47-928c-ec4064c8dc18" />

- Pengguna akan diminta untuk input estimasi pengiriman barang dengan format *(DD/MM/YYY)*
<img width="380" height="36" alt="image" src="https://github.com/user-attachments/assets/80497f03-2e29-422d-bcef-e7db516c668a" />

- Apabila format tidak sesuai, maka pengguna diminta untuk kembali memasukkan estimasi pengiriman
<img width="609" height="79" alt="image" src="https://github.com/user-attachments/assets/04318629-482e-4ae0-8668-caa9089d1c98" />

- Setelah semua data lengkap, maka program akan menyimpan data pengiriman ke dalam JSON dan menampilkan ringkasan data pengiriman baru
<img width="615" height="370" alt="image" src="https://github.com/user-attachments/assets/f3b41ae9-511c-48fb-9d57-c793ea57bd2b" />

### 2. Lihat data pengiriman
- Pada menu ini pengguna diminta untuk memilih jenis pengiriman yang ingin dilihat datanya
<img width="238" height="167" alt="image" src="https://github.com/user-attachments/assets/e75be22c-521d-4222-a254-02876e94b43f" />

- Apabila pengguna salah memasukkan input, akan muncul "Masukkan angka 1 atau 2!" dan pengguna dapat memilih kembali jenis pengiriman yang ingin dilihat
<img width="624" height="217" alt="image" src="https://github.com/user-attachments/assets/88d163fe-6cf8-4145-9194-e36b0e26672c" />

- Setelah memilih jenis pengiriman, program akan menampilkan data pengiriman berdasarkan jenis pengiriman yang dipilih
<img width="1114" height="217" alt="image" src="https://github.com/user-attachments/assets/afe028d0-5590-4dad-9b79-a71139ee4a3a" />

### 3. Ubah data pengiriman
- Pada menu ini pengguna diminta untuk memilih jenis pengiriman yang ingin dilihat datanya
<img width="238" height="167" alt="image" src="https://github.com/user-attachments/assets/e75be22c-521d-4222-a254-02876e94b43f" />

- Apabila pengguna salah memasukkan input, akan muncul "Masukkan angka 1 atau 2!" dan pengguna dapat memilih kembali jenis pengiriman yang ingin diubah
<img width="624" height="217" alt="image" src="https://github.com/user-attachments/assets/88d163fe-6cf8-4145-9194-e36b0e26672c" />

- Setelah memilih jenis pengiriman, program akan menampilkan data pengiriman berdasarkan jenis pengiriman yang dipilih
<img width="1114" height="217" alt="image" src="https://github.com/user-attachments/assets/afe028d0-5590-4dad-9b79-a71139ee4a3a" />

- Pengguna kemudian memasukkan ID pengiriman yang ingin diubah
<img width="1119" height="237" alt="image" src="https://github.com/user-attachments/assets/07672e82-7b74-4e84-b41a-8bdf287e8416" />

- Apabila ID yang diinput tidak sesuai, maka program menampilkan "ID Pengiriman tidak ditemukan" dan pengguna kembali ke menu utama
<img width="623" height="83" alt="image" src="https://github.com/user-attachments/assets/9f53e902-212a-42f3-af55-d7b162907c1c" />

- Apabila ID ditemukan, maka pengguna diminta untuk memilih jenis perubahan
<img width="307" height="182" alt="image" src="https://github.com/user-attachments/assets/117cd6b1-a894-4c14-9a04-0bbbd39966fe" />

- Pada pilihan "1", pengguna dapat mengubah detail pengiriman seperti nama pengirim, nama penerima, alamat asal, dan alamat tujuan. Apabila terdapat detail yang tidak perlu diubah, maka pengguna dapat mengosongkan bagian tersebut
<img width="640" height="139" alt="image" src="https://github.com/user-attachments/assets/03220362-3b1b-4e8b-b043-0830cbb1d38c" />

<img width="619" height="82" alt="image" src="https://github.com/user-attachments/assets/33e97f13-4bd0-4809-88d9-08fccb3ba3b4" />

- Pada pilihan "2", pengguna dapat mengubah status pengiriman barang
<img width="271" height="189" alt="image" src="https://github.com/user-attachments/assets/a8d002bc-d6c4-4a1e-a1f9-9114ac567a21" />

<img width="271" height="189" alt="image" src="https://github.com/user-attachments/assets/e24ce785-d33c-40c4-94d8-05024348d8bd" />

- Pada pilihan "3", pengguna dapat mengubah dan mengatur estimasi pengiriman barang
<img width="613" height="87" alt="image" src="https://github.com/user-attachments/assets/12775003-399d-48c0-a3b1-2aabbc7fd2ba" />

<img width="635" height="86" alt="image" src="https://github.com/user-attachments/assets/7b308ce2-28ef-4e82-9508-63ea33871705" />

### 4. Hapus data pengiriman
- Pada menu ini pengguna diminta untuk memilih jenis pengiriman yang ingin dilihat datanya
<img width="238" height="167" alt="image" src="https://github.com/user-attachments/assets/e75be22c-521d-4222-a254-02876e94b43f" />

- Apabila pengguna salah memasukkan input, akan muncul "Masukkan angka 1 atau 2!" dan pengguna dapat memilih kembali jenis pengiriman yang ingin dihapus
<img width="624" height="217" alt="image" src="https://github.com/user-attachments/assets/88d163fe-6cf8-4145-9194-e36b0e26672c" />

- Setelah memilih jenis pengiriman, program akan menampilkan data pengiriman berdasarkan jenis pengiriman yang dipilih
<img width="1114" height="217" alt="image" src="https://github.com/user-attachments/assets/afe028d0-5590-4dad-9b79-a71139ee4a3a" />

- Pengguna kemudian memasukkan ID pengiriman yang ingin dihapus
<img width="1069" height="204" alt="image" src="https://github.com/user-attachments/assets/9bd56170-6f12-4e02-8414-e46b47409cfc" />

- Apabila ID yang diinput tidak sesuai, maka program menampilkan "ID Pengiriman tidak ditemukan" dan pengguna kembali ke menu utama
<img width="660" height="86" alt="image" src="https://github.com/user-attachments/assets/ac3f2872-4c85-4c65-a361-95f5f941d895" />

- Apabila ID pengiriman ditemukan, maka program akan menghapus data pengiriman tersebut
<img width="622" height="80" alt="image" src="https://github.com/user-attachments/assets/5f127363-8153-4d4b-b930-c0055b3cfec6" />

### 5. Kembali ke menu utama
- Apabila memilih "5" pada menu admin, maka program akan kembali ke menu utama dengan *delay* 3 detik
<img width="634" height="66" alt="image" src="https://github.com/user-attachments/assets/0527103a-f95a-4675-b86f-98bf01f70a8e" />

## Menu User

### 1. Tambah pengiriman barang
- Saat masuk ke menu "Tambah Pengiriman Barang" pengguna diminta untuk input nama pengirim, nama penerima, alamat asal, dan alamat tujuan
<img width="606" height="139" alt="image" src="https://github.com/user-attachments/assets/4600f4aa-8828-43b0-a096-38420cbe8831" />

- Apabila salah satu dari 4 input tersebut ada yang dikosongkan, maka akan terulang dari awal input nama pengirim
<img width="603" height="77" alt="image" src="https://github.com/user-attachments/assets/5d0eb9a7-b625-4e0f-b384-f08ed3cc9378" />

- Selanjutnya, pengguna akan diminta untuk memilih jenis pengiriman "Antar Pulau" atau "Luar Pulau"
<img width="260" height="159" alt="image" src="https://github.com/user-attachments/assets/679d81cb-7b02-49e2-9ad1-c8a430fe9f22" />

- Setelah itu, pengguna diminta untuk memasukkan barang yang akan dikirim dan berat barang tersebut dalam satuan kg
<img width="231" height="47" alt="image" src="https://github.com/user-attachments/assets/d0e828cf-711b-4a5c-a296-4a775a13664d" />

- Apabila berat barang yang diinput < 0 kg atau > 100 kg, maka akan diulang dan menampilkan "Berat barang harus lebih dari 0 dengan maksimal 100kg!"
<img width="602" height="83" alt="image" src="https://github.com/user-attachments/assets/c7f05e58-ff9f-4c67-b331-58eeb52a8534" />

- Selanjutnya pengguna diminta untuk memilih layanan pengiriman, diataranya; "Reguler", "Express", dan "Kargo"
<img width="311" height="187" alt="image" src="https://github.com/user-attachments/assets/9a7a50f2-5b55-4f47-928c-ec4064c8dc18" />

- Program akan menampilkan ringkasan data pengiriman beserta total ongkir dan saldo. Selain itu, pengguna diminta untuk konfirmasi pembayaran
<img width="634" height="373" alt="image" src="https://github.com/user-attachments/assets/a6dd9bf9-80f7-46c1-a1f7-87414b6877b3" />

- Apabila akun user merupakan akun **GOLD**, maka pengguna mendapatkan diskon ongkir sebesar 10%
<img width="643" height="173" alt="image" src="https://github.com/user-attachments/assets/66cef1f6-c787-43b0-b725-dd370f3e9e62" />

- Apabila user memilih "Ya" saat konfirmasi pembayaran dan saldo mencukupi, transaksi pembayaran akan diproses
<img width="639" height="153" alt="image" src="https://github.com/user-attachments/assets/443e6702-a0af-417f-b06a-b79d55eb7877" />

- Saat proses transaksi selesai, program akan menampilkan *Invoice* dan saldo user akan terpotong, serta mendapatkan 250 poin
<img width="654" height="451" alt="image" src="https://github.com/user-attachments/assets/2f6f3b4b-d6b4-49b2-9656-62e9d6869a3a" />

- Jika saldo tidak mencukupi, maka akan pengguna akan kembali ke menu utama
<img width="649" height="89" alt="image" src="https://github.com/user-attachments/assets/30ba0cde-54ff-47f1-989b-f726440a25ce" />

- Apabila user memilih "Tidak" saat konfirmasi pembayaran, maka pesanan dibatalkan dan kembali ke menu utama
<img width="643" height="108" alt="image" src="https://github.com/user-attachments/assets/d0eeba37-9e94-4b45-a647-319cf38e9f89" />

### 2. Lihat pengiriman barang anda
- Pada menu ini, program akan menampilkan daftar pengiriman user
<img width="650" height="524" alt="image" src="https://github.com/user-attachments/assets/7360044b-d48c-46e8-986a-61f0a6ddeeca" />

- Apabila tidak ditemukan pengiriman barang, maka program menampilkan bahwa user belum memiliki data pengiriman
<img width="632" height="77" alt="image" src="https://github.com/user-attachments/assets/0d64732b-09cd-403d-b132-aacd28b6ba16" />

### 3. ShipPay
- Sebelum masuk ke menu ShipPay, pengguna diminta untuk memasukkan password akun
<img width="621" height="90" alt="image" src="https://github.com/user-attachments/assets/f5f4a1b2-fb07-4c5a-bdd2-1df2b8df23f0" />

- Pengguna diberikan 3 kesempatan untuk memasukkan password yang benar. Apabila salah, maka kesempatan diulang dan program akan menampilkan "UPassword
  salah!" serta jumlah kesempatan yang tersisa
<img width="610" height="83" alt="image" src="https://github.com/user-attachments/assets/219138c6-6523-4734-836c-41fb21fe8051" />

- Apabila kesempatan habis, pengguna akan kembali ke menu user dengan *delay* 5 detik
<img width="607" height="57" alt="image" src="https://github.com/user-attachments/assets/1723e3cd-c96f-4188-ad21-811c4858684a" />

- Apabila pengguna memasukkan password yang benar, maka user bisa masuk ke menu ShipPay
<img width="601" height="86" alt="image" src="https://github.com/user-attachments/assets/1c8d2e73-6781-4d51-9ab8-86424d54ea13" />

## Menu ShipPay
- Pada menu ini, program menampilkan akun user, jenis akun, serta banyaknya poin yang telah dikumpulkan. Selain itu, menu ini juga menyediakan 4 pilihan menu, yakni:
<img width="610" height="257" alt="image" src="https://github.com/user-attachments/assets/45fbc593-6872-4b81-a524-74921a67e22e" />

### 1. Lihat saldo
- Apabila pengguba memilih menu "1" maka program akan menampilkan saldo ShipPay saat ini
<img width="617" height="84" alt="image" src="https://github.com/user-attachments/assets/72c07f27-6047-48f1-96fc-4abec91a616e" />

### 2. Top-up saldo
- Apabila pengguna memilih menu "2", program akan menampilkan saldo ShipPay saat ini dan user diminta untuk memasukkan nominal Top-Up
<img width="600" height="90" alt="image" src="https://github.com/user-attachments/assets/d89845bc-1c70-468d-9bc9-9bff28495308" />

- Nominal tersebut tidak boleh kurang dari Rp10.000 atau lebih dari Rp200.000
<img width="620" height="93" alt="image" src="https://github.com/user-attachments/assets/74788fb0-c4d8-433c-888d-ebd149204eda" />

<img width="620" height="87" alt="image" src="https://github.com/user-attachments/assets/d98a937e-44ef-450b-bc45-d0f9787ac433" />

- Setelah memasukkan nominal Top Up yang sesuai, maka saldo pengguna akan ditambah dan program menampilkan saldo user saat ini
<img width="617" height="81" alt="image" src="https://github.com/user-attachments/assets/f4f297d3-c6d8-4370-b97a-88473f269fbd" />

### 3. Upgrade ke akun GOLD
- Pada menu ini, program akan menampilkan jumlah poin yang dimiliki pengguna dan melakukan konfirmasi apakah ingin upgrade ke akun gold atau tidak
<img width="599" height="84" alt="image" src="https://github.com/user-attachments/assets/11563383-f486-41ac-81a8-3f705f83fbf3" />

- Jika memilih "Tidak", maka upgrade akun akan dibatalkan
<img width="605" height="80" alt="image" src="https://github.com/user-attachments/assets/a6e7a047-1e49-4702-a044-6e5eaf3f807d" />

- Jika "Ya" dan pengguna memiliki poin lebih dari sama dengan 1000, maka akun user akan diupgrade ke akun GOLD
<img width="604" height="78" alt="image" src="https://github.com/user-attachments/assets/132a217e-655a-401f-b7fe-983256887860" />

- Namun jika poin pennguna kurang dari 1000, maka upgrade akun gagal karena poin yang tidak mencukupi
<img width="626" height="87" alt="image" src="https://github.com/user-attachments/assets/69b0bcf3-d99c-45a0-ac4c-702c0f27e989" />

- Jika akun sudah merupakan akun gold, maka akan muncul pemberitahuan bahwa "akun anda sudah gold"
<img width="609" height="79" alt="image" src="https://github.com/user-attachments/assets/04827c1b-2d02-48a7-833a-397d7ba7eda6" />

### 4. Kembali ke menu user
- Apabila pengguna memilih menu "4", maka program akan keluar dari ShipPay dan kembali ke menu user dengan *delay* 3 detik
<img width="609" height="64" alt="image" src="https://github.com/user-attachments/assets/4958e4c4-45d8-4fcb-9501-063c237986ae" />

## 4. Kembali ke Menu Utama
- Menu ini merupakan terakhir dalam menu user yang fungsinya agar pengguna kembali ke menu utama dengan *delay* 5 detik
![Uploading image.png…]()


