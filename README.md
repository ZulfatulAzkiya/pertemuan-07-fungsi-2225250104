# pertemuan-07-fungsi-2225250104

**Nama:** Zulfatul Azkiya
**NIM:** 2225250104
**Kelas:** 3A

## Deskripsi

Proyek ini dibuat untuk memenuhi latihan dan Praktik 2
Pertemuan 07 tentang fungsi, parameter, return value,
dan scope dalam Python.

Program dibuat menggunakan Visual Studio Code dan
dikumpulkan melalui GitHub.

## Tujuan

1. Memahami definisi dan pemanggilan fungsi.
2. Menggunakan parameter dan argumen dengan benar.
3. Memahami perbedaan print dan return.
4. Memahami local scope dan global scope.
5. Menggunakan perulangan untuk menyelesaikan perhitungan.
6. Menguji program dengan beberapa test case.

## Struktur Folder

```text
pertemuan-07-fungsi-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_salam.py
│   ├── 02_luas_persegi_panjang.py
│   ├── 03_jumlah_n.py
│   ├── 04_statistik_sederhana.py
│   └── 05_scope.py
└── praktik/
    └── utilitas_matematika.py
```

## Daftar Latihan

### 1. Fungsi Salam
Menggunakan parameter nama dan kelas untuk
menampilkan salam kepada pengguna.

### 2. Luas Persegi Panjang
Menghitung luas dengan rumus panjang dikali lebar.
Fungsi mengembalikan hasil menggunakan return.

### 3. Jumlah 1 sampai n
Menghitung jumlah bilangan dari 1 sampai n
menggunakan perulangan for.

### 4. Statistik Sederhana
Menghitung nilai minimum, maksimum, dan rata-rata
dari sekumpulan data.

### 5. Eksperimen Scope
Memahami perbedaan variabel lokal di dalam fungsi
dan variabel global di luar fungsi.

## Praktik 2: Utilitas Matematika

Program utama menyediakan menu:
1. Luas persegi panjang
2. Luas segitiga
3. Jumlah 1 sampai n
4. Faktorial
5. Keluar

### Fungsi yang Digunakan

| Fungsi | Kegunaan |
|---|---|
| luas_persegi_panjang(p, l) | Menghitung luas persegi panjang |
| luas_segitiga(a, t) | Menghitung luas segitiga |
| jumlah_n(n) | Menghitung jumlah 1 sampai n |
| faktorial(n) | Menghitung faktorial bilangan |
| tampilkan_menu() | Menampilkan menu program |
| input_angka(pesan) | Memvalidasi input angka nonnegatif |
| input_bilangan_bulat(pesan) | Memvalidasi input bilangan bulat |
| jalankan_program() | Menjalankan menu utama |

## Cara Menjalankan

Pastikan Python sudah terpasang.

Jalankan salah satu perintah berikut di terminal
VS Code dari folder utama proyek.

Windows:

```bash
python latihan/01_salam.py
python latihan/02_luas_persegi_panjang.py
python latihan/03_jumlah_n.py
python latihan/04_statistik_sederhana.py
python latihan/05_scope.py
python praktik/utilitas_matematika.py
```

Jika perintah python tidak tersedia, coba gunakan
python3 sesuai konfigurasi perangkat.

## Hasil Pengujian

| Pengujian | Input | Hasil yang Diharapkan |
|---|---|---|
| Luas persegi panjang | p=8, l=5 | 40 |
| Luas segitiga | a=10, t=6 | 30.0 |
| Jumlah 1 sampai n | n=10 | 55 |
| Faktorial | n=5 | 120 |
| Faktorial | n=0 | 1 |

## Refleksi

Dengan menggunakan fungsi, program menjadi lebih
terstruktur dan mudah dibaca. Rumus dapat ditulis
satu kali dan digunakan kembali melalui parameter
yang berbeda.

Penggunaan return memungkinkan hasil perhitungan
disimpan atau digunakan dalam proses lain. Variabel
lokal juga membantu membatasi penggunaan variabel
agar tidak tertukar dengan variabel di luar fungsi.
