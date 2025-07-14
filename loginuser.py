import sqlite3
import os
from project.UAS.index import main_dashboard

conn = sqlite3.connect('PermenGagangWash.db')
cursor = conn.cursor()

cursor.execute ('''CREATE TABLE IF NOT EXISTS pengguna (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
)''')

def halaman_user():
    while True:
        os.system("cls")
        print("SELAMAT DATANG DI PERMEN GAGANG WASH!!")
        print("SILAKAN DAFTAR DAN LOGIN TERLEBIH DAHULU")
        print("-" * 38)
        print("1. Daftar Pengguna Baru")
        print("2. Login Pengguna")
        print("0. Keluar\n")
        
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            daftar_pengguna()
        elif pilihan == "2":
            if login_pengguna():
                break 
        elif pilihan == "0":
            print("Terimakash telah datang di PermenGagangWash, Sampai jumpa kembali!!")
            exit()
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk kembali ke menu utama...")

def daftar_pengguna():
    conn = sqlite3.connect('PermenGagangWash.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pengguna (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    cursor.execute("SELECT * FROM pengguna WHERE username = ?", (username,))
    if cursor.fetchone():
        print("Username sudah terdaftar.")
    else:
        cursor.execute("INSERT INTO pengguna (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Pendaftaran berhasil!")

    conn.close()

def login_pengguna():
    conn = sqlite3.connect('PermenGagangWash.db')
    cursor = conn.cursor()

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    cursor.execute("SELECT * FROM pengguna WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user:
        if user[2] == password:
            print(f"Selamat datang, {username}!")
            conn.close() 
            main_dashboard()  
            return True  
        else:
            print("Password salah. Silakan coba lagi.")
    else:
        print("Username tidak ditemukan. Silakan daftar terlebih dahulu.")

    conn.close()  
    input("Tekan Enter untuk kembali ke menu login...")
    return False

if __name__ == "__main__":
    halaman_user()