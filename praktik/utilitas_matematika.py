
def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus bilangan bulat nonnegatif.")

    total = 0
    for i in range(1, n + 1):
        total += i

    return total


def faktorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus bilangan bulat nonnegatif.")

    hasil = 1
    for i in range(2, n + 1):
        hasil *= i

    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")


def input_angka(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            if nilai < 0:
                print("Angka tidak boleh negatif.")
                continue
            return nilai
        except ValueError:
            print("Input harus berupa angka yang valid.")


def input_bilangan_bulat(pesan):
    while True:
        try:
            teks = input(pesan).strip()
            nilai = int(teks)

            if nilai < 0:
                print("Bilangan tidak boleh negatif.")
                continue

            return nilai
        except ValueError:
            print("Masukkan bilangan bulat nonnegatif.")


def jalankan_program():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        try:
            if pilihan == "1":
                p = input_angka("Masukkan panjang: ")
                l = input_angka("Masukkan lebar: ")
                hasil = luas_persegi_panjang(p, l)
                print("Luas persegi panjang =", hasil)

            elif pilihan == "2":
                a = input_angka("Masukkan alas: ")
                t = input_angka("Masukkan tinggi: ")
                hasil = luas_segitiga(a, t)
                print("Luas segitiga =", hasil)

            elif pilihan == "3":
                n = input_bilangan_bulat("Masukkan n: ")
                print("Jumlah 1 sampai", n, "=", jumlah_n(n))

            elif pilihan == "4":
                n = input_bilangan_bulat("Masukkan n: ")
                print("Faktorial", n, "=", faktorial(n))

            elif pilihan == "5":
                print("Program selesai. Terima kasih!")
                break

            else:
                print("Pilihan tidak valid. Pilih angka 1-5.")

        except ValueError as error:
            print("Terjadi kesalahan:", error)


if __name__ == "__main__":
    jalankan_program()
