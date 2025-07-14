def main_dashboard():
    while True:
        print("\nWELCOME TO DASHBOARD!!")
        print("-"*20)
        print("1. Layanan")
        print("2. Kendaraan")
        print("3. Pemesanan")
        print("4. Pembayaran")
        print("0. Keluar\n")

        pilihan = input("Masukkan pilihan (Masukan Nomor): ").strip()

        if pilihan == "1":
            halaman_layanan()
        elif pilihan == "2":
            halaman_kendaraan()  
        elif pilihan == "3":
            halaman_pemesanan() 
        elif pilihan == "4":
            halaman_pembayaran()  
        elif pilihan == "0":
            print("Terimakash telah datang di PermenGagangWash, Sampai jumpa kembali")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def halaman_layanan():
    while True:
        print("\nHalaman Layanan")
        print("-"*20)
        print("1. Lihat Daftar Layanan")
        print("2. Pilih Layanan untuk Pemesanan")
        print("3. Lihat Detail Layanan")
        print("4. Lihat Riwayat Layanan yang Dipesan")
        print("5. Lihat Testimoni")
        print("6. Tambah Testimoni")
        print("0. Kembali ke Menu Utama\n")

        pilihan = input("Masukan Pilihan (Masukan Nomor): ").strip()

        if pilihan == "1":
            from project.UAS.layanan import lihat_layanan
            lihat_layanan()
        elif pilihan == "2":
            from project.UAS.layanan import pilih_layanan_pemesanan
            pilih_layanan_pemesanan()
        elif pilihan == "3":
            from project.UAS.layanan import lihat_detail_layanan
            lihat_detail_layanan()
        elif pilihan == "4":
            from project.UAS.layanan import lihat_riwayat_layanan
            lihat_riwayat_layanan()
        elif pilihan == "5":
            from project.UAS.layanan import lihat_testimoni
            lihat_testimoni()
        elif pilihan == "6":
            from project.UAS.layanan import tambah_testimoni
            tambah_testimoni()
        elif pilihan == "0":
            print("Kembali ke Menu Utama...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def halaman_kendaraan():
    while True:
        print("Halaman Kendaraan")
        print("-"*15)
        print("1. Lihat Daftar Kendaraan")
        print("2. Tambah Kendaraan")
        print("3. Lihat Detail Kendaraan")
        print("4. Hapus Kendaraan")
        print("0. Kembali ke Menu Utama\n")

        pilihan = input("Masukan Pilihan (Masukan Nomor): ").strip()

        if pilihan == "1":
            from project.UAS.kendaraan import lihat_kendaraan
            lihat_kendaraan()
        elif pilihan == "2":
            from project.UAS.kendaraan import tambah_kendaraan
            tambah_kendaraan()
        elif pilihan == "3":
            from project.UAS.kendaraan import lihat_detail_kendaraan
            lihat_detail_kendaraan()
        elif pilihan == "4":
            from project.UAS.kendaraan import hapus_kendaraan
            hapus_kendaraan()
        elif pilihan == "0":
            print("Kembali ke Menu Utama...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def halaman_pemesanan():
    while True:
        print("Halaman Pemesanan")
        print("-"*15)
        print("1. Lihat Daftar Pemesanan")
        print("2. Membuat Pemesanan Baru")
        print("3. Melihat Detail Pemesanan")
        print("4. Mengedit/Membatalkan Pemesanan")
        print("5. Lihat Riwayat Pemesanan")
        print("0. Kembali ke Menu Utama\n")

        pilihan = input("Masukan Pilihan (Masukkan Nomor): ").strip()

        if pilihan == "1":
            from project.UAS.pemesanan import lihat_daftar_pemesanan
            lihat_daftar_pemesanan()
        elif pilihan == "2":
            from project.UAS.pemesanan import membuat_pemesanan
            membuat_pemesanan()
        elif pilihan == "3":
            from project.UAS.pemesanan import melihat_detail_pemesanan
            melihat_detail_pemesanan()
        elif pilihan == "4":
            from project.UAS.pemesanan import mengedit_pemesanan
            mengedit_pemesanan()
        elif pilihan == "5":
            from project.UAS.pemesanan import lihat_riwayat_pemesanan
            lihat_riwayat_pemesanan()
        elif pilihan == "0":
            print("Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")



def halaman_pembayaran():
    while True:
        print("Halaman Pembayaran  ")
        print("-"*15)
        print("1. Lihat Daftar Pembayaran")
        print("2. Melakukan Pembayaran")
        print("3. Memilih Metode Pembayaran")
        print("4. Lihat Riwayat Pembayaran")
        print("5. Konfirmasi Pembayaran")
        print("0. Kembali ke Menu Utama\n")

        pilihan = input("Masukan Pilihan(masukkan nomor): ").strip()

        if pilihan == "1":
            from project.UAS.pembayaran import lihat_daftar_pembayaran
            lihat_daftar_pembayaran()
        elif pilihan == "2":
            from project.UAS.pembayaran import melakukan_pembayaran
            melakukan_pembayaran()
        elif pilihan == "3":
            from project.UAS.pembayaran import memilih_metode_pembayaran
            metode = memilih_metode_pembayaran()
            if metode:
                print(f"Metode Pembayaran yang dipilih: {metode}")
        elif pilihan == "4":
            from project.UAS.pembayaran import lihat_riwayat_pembayaran
            lihat_riwayat_pembayaran()
        elif pilihan == "5":
            from project.UAS.pembayaran import konfirmasi_pembayaran
            konfirmasi_pembayaran()
        elif pilihan == "0":
            print("Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def pembayaran():
    while True:
        print("Halaman Pembayaran")
        print("-"*20)
        print("1. Lihat Daftar Pembayaran")
        print("2. Melakukan Pembayaran")
        print("3. Memilih Metode Pembayaran")
        print("4. Lihat Riwayat Pembayaran")
        print("5. Konfirmasi Pembayaran")
        print("0. Kembali ke Menu Utama")

        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            from project.UAS.pembayaran import lihat_daftar_pembayaran
            lihat_daftar_pembayaran()
        elif pilihan == "2":
            from project.UAS.pembayaran import melakukan_pembayaran
            melakukan_pembayaran()
        elif pilihan == "3":
            from project.UAS.pembayaran import memilih_metode_pembayaran
            metode = memilih_metode_pembayaran()
            if metode:
                print(f"Metode pembayaran yang Anda pilih adalah: {metode}")
        elif pilihan == "4":
            from project.UAS.pembayaran import lihat_daftar_pembayaran
            lihat_daftar_pembayaran()
        elif pilihan == "5":
            from project.UAS.pembayaran import konfirmasi_pembayaran
            konfirmasi_pembayaran()
        elif pilihan == "0":
            print("Kembali ke Menu Utama...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


