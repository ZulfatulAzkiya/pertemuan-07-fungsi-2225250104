
def statistik(data):
    if len(data) == 0:
        raise ValueError("Data tidak boleh kosong.")

    total = 0
    minimum = data[0]
    maksimum = data[0]

    for x in data:
        total += x

        if x < minimum:
            minimum = x

        if x > maksimum:
            maksimum = x

    rata_rata = total / len(data)

    return minimum, maksimum, rata_rata


data_nilai = [70, 80, 65, 90, 75]
minimum, maksimum, rata_rata = statistik(data_nilai)

print("Data nilai:", data_nilai)
print("Nilai minimum:", minimum)
print("Nilai maksimum:", maksimum)
print("Rata-rata:", rata_rata)
