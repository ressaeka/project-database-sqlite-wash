🚗 SewaKuy

**SewaKuy** adalah aplikasi sederhana berbasis Python untuk melakukan pemesanan kendaraan. Sistem ini memungkinkan pengguna untuk login, memilih kendaraan dan layanan, melakukan pemesanan, serta menyelesaikan pembayaran.

📌 Fitur Utama

- 🔐 Login pengguna
- 🚘 Manajemen data kendaraan
- 🧾 Pemilihan layanan (misalnya: dengan sopir, lepas kunci)
- 📅 Pemesanan kendaraan
- 💳 Pembayaran

 📁 Struktur File

| File              | Fungsi                                               |
|-------------------|------------------------------------------------------|
| `index.py`        | Titik masuk utama aplikasi                           |
| `loginuser.py`    | Autentikasi dan manajemen akun pengguna              |
| `kendaraan.py`    | Data dan pengelolaan kendaraan                       |
| `layanan.py`      | Opsi layanan yang ditawarkan                         |
| `pemesanan.py`    | Proses pemesanan kendaraan oleh pengguna             |
| `pembayaran.py`   | Proses pembayaran dan validasi                       |
| `PermenGagangW...`| Kemungkinan file database SQLite atau penyimpanan    |



▶️ Cara Menjalankan

1. Pastikan Python sudah terinstal.
2. Jalankan program menggunakan perintah berikut:
   ```bash
   python index.py
