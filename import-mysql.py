import mysql.connector

# Konfigurasi koneksi MySQL
db_config = {
    'host': 'localhost',  # Ganti dengan host MySQL Anda
    'user': 'root',       # Ganti dengan username MySQL Anda
    'password': '',       # Ganti dengan password MySQL Anda
    'database': 'fastprint_db'  # Nama database yang ingin Anda gunakan
}

# Buat koneksi ke MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Buat tabel produk di MySQL
create_table_query = """
CREATE TABLE IF NOT EXISTS produk (
    no INT PRIMARY KEY,
    id_produk INT,
    nama_produk VARCHAR(255),
    kategori VARCHAR(255),
    harga INT,
    status VARCHAR(50)
);
"""
cursor.execute(create_table_query)

# Menyisipkan data ke dalam tabel
insert_query = """
INSERT INTO produk (no, id_produk, nama_produk, kategori, harga, status)
VALUES (%s, %s, %s, %s, %s, %s);
"""

# Data produk untuk dimasukkan
produk_data = [
    (7, 6, "ALCOHOL GEL POLISH CLEANSER GP-CLN01", "L QUEENLY", 12500, "bisa dijual"),
    (10, 9, "ALUMUNIUM FOIL ALL IN ONE BULAT 23mm IM", "L MTH AKSESORIS (IM)", 1000, "bisa dijual"),
    (12, 11, "ALUMUNIUM FOIL ALL IN ONE BULAT 30mm IM", "L MTH AKSESORIS (IM)", 1000, "bisa dijual"),
    (13, 12, "ALUMUNIUM FOIL ALL IN ONE SHEET 250mm IM", "L MTH AKSESORIS (IM)", 12500, "tidak bisa dijual"),
    (16, 15, "ALUMUNIUM FOIL HDPE/PE BULAT 23mm IM", "L MTH AKSESORIS (IM)", 12500, "bisa dijual"),
    (18, 17, "ALUMUNIUM FOIL HDPE/PE BULAT 30mm IM", "L MTH AKSESORIS (IM)", 1000, "bisa dijual"),
    (19, 18, "ALUMUNIUM FOIL HDPE/PE SHEET 250mm IM", "L MTH AKSESORIS (IM)", 13000, "tidak bisa dijual"),
    (20, 19, "ALUMUNIUM FOIL PET SHEET 250mm IM", "L MTH AKSESORIS (IM)", 1000, "tidak bisa dijual"),
    (23, 22, "ARM PENDEK MODEL U", "L MTH AKSESORIS (IM)", 13000, "bisa dijual"),
    (24, 23, "ARM SUPPORT KECIL", "L MTH TABUNG (LK)", 13000, "tidak bisa dijual"),
    (25, 24, "ARM SUPPORT KOTAK PUTIH", "L MTH AKSESORIS (IM)", 13000, "tidak bisa dijual"),
    (27, 26, "ARM SUPPORT PENDEK POLOS", "L MTH TABUNG (LK)", 13000, "bisa dijual"),
    (28, 27, "ARM SUPPORT S IM", "L MTH AKSESORIS (IM)", 1000, "tidak bisa dijual"),
    (29, 28, "ARM SUPPORT T (IMPORT)", "L MTH AKSESORIS (IM)", 13000, "bisa dijual"),
    (30, 29, "ARM SUPPORT T - MODEL 1 ( LOKAL )", "L MTH TABUNG (LK)", 10000, "bisa dijual"),
    (51, 50, "BLACK LASER TONER FP-T3 (100gr)", "L MTH AKSESORIS (IM)", 13000, "tidak bisa dijual"),
    (57, 56, "BODY PRINTER CANON IP2770", "SP MTH SPAREPART (LK)", 500, "bisa dijual"),
    (59, 58, "BODY PRINTER T13X", "SP MTH SPAREPART (LK)", 15000, "bisa dijual"),
    (60, 59, "BOTOL 1000ML BLUE KHUSUS UNTUK EPSON R1800/R800 - 4180 IM (T054920)", "CI MTH TINTA LAIN (IM)", 10000, "bisa dijual"),
    (61, 60, "BOTOL 1000ML CYAN KHUSUS UNTUK EPSON R1800/R800/R1900/R2000 - 4120 IM (T054220)", "CI MTH TINTA LAIN (IM)", 10000, "tidak bisa dijual"),
    (62, 61, "BOTOL 1000ML GLOSS OPTIMIZER KHUSUS UNTUK EPSON R1800/R800/R1900/R2000/IX7000/MG6170 - 4100 IM (T054020)", "CI MTH TINTA LAIN (IM)", 1500, "bisa dijual"),
    (63, 62, "BOTOL 1000ML L.LIGHT BLACK KHUSUS UNTUK EPSON 2400 - 0599 IM", "CI MTH TINTA LAIN (IM)", 1500, "tidak bisa dijual"),
    (64, 63, "BOTOL 1000ML LIGHT BLACK KHUSUS UNTUK EPSON 2400 - 0597 IM", "CI MTH TINTA LAIN (IM)", 1500, "tidak bisa dijual"),
    (65, 64, "BOTOL 1000ML MAGENTA KHUSUS UNTUK EPSON R1800/R800/R1900/R2000 - 4140 IM (T054320)", "CI MTH TINTA LAIN (IM)", 1000, "bisa dijual"),
    (66, 65, "BOTOL 1000ML MATTE BLACK KHUSUS UNTUK EPSON R1800/R800/R1900/R2000 - 3503 IM (T054820)", "CI MTH TINTA LAIN (IM)", 1500, "tidak bisa dijual"),
    (67, 66, "BOTOL 1000ML ORANGE KHUSUS UNTUK EPSON R1900/R2000 IM - 4190 (T087920)", "CI MTH TINTA LAIN (IM)", 1500, "bisa dijual"),
    (68, 67, "BOTOL 1000ML RED KHUSUS UNTUK EPSON R1800/R800/R1900/R2000 - 4170 IM (T054720)", "CI MTH TINTA LAIN (IM)", 1000, "tidak bisa dijual"),
    (69, 68, "BOTOL 1000ML YELLOW KHUSUS UNTUK EPSON R1800/R800/R1900/R2000 - 4160 IM (T054420)", "CI MTH TINTA LAIN (IM)", 1500, "tidak bisa dijual"),
    (71, 70, "BOTOL KOTAK 100ML LK", "L MTH AKSESORIS (LK)", 1000, "bisa dijual"),
    (73, 72, "BOTOL 10ML IM", "S MTH STEMPEL (IM)", 1000, "tidak bisa dijual")
]

# Menyisipkan data ke dalam tabel
cursor.executemany(insert_query, produk_data)
conn.commit()

# Menutup koneksi
cursor.close()
conn.close()

print("Data berhasil disimpan di MySQL")
