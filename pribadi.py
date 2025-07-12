import csv
import os

# Inisialisasi struktur data
data_transaksi = []  # list
kategori_pengeluaran = {  # dictionary
    "Makanan": [],
    "Transportasi": [],
    "Pendidikan": [],
    "Hiburan": [],
    "Lainnya": []
}

# Membuat file CSV jika belum ada
def inisialisasi_csv():
    if not os.path.exists("transaksi.csv"):
        with open("transaksi.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Tanggal", "Jenis", "Nominal", "Kategori", "Deskripsi"])

# Tambah transaksi
def tambah_transaksi():
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    jenis = input("Jenis (Pemasukan/Pengeluaran): ").capitalize()
    nominal = float(input("Nominal: "))
    kategori = input("Kategori: ").capitalize()
    deskripsi = input("Deskripsi: ")

    transaksi = [tanggal, jenis, nominal, kategori, deskripsi]
    data_transaksi.append(transaksi)

    with open("transaksi.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(transaksi)

    if jenis == "Pengeluaran":
        if kategori in kategori_pengeluaran:
            kategori_pengeluaran[kategori].append(transaksi)
        else:
            kategori_pengeluaran["Lainnya"].append(transaksi)

    print("✅ Transaksi berhasil ditambahkan.")

# Laporan bulanan
def laporan_bulanan():
    bulan = input("Masukkan Bulan (MM): ")
    tahun = input("Masukkan Tahun (YYYY): ")
    pemasukan = 0
    pengeluaran = 0

    with open("transaksi.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            if row[0].startswith(f"{tahun}-{bulan}"):
                if row[1] == "Pemasukan":
                    pemasukan += float(row[2])
                elif row[1] == "Pengeluaran":
                    pengeluaran += float(row[2])

    print(f"\n Laporan Bulan {bulan}/{tahun}")
    print(f"Total Pemasukan   : Rp {pemasukan}")
    print(f"Total Pengeluaran : Rp {pengeluaran}")
    print(f"Saldo             : Rp {pemasukan - pengeluaran}")

# Laporan tahunan
def laporan_tahunan():
    tahun = input("Masukkan Tahun (YYYY): ")
    pemasukan = 0
    pengeluaran = 0

    with open("transaksi.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0].startswith(tahun):
                if row[1] == "Pemasukan":
                    pemasukan += float(row[2])
                elif row[1] == "Pengeluaran":
                    pengeluaran += float(row[2])

    print(f"\n Laporan Tahun {tahun}")
    print(f"Total Pemasukan   : Rp {pemasukan}")
    print(f"Total Pengeluaran : Rp {pengeluaran}")
    print(f"Saldo             : Rp {pemasukan - pengeluaran}")

# Tampilkan kategori
def tampilkan_kategori():
    print("\n Kategori Pengeluaran:")
    for kategori, transaksi in kategori_pengeluaran.items():
        print(f"\n {kategori}")
        if not transaksi:
            print("  (tidak ada data)")
        else:
            for t in transaksi:
                print(f"  - {t[0]} | Rp {t[2]} | {t[4]}")

# Menu CLI
def tampilkan_menu():
    inisialisasi_csv()
    while True:
        print("\n====== MENU APLIKASI KEUANGAN ======")
        print("1. Tambah Transaksi")
        print("2. Laporan Bulanan")
        print("3. Laporan Tahunan")
        print("4. Lihat Kategori Pengeluaran")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tambah_transaksi()
        elif pilihan == '2':
            laporan_bulanan()
        elif pilihan == '3':
            laporan_tahunan()
        elif pilihan == '4':
            tampilkan_kategori()
        elif pilihan == '5':
            print(" Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print(" Pilihan tidak valid. Coba lagi.")

# Jalankan program
if __name__ == "__main__":
    tampilkan_menu()
