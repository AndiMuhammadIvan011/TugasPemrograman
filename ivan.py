def tampilkan_menu():
    print("Selamat datang di Warung Ayam Geprek")
    print("1. Pesan Ayam Geprek")
    print("2. Lihat Pesanan")
    print("3. Hitung Total Harga")
    print("4. Keluar")

def pesan_ayam_geprek(pesanan, menu_ayam_geprek):
    print("Menu Ayam Geprek:")
    for index, menu in enumerate(menu_ayam_geprek, 1):
        print(f"{index}. {menu['nama']} - Rp {menu['harga']}")

    nomor_pesanan = int(input("Masukkan nomor ayam geprek yang ingin dipesan: "))
    jumlah_pesanan = int(input("Masukkan jumlah ayam geprek yang ingin dipesan: "))

    if 1 <= nomor_pesanan <= len(menu_ayam_geprek):
        pesanan.append({"nama": menu_ayam_geprek[nomor_pesanan - 1]['nama'], "harga": menu_ayam_geprek[nomor_pesanan - 1]['harga'], "jumlah": jumlah_pesanan})
        print(f"{jumlah_pesanan} {menu_ayam_geprek[nomor_pesanan - 1]['nama']} telah ditambahkan ke pesanan.")
    else:
        print("Nomor pesanan tidak valid")

def lihat_pesanan(pesanan):
    print("Pesanan Anda:")
    for item in pesanan:
        print(f"{item['jumlah']} {item['nama']} - Rp {item['harga']} per item")

def hitung_total_harga(pesanan):
    total = sum(item['harga'] * item['jumlah'] for item in pesanan)
    print(f"Total harga pesanan Anda: Rp {total}")

def warung_ayam_geprek():
    menu_ayam_geprek = [
        {"nama": "Ayam Geprek Original", "harga": 15000},
        {"nama": "Ayam Geprek Pedas", "harga": 18000},
        {"nama": "Ayam Geprek Cheese", "harga": 20000}
    ]

    pesanan = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            pesan_ayam_geprek(pesanan, menu_ayam_geprek)
        elif pilihan == '2':
            lihat_pesanan(pesanan)
        elif pilihan == '3':
            hitung_total_harga(pesanan)
        elif pilihan == '4':
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "_main_":
    warung_ayam_geprek()