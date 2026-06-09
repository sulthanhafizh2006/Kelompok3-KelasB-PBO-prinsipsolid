# 📚 Sistem Manajemen Perpustakaan

Program Python berbasis **Object-Oriented Programming (OOP)** untuk mengelola data koleksi perpustakaan dengan menerapkan konsep:

* Inheritance (Pewarisan)
* Abstraction (Abstraksi)
* Polymorphism (Polimorfisme)
* SOLID Principles

---

# 👥 Anggota Kelompok dan Pembagian Tugas

| No | Nama   | Tugas                                              | File                         |
| -- | ------ | -------------------------------------------------- | ---------------------------- |
| 1  | Sulthan Hafizh Putra Agung | Membuat Abstract Class Koleksi                     | `bagian1_koleksi.py`         |
| 2  | Zahra Faizza Kuncoroningrum  | Membuat Model Koleksi (Buku, Majalah, Jurnal, DVD) | `bagian2_model_koleksi.py`   |
| 3  | ⁠Adibah Ruhil | Membuat Repository Penyimpanan Data                | `bagian3_repository.py`      |
| 4  | Aksya Nayla  | Membuat Input Handler                              | `bagian4_input_handler.py`   |
| 5  | Allicya Nailah Fairuza    | Membuat Display Manager                            | `bagian5_display_manager.py` |
| 6  | Faris Rafiuddin Hannan  | Membuat Main Program dan Integrasi Sistem          | `bagian6_main.py`            |

---

# 📂 Struktur Project

```text
perpustakaan/
│
├── bagian1_koleksi.py
├── bagian2_model_koleksi.py
├── bagian3_repository.py
├── bagian4_input_handler.py
├── bagian5_display_manager.py
└── bagian6_main.py
```

## Deskripsi File

| File                         | Deskripsi                                            |
| ---------------------------- | ---------------------------------------------------- |
| `bagian1_koleksi.py`         | Abstract class Koleksi                               |
| `bagian2_model_koleksi.py`   | Class Buku, Majalah, Jurnal, dan DVD Film Dokumenter |
| `bagian3_repository.py`      | Penyimpanan dan pengelolaan data koleksi             |
| `bagian4_input_handler.py`   | Pengambilan input dari pengguna                      |
| `bagian5_display_manager.py` | Menampilkan menu dan data koleksi                    |
| `bagian6_main.py`            | Entry point dan pengatur alur program                |

---

# ⚙️ Cara Menjalankan Program

Pastikan seluruh file berada dalam satu folder yang sama.

Jalankan program menggunakan perintah berikut:

```bash
python bagian6_main.py
```

---

# ✨ Fitur Program

### 1. Tambah Data Koleksi

Pengguna dapat menambahkan berbagai jenis koleksi:

* Buku
* Majalah
* Jurnal
* DVD Film Dokumenter

### 2. Hapus Data Koleksi

Menghapus data koleksi berdasarkan kode koleksi.

### 3. Tampilkan Semua Data Koleksi

Menampilkan seluruh data koleksi yang tersimpan dalam sistem.

### 4. Keluar Program

Mengakhiri eksekusi aplikasi.

---

# 🏛 Implementasi OOP

## 1. Abstraction (Abstraksi)

Menggunakan Abstract Base Class (ABC) berupa class `Koleksi`.

Class ini mendefinisikan atribut dan method umum yang wajib dimiliki oleh seluruh jenis koleksi.

Contoh method abstrak:

```python
@abstractmethod
def get_jenis(self):
    pass
```

---

## 2. Inheritance (Pewarisan)

Class berikut merupakan turunan dari class `Koleksi`:

* Buku
* Majalah
* Jurnal
* DVDFilmDokumenter

Diagram sederhana:

```text
Koleksi
│
├── Buku
├── Majalah
├── Jurnal
└── DVDFilmDokumenter
```

---

## 3. Polymorphism (Polimorfisme)

Setiap subclass mengimplementasikan method yang sama dengan cara yang berbeda.

Contoh:

```python
koleksi.get_info_tambahan()
```

Method tersebut akan menghasilkan output yang berbeda sesuai jenis koleksinya.

---

# 🧩 Implementasi Prinsip SOLID

## S — Single Responsibility Principle (SRP)

Setiap class memiliki satu tanggung jawab utama.

| Class             | Tanggung Jawab             |
| ----------------- | -------------------------- |
| KoleksiRepository | Mengelola penyimpanan data |
| InputHandler      | Mengelola input pengguna   |
| DisplayManager    | Mengelola tampilan         |
| Aplikasi          | Mengatur alur program      |

---

## O — Open/Closed Principle (OCP)

Sistem terbuka untuk pengembangan tetapi tertutup untuk modifikasi.

Contohnya ketika menambahkan jenis koleksi baru:

```python
class DVDFilmDokumenter(Koleksi):
    ...
```

Tidak perlu mengubah kode pada class yang sudah ada.

---

## L — Liskov Substitution Principle (LSP)

Semua subclass dapat menggantikan parent class `Koleksi`.

Contoh:

```python
koleksi = Buku(...)
koleksi = Majalah(...)
koleksi = Jurnal(...)
```

Ketiganya tetap dapat diproses sebagai objek bertipe `Koleksi`.

---

## I — Interface Segregation Principle (ISP)

Abstract class `Koleksi` hanya menyediakan method yang benar-benar diperlukan oleh subclass.

Dengan demikian subclass tidak dipaksa mengimplementasikan method yang tidak digunakan.

---

## D — Dependency Inversion Principle (DIP)

Class `Aplikasi` bergantung pada abstraksi, bukan implementasi konkret.

Dependensi diberikan melalui constructor:

```python
app = Aplikasi(
    repository,
    input_handler,
    display_manager
)
```

Hal ini membuat program lebih fleksibel dan mudah dikembangkan.

---

# 📝 Contoh Output Program

```text
====================
MENU PROGRAM
====================

1. Tambah data koleksi
2. Hapus data koleksi
3. Tampil semua data koleksi
4. Keluar

Nomor yang dipilih : 1

------------------------------------------------
JENIS KOLEKSI YANG AKAN DITAMBAH

1. Buku
2. Majalah
3. Jurnal
4. DVD Film Dokumenter

Nomor yang dipilih : 1

------------------------------------------------
TAMBAH DATA BUKU

Masukkan Kode Koleksi : B001
Masukkan Judul        : Pemrograman Python
Masukkan Tahun Terbit : 2023
Masukkan Pengarang    : Budi Santoso
Masukkan Penerbit     : Gramedia

------------------------------------------------
Tambah Buku Sukses
```

---

# 📌 Kesimpulan

Program Sistem Manajemen Perpustakaan ini berhasil menerapkan konsep utama Object-Oriented Programming (OOP), yaitu Abstraksi, Pewarisan, dan Polimorfisme, serta memenuhi kelima prinsip SOLID. Dengan struktur yang modular dan terpisah berdasarkan tanggung jawab masing-masing komponen, sistem menjadi lebih mudah dipelihara, dikembangkan, dan diuji di masa mendatang.
