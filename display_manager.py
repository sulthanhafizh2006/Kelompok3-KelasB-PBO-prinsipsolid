# ============================================================
# BAGIAN 5 - display_manager.py
# NAMA : ALLICYA NAILAH FAIRUZA
# NIM : K3525048
# KELAS : B
# Menampilkan Output ke Layar (Single Responsibility)
# ============================================================

from koleksi import Koleksi


class DisplayManager:
    """Bertanggung jawab HANYA untuk menampilkan data ke layar."""

    def tampilkan_menu_utama(self):
        print("\n" + "=" * 20)
        print("MENU PROGRAM")
        print("-" * 30)
        print("  1. Tambah data koleksi")
        print("  2. Hapus data koleksi")
        print("  3. Tampil semua data koleksi")
        print("  4. Keluar")

    def tampilkan_menu_jenis(self):
        print("\n" + "-" * 50)
        print("JENIS KOLEKSI YANG AKAN DITAMBAH")
        print()
        print("  1. Buku")
        print("  2. Majalah")
        print("  3. Jurnal")
        print("  4. DVD Film Dokumenter")

    def tampilkan_semua(self, koleksi_list: list[Koleksi]):
        print("\n" + "-" * 50)
        print("DATA KOLEKSI")
        print()
        if not koleksi_list:
            print("  (Belum ada data koleksi)")
            return
        for i, koleksi in enumerate(koleksi_list, 1):
            print(f"Koleksi {i}:")
            koleksi.tampilkan()
            print()