import sqlite3
from datetime import date

conn = sqlite3.connect('PermenGagangWash.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS pemesanan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    layanan_id INTEGER NOT NULL,
    kendaraan_id INTEGER NOT NULL,
    tanggal_pemesanan DATE NOT NULL,
    status TEXT NOT NULL, -- Status seperti "Pending", "Dikonfirmasi", "Dibatalkan"
    FOREIGN KEY (layanan_id) REFERENCES layanan(id),
    FOREIGN KEY (kendaraan_id) REFERENCES kendaraan(id)
)''')

def lihat_daftar_pemesanan():
    cursor.execute("SELECT * FROM pemesanan")
    rows = cursor.fetchall()
    if rows:
        print("\nDaftar Pemesanan:")
        for row in rows:
            print(f"ID: {row[0]}, Layanan ID: {row[1]}, Kendaraan ID: {row[2]}, Tanggal: {row[3]}, Status: {row[4]}")
    else:
        print("Tidak ada pemesanan yang tercatat.")

def membuat_pemesanan():
    layanan_id = input("Masukkan ID layanan: ").strip()
    kendaraan_id = input("Masukkan ID kendaraan: ").strip()
    if layanan_id.isdigit() and kendaraan_id.isdigit():
        tanggal_pemesanan = date.today().strftime('%Y-%m-%d')
        status = "Pending"
        cursor.execute("INSERT INTO pemesanan (layanan_id, kendaraan_id, tanggal_pemesanan, status) VALUES (?, ?, ?, ?)",
                       (int(layanan_id), int(kendaraan_id), tanggal_pemesanan, status))
        conn.commit()
        print("Pemesanan berhasil dibuat dengan status: Pending.")
    else:
        print("ID layanan dan ID kendaraan harus berupa angka.")

def melihat_detail_pemesanan():
    lihat_daftar_pemesanan()
    pemesanan_id = input("Masukkan ID pemesanan untuk melihat detail: ").strip()
    if pemesanan_id.isdigit():
        cursor.execute("SELECT * FROM pemesanan WHERE id = ?", (int(pemesanan_id),))
        pemesanan = cursor.fetchone()
        if pemesanan:
            print(f"Detail Pemesanan ID: {pemesanan[0]}")
            print(f"Layanan ID: {pemesanan[1]}, Kendaraan ID: {pemesanan[2]}, Tanggal: {pemesanan[3]}, Status: {pemesanan[4]}")
        else:
            print("Pemesanan tidak ditemukan.")
    else:
        print("ID pemesanan harus berupa angka.")

def mengedit_pemesanan():
    lihat_daftar_pemesanan()
    pemesanan_id = input("Masukkan ID pemesanan yang ingin diedit: ").strip()
    if pemesanan_id.isdigit():
        pemesanan_id = int(pemesanan_id)
        cursor.execute("SELECT * FROM pemesanan WHERE id = ?", (pemesanan_id,))
        pemesanan = cursor.fetchone()
        if pemesanan:
            print("1. Ubah Status")
            print("2. Batalkan Pemesanan")
            pilihan = input("Pilih opsi: ").strip()
            if pilihan == "1":
                status_baru = input("Masukkan status baru (Pending/Dikonfirmasi/Dibatalkan): ").strip()
                cursor.execute("UPDATE pemesanan SET status = ? WHERE id = ?", (status_baru, pemesanan_id))
                conn.commit()
                print("Status pemesanan berhasil diubah.")
            elif pilihan == "2":
                cursor.execute("DELETE FROM pemesanan WHERE id = ?", (pemesanan_id,))
                conn.commit()
                print("Pemesanan berhasil dibatalkan.")
            else:
                print("Pilihan tidak valid.")
        else:
            print("Pemesanan tidak ditemukan.")
    else:
        print("ID pemesanan harus berupa angka.")

def lihat_riwayat_pemesanan():
    cursor.execute("SELECT * FROM pemesanan ORDER BY tanggal_pemesanan DESC")
    rows = cursor.fetchall()
    if rows:
        print("\nRiwayat Pemesanan:")
        for row in rows:
            print(f"ID: {row[0]}, Layanan ID: {row[1]}, Kendaraan ID: {row[2]}, Tanggal: {row[3]}, Status: {row[4]}")
    else:
        print("Tidak ada riwayat pemesanan.")
