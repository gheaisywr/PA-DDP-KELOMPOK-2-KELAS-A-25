# PA-DDP-
Kelompok 2
# 🐍 Tugas 3: Searching Data di Python
> Disusun oleh: **[Nama Kamu]**  
> NIM: **[NIM Kamu]**  
> Mata Kuliah: **Pemrograman Dasar Python**  
> Dosen Pengampu: **[Nama Dosen]**

---

## 📌 Deskripsi Program
Program ini dibuat untuk **mencari data dalam sebuah list menggunakan metode Linear Search**.  
Pengguna dapat memasukkan angka yang ingin dicari, dan program akan menampilkan posisi (indeks) angka tersebut jika ditemukan.

---

## 🧠 Konsep yang Digunakan
1. **Fungsi (`def`)** untuk membuat kode lebih terstruktur.  
2. **Perulangan (`for`)** untuk menelusuri elemen dalam list.  
3. **Percabangan (`if-else`)** untuk menentukan kondisi data ditemukan atau tidak.  
4. **Input dan Output** untuk interaksi dengan pengguna.  

---

## 💻 Kode Program

```python
# file: src/main.py

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

angka = [10, 25, 30, 45, 50]
cari = int(input("Masukkan angka yang ingin dicari: "))

hasil = linear_search(angka, cari)

if hasil != -1:
    print(f"Angka {cari} ditemukan di indeks {hasil}")
else:
    print(f"Angka {cari} tidak ditemukan")
