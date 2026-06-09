# ============================================================
# BAGIAN 6 - main.py
# NAMA : FARIS RAFIUDDIN HANNAN
# NIM : K3525058
# KELAS : B
# Aplikasi Utama & Entry Point (Dependency Inversion)
# ============================================================

from repository import KoleksiRepository
from input_handler import InputHandler
from display_manager import DisplayManager


class Aplikasi:
    """
    Mengatur alur program secara keseluruhan.
    Bergantung pada abstraksi, bukan implementasi konkret.
    (Dependency Inversion Principle)
    """

    def __init__(self,
                 repository: KoleksiRepository,
                 input_handler: InputHandler,
                 display: DisplayManager):
        self.repo = repository
        self.input_handler = input_handler
        self.display = display

    def menu_tambah(self):
        self.display.tampilkan_menu_jenis()
        pilih = input("\nNomor yang dipilih: ")

        if pilih == "1":
            koleksi = self.input_handler.input_buku()
            pesan = "Tambah Buku Sukses"
        elif pilih == "2":
            koleksi = self.input_handler.input_majalah()
            pesan = "Tambah Majalah Sukses"
        elif pilih == "3":
            koleksi = self.input_handler.input_jurnal()
            pesan = "Tambah Jurnal Sukses"
        elif pilih == "4":
            koleksi = self.input_handler.input_dvd()
            pesan = "Tambah DVD Film Dokumenter Sukses"
        else:
            print("Pilihan tidak valid.")
            return

        self.repo.tambah(koleksi)
        print("-" * 50)
        print(pesan)

    def menu_hapus(self):
        print("\n" + "-" * 30)
        print("HAPUS DATA KOLEKSI")
        print()
        kode = input("Masukkan Kode Koleksi  : ")
        print("-" * 50)
        if self.repo.hapus(kode):
            print("Hapus data koleksi sukses")
        else:
            print(f"Koleksi dengan kode '{kode}' tidak ditemukan.")

    def jalankan(self):
        while True:
            self.display.tampilkan_menu_utama()
            pilih = input("\nNomor yang dipilih: ")

            if pilih == "1":
                self.menu_tambah()
            elif pilih == "2":
                self.menu_hapus()
            elif pilih == "3":
                self.display.tampilkan_semua(self.repo.get_semua())
            elif pilih == "4":
                print("\nTerima kasih. Program selesai.")
                break
            else:
                print("Pilihan tidak valid, coba lagi.")

            input("\nTekan [ENTER] untuk kembali ke menu program")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    repo    = KoleksiRepository()
    handler = InputHandler()
    display = DisplayManager()

    app = Aplikasi(repo, handler, display)
    app.jalankan()
