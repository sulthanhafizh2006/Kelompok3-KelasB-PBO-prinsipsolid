# ============================================================
# BAGIAN 1 - koleksi.py
# NAMA : Sulthan Hafizh Putra Agung
# NIM : K3525013
# KELAS : B
# Abstraksi / Interface (Interface Segregation + Dependency Inversion)
# ============================================================

from abc import ABC, abstractmethod

class Koleksi(ABC):
    """Abstract base class untuk semua jenis koleksi perpustakaan."""

    def __init__(self, kode_koleksi: str, judul: str, tahun_terbit: str, penerbit: str):
        self.kode_koleksi = kode_koleksi
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit

    @abstractmethod
    def get_jenis(self) -> str:
        """Mengembalikan jenis koleksi."""
        pass

    @abstractmethod
    def get_info_tambahan(self) -> dict:
        """Mengembalikan atribut tambahan spesifik koleksi."""
        pass

    def tampilkan(self):
        """Polimorfisme: tampilkan data koleksi (Liskov Substitution)."""
        print(f"  Jenis         : {self.get_jenis()}")
        print(f"  Kode Koleksi  : {self.kode_koleksi}")
        print(f"  Judul         : {self.judul}")
        print(f"  Thn Terbit    : {self.tahun_terbit}")
        print(f"  Penerbit      : {self.penerbit}")
        for key, val in self.get_info_tambahan().items():
            print(f"  {key:<14}: {val}")
