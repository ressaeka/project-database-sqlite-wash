import sqlite3

conn = sqlite3.connect('PermenGagangWash.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS kendaraan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    merek TEXT NOT NULL,
    model TEXT NOT NULL,
    tahun INTEGER NOT NULL
)''')

def lihat_kendaraan():
    cursor.execute("SELECT * FROM kendaraan")
    rows = cursor.fetchall()
    if rows:
        print("\nDaftar Kendaraan:")
        for row in rows:
            print(f"ID: {row[0]}, Merek: {row[1]}, Model: {row[2]}, Tahun: {row[3]}")
    else:
        print("Tidak ada kendaraan yang terdaftar.")

def tambah_kendaraan():
    merek = input("Masukkan merek kendaraan: ").strip()
    model = input("Masukkan model kendaraan: ").strip()
    tahun = input("Masukkan tahun kendaraan: ").strip()
    if tahun.isdigit():
        tahun = int(tahun)
        cursor.execute("INSERT INTO kendaraan (merek, model, tahun) VALUES (?, ?, ?)", (merek, model, tahun))
        conn.commit()
        print(f"Kendaraan {merek} {model} ({tahun}) berhasil ditambahkan.")
    else:
        print("Tahun harus berupa angka.")
        pass

def lihat_detail_kendaraan():
    lihat_kendaraan()
    kendaraan_id = input("Masukkan ID kendaraan untuk melihat detail: ").strip()
    if kendaraan_id.isdigit():
        kendaraan_id = int(kendaraan_id)
        cursor.execute("SELECT * FROM kendaraan WHERE id = ?", (kendaraan_id,))
        kendaraan = cursor.fetchone()
        if kendaraan:
            print(f"\nDetail Kendaraan {kendaraan[1]} {kendaraan[2]} ({kendaraan[3]})")
        else:
            print("Kendaraan tidak ditemukan.")
    else:
        print("ID kendaraan harus berupa angka.")
        pass

def hapus_kendaraan():
    lihat_kendaraan()
    kendaraan_id = input("Masukkan ID kendaraan yang ingin dihapus: ").strip()
    if kendaraan_id.isdigit():
        kendaraan_id = int(kendaraan_id)
        cursor.execute("SELECT * FROM kendaraan WHERE id = ?", (kendaraan_id,))
        kendaraan = cursor.fetchone()
        if kendaraan:
            cursor.execute("DELETE FROM kendaraan WHERE id = ?", (kendaraan_id,))
            conn.commit()
            print(f"Kendaraan {kendaraan[1]} {kendaraan[2]} ({kendaraan[3]}) berhasil dihapus.")
        else:
            print("Kendaraan tidak ditemukan.")
    else:
        print("ID kendaraan harus berupa angka.")

