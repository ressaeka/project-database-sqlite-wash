import sqlite3

conn = sqlite3.connect('PermenGagangWash.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS layanan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    detail TEXT,
    harga REAL NOT NULL
)''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS riwayat_layanan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    layanan_id INTEGER,
    status TEXT,
    FOREIGN KEY(layanan_id) REFERENCES layanan(id)
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS testimoni (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    layanan_id INTEGER NOT NULL,
    ulasan TEXT NOT NULL,
    FOREIGN KEY(layanan_id) REFERENCES layanan(id)
)''')


cursor.execute("SELECT COUNT(*) FROM layanan")
count = cursor.fetchone()[0]
if count == 0:
    layanan_default = [
        ("Cuci Motor Standar"  , "Pembersihan bagian luar Motor", 20000),
        ("Cuci Motor Detailing", "Pembersihan Rantai, Mesin dan Sela sela Motor", 30000),
        ("Cuci Poles Motor"    , "Untuk menghilangkan goresan ringan dan mengkilap", 40000),
        ("Cuci Mobil Standar"  , "Pembersihan bagian luar Mobil, Seperti Body, Velg dan Ban", 60000),
        ("Pembersihan Interior", "Vakum Interior untuk membersihkan Debu dan Kotoran", 30000),
        ("Poles Dan Waxing"    , "Meningkatkan ketahanan terhadap goresan ringan dan sinar uv", 200000),
    ]
    
    cursor.executemany("INSERT INTO layanan (nama, detail, harga) VALUES (?, ?, ?)", layanan_default)
    conn.commit()

cursor.execute("SELECT * FROM layanan")
layanan_data = cursor.fetchall()
for layanan in layanan_data:
    print(layanan)

def lihat_layanan():
    cursor.execute("SELECT * FROM layanan")
    rows = cursor.fetchall()
    if rows:
        print("\nDaftar Layanan:")
        for row in rows:
            print(f"ID: {row[0]}, Nama: {row[1]}, Detail: {row[2]}, Harga: Rp {row[3]:,.2f}")
    else:
        print("Tidak ada layanan yang terdaftar.")


def pilih_layanan_pemesanan():
    lihat_layanan()
    layanan_id = input("Masukkan ID layanan yang ingin dipesan: ").strip()
    if layanan_id.isdigit():
        layanan_id = int(layanan_id)
        cursor.execute("SELECT * FROM layanan WHERE id = ?", (layanan_id,))
        layanan = cursor.fetchone()
        if layanan:
            cursor.execute("INSERT INTO riwayat_layanan (layanan_id, status) VALUES (?, ?)", (layanan_id, 'Dipesan'))
            conn.commit()
            print(f"Layanan {layanan[1]} berhasil dipesan.")
        else:
            print("Layanan tidak ditemukan.")
    else:
        print("ID layanan harus berupa angka.")

def lihat_detail_layanan():
    lihat_layanan()
    layanan_id = input("Masukkan ID layanan untuk melihat detail: ").strip()
    if layanan_id.isdigit():
        layanan_id = int(layanan_id)
        cursor.execute("SELECT * FROM layanan WHERE id = ?", (layanan_id,))
        layanan = cursor.fetchone()
        if layanan:
            print(f"\nDetail Layanan {layanan[1]}: {layanan[2]}")
        else:
            print("Layanan tidak ditemukan.")
    else:
        print("ID layanan harus berupa angka.")

def lihat_riwayat_layanan():
    cursor.execute("SELECT * FROM riwayat_layanan")
    rows = cursor.fetchall()
    if rows:
        print("\nRiwayat Layanan yang Dipesan:")
        for row in rows:
            cursor.execute("SELECT nama FROM layanan WHERE id = ?", (row[1],))
            layanan = cursor.fetchone()
            print(f"ID Layanan: {layanan[0]}, Status: {row[2]}")
    else:
        print("Belum ada riwayat layanan yang dipesan.")

def lihat_testimoni():
    lihat_layanan() 
    layanan_id = input("Masukkan ID layanan untuk melihat testimoni: ").strip()
    if layanan_id.isdigit():
        layanan_id = int(layanan_id)
        cursor.execute("SELECT * FROM layanan WHERE id = ?", (layanan_id,))
        layanan = cursor.fetchone()
        if layanan:
            cursor.execute("SELECT ulasan FROM testimoni WHERE layanan_id = ?", (layanan_id,))
            testimoni = cursor.fetchall()
            print(f"\nTestimoni untuk Layanan '{layanan[1]}':")
            if testimoni:
                for i, t in enumerate(testimoni, start=1):
                    print(f"{i}. {t[0]}")
            else:
                print("Belum ada testimoni untuk layanan ini.")
        else:
            print("Layanan tidak ditemukan.")
    else:
        print("ID layanan harus berupa angka.")

def tambah_testimoni():
    lihat_layanan() 
    layanan_id = input("Masukkan ID layanan untuk memberikan testimoni: ").strip()
    if layanan_id.isdigit():
        layanan_id = int(layanan_id)
        cursor.execute("SELECT * FROM layanan WHERE id = ?", (layanan_id,))
        layanan = cursor.fetchone()
        if layanan:
            ulasan = input("Masukkan testimoni Anda: ").strip()
            if ulasan:
                cursor.execute("INSERT INTO testimoni (layanan_id, ulasan) VALUES (?, ?)", (layanan_id, ulasan))
                conn.commit()
                print("Testimoni Anda berhasil ditambahkan.")
            else:
                print("Testimoni tidak boleh kosong.")
        else:
            print("Layanan tidak ditemukan.")
    else:
        print("ID layanan harus berupa angka.")
