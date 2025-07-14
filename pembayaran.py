import sqlite3
from datetime import date

conn = sqlite3.connect('PermenGagangWash.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS pembayaran (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    layanan_id INTEGER NOT NULL,
    jumlah REAL NOT NULL,
    metode_pembayaran TEXT NOT NULL,
    status TEXT NOT NULL,  -- Contoh status: "Pending", "Lunas"
    tanggal DATE NOT NULL,
    FOREIGN KEY (layanan_id) REFERENCES layanan(id)
)''')

def lihat_daftar_pembayaran():
    cursor.execute("SELECT * FROM pembayaran")
    rows = cursor.fetchall()
    if rows:
        print("\nDaftar Pembayaran:")
        for row in rows:
            print(f"ID: {row[0]}, Layanan ID: {row[1]}, Jumlah: {row[2]}, Metode: {row[3]}, Status: {row[4]}, Tanggal: {row[5]}")
    else:
        print("Tidak ada pembayaran yang tercatat.")

def melakukan_pembayaran():
    layanan_id = input("Masukkan ID layanan yang ingin dibayar: ").strip()
    if layanan_id.isdigit():
        layanan_id = int(layanan_id)
        cursor.execute("SELECT harga FROM layanan WHERE id = ?", (layanan_id,))
        layanan = cursor.fetchone()
        if layanan:
            jumlah = layanan[0]
            print(f"Jumlah yang perlu dibayar: Rp {jumlah}")
            
            metode_pembayaran = input("Masukkan metode pembayaran (Cash, Transfer, Credit Card): ").strip()
            status = "Pending"
            tanggal = date.today().strftime('%Y-%m-%d')

            cursor.execute("INSERT INTO pembayaran (layanan_id, jumlah, metode_pembayaran, status, tanggal) VALUES (?, ?, ?, ?, ?)", 
                           (layanan_id, jumlah, metode_pembayaran, status, tanggal))
            conn.commit()
            print("Pembayaran berhasil dilakukan. Status: Pending.")
        else:
            print("Layanan tidak ditemukan.")
    else:
        print("ID layanan tidak valid.")

def memilih_metode_pembayaran():
    print("\nMetode Pembayaran:")
    print("1. Cash")
    print("2. Transfer")
    print("3. Credit Card")
    
    pilihan = input("Pilih metode pembayaran (1/2/3): ").strip()
    if pilihan == '1':
        return 'Cash'
    elif pilihan == '2':
        return 'Transfer'
    elif pilihan == '3':
        return 'Credit Card'
    else:
        print("Pilihan tidak valid.")
        return None

def lihat_riwayat_pembayaran():
    cursor.execute("SELECT * FROM pembayaran ORDER BY tanggal DESC")
    rows = cursor.fetchall()
    if rows:
        print("\nRiwayat Pembayaran:")
        for row in rows:
            print(f"ID: {row[0]}, Layanan ID: {row[1]}, Jumlah: {row[2]}, Metode: {row[3]}, Status: {row[4]}, Tanggal: {row[5]}")
    else:
        print("Tidak ada riwayat pembayaran.")

def konfirmasi_pembayaran():
    pembayaran_id = input("Masukkan ID pembayaran untuk dikonfirmasi: ").strip()
    if pembayaran_id.isdigit():
        pembayaran_id = int(pembayaran_id)
        cursor.execute("SELECT * FROM pembayaran WHERE id = ?", (pembayaran_id,))
        pembayaran = cursor.fetchone()
        if pembayaran:
            if pembayaran[4] == 'Pending':
                cursor.execute("UPDATE pembayaran SET status = 'Lunas' WHERE id = ?", (pembayaran_id,))
                conn.commit()
                print("Pembayaran berhasil dikonfirmasi.")
            else:
                print("Pembayaran sudah dikonfirmasi sebelumnya.")
        else:
            print("Pembayaran tidak ditemukan.")
    else:
        print("ID pembayaran tidak valid.")