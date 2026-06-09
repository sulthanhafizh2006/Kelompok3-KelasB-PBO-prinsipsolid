# ============================================================
# BAGIAN 2 - model_koleksi.py
# Nama  : Zahra Faizza Kuncoroningrum
# NIM   : K3525017
# Kelas : B
# Kelas Turunan (Open/Closed + Liskov Substitution)
# ============================================================

from koleksi import Koleksi


class Buku(Koleksi):
    """Koleksi jenis Buku. (Single Responsibility: hanya merepresentasikan Buku)"""

    def __init__(self, kode_koleksi, judul, tahun_terbit, pengarang, penerbit):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self.pengarang = pengarang

    def get_jenis(self) -> str:
        return "Buku"

    def get_info_tambahan(self) -> dict:
        return {"Pengarang": self.pengarang}


class Majalah(Koleksi):
    """Koleksi jenis Majalah. (Single Responsibility: hanya merepresentasikan Majalah)"""

    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, edisi):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self.edisi = edisi

    def get_jenis(self) -> str:
        return "Majalah"

    def get_info_tambahan(self) -> dict:
        return {"Edisi": self.edisi}


class Jurnal(Koleksi):
    """Koleksi jenis Jurnal. (Single Responsibility: hanya merepresentasikan Jurnal)"""

    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, bidang_studi, impact_factor):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor

    def get_jenis(self) -> str:
        return "Jurnal"

    def get_info_tambahan(self) -> dict:
        return {
            "Bidang Studi  ": self.bidang_studi,
            "Impact Factor ": self.impact_factor,
        }


class DVDFilmDokumenter(Koleksi):
    """
    Koleksi jenis DVD Film Dokumenter.
    Penerapan Open/Closed: kelas baru ditambahkan TANPA mengubah kode yang sudah ada.
    """

    def __init__(self, kode_koleksi, judul, tahun_terbit, jenis, bidang_ilmu, durasi):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit="-")
        self.jenis = jenis
        self.bidang_ilmu = bidang_ilmu
        self.durasi = durasi

    def get_jenis(self) -> str:
        return "DVD Film Dokumenter"

    def get_info_tambahan(self) -> dict:
        return {
            "Jenis         ": self.jenis,
            "Bidang Ilmu   ": self.bidang_ilmu,
            "Durasi        ": self.durasi,
        }
