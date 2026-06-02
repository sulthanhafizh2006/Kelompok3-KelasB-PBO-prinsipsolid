# ============================================================
# BAGIAN 4 - input_handler.py
# Membaca Input dari User (Single Responsibility)
# ============================================================

from model_koleksi import Buku, Majalah, Jurnal, DVDFilmDokumenter


class InputHandler:
    """Bertanggung jawab HANYA untuk membaca input koleksi dari user."""

    def input_buku(self) -> Buku:
        print("-" * 50)
        print("TAMBAH DATA BUKU")
        print()
        kode      = input("Masukkan Kode Koleksi  : ")
        judul     = input("Masukkan Judul         : ")
        tahun     = input("Masukkan Tahun Terbit  : ")
        pengarang = input("Masukkan Pengarang     : ")
        penerbit  = input("Masukkan Penerbit      : ")
        return Buku(kode, judul, tahun, pengarang, penerbit)

    def input_majalah(self) -> Majalah:
        print("-" * 50)
        print("TAMBAH DATA MAJALAH")
        print()
        kode     = input("Masukkan Kode Koleksi  : ")
        judul    = input("Masukkan Judul         : ")
        tahun    = input("Masukkan Tahun Terbit  : ")
        penerbit = input("Masukkan Penerbit      : ")
        edisi    = input("Masukkan Edisi         : ")
        return Majalah(kode, judul, tahun, penerbit, edisi)

    def input_jurnal(self) -> Jurnal:
        print("-" * 50)
        print("TAMBAH DATA JURNAL")
        print()
        kode     = input("Masukkan Kode Koleksi  : ")
        judul    = input("Masukkan Judul         : ")
        tahun    = input("Masukkan Tahun Terbit  : ")
        penerbit = input("Masukkan Penerbit      : ")
        bidang   = input("Masukkan Bidang Studi  : ")
        impact   = input("Masukkan Impact Factor : ")
        return Jurnal(kode, judul, tahun, penerbit, bidang, impact)

    def input_dvd(self) -> DVDFilmDokumenter:
        print("-" * 50)
        print("TAMBAH DATA DVD FILM DOKUMENTER")
        print()
        kode   = input("Masukkan Kode Koleksi  : ")
        judul  = input("Masukkan Judul         : ")
        tahun  = input("Masukkan Tahun         : ")
        jenis  = input("Masukkan Jenis         : ")
        bidang = input("Masukkan Bidang Ilmu   : ")
        durasi = input("Masukkan Durasi        : ")
        return DVDFilmDokumenter(kode, judul, tahun, jenis, bidang, durasi)
