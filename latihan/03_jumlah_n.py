
def jumlah_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


print("Jumlah 1 sampai n:")
for n in [1, 5, 10, 100]:
    print(f"n = {n}, hasil = {jumlah_n(n)}")
