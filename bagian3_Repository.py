# ============================================================
# BAGIAN 3 - repository.py
# Nama : Adibah Ruhil
# Kelas : B
# NIM : K3525044
# Penyimpanan Data (Single Responsibility + Dependency Inversion)
# ============================================================

from koleksi import Koleksi

class KoleksiRepository:
    """
    Bertanggung jawab HANYA untuk menyimpan dan mengambil data koleksi.
    (Single Responsibility Principle)
    Bergantung pada abstraksi Koleksi, bukan kelas konkret.
    (Dependency Inversion Principle)
    """

    def __init__(self):
        self._data: list[Koleksi] = []

    def tambah(self, koleksi: Koleksi):
        self._data.append(koleksi)

    def hapus(self, kode: str) -> bool:
        for item in self._data:
            if item.kode_koleksi == kode:
                self._data.remove(item)
                return True
        return False

    def get_semua(self) -> list[Koleksi]:
        return self._data
