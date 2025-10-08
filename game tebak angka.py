def main():
    print("=== Selamat datang di Game Tebak Angka! ===")
    print("Saya sudah memilih sebuah angka antara 1 sampai 10.")
    print("Bisakah kamu menebaknya? Kamu punya 3 kesempatan.")

    angka_rahasia = random.randint(1, 10)
    kesempatan = 3

    while kesempatan > 0:
        try:
            tebakan = int(input("Tebakan kamu: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if tebakan == angka_rahasia:
            print("🎉 Selamat! Kamu menebak dengan benar!")
            break
        elif tebakan < angka_rahasia:
            print("Terlalu kecil!")
        else:
            print("Terlalu besar!")

        kesempatan -= 1
        print(f"Sisa kesempatan: {kesempatan}")

    if kesempatan == 0:
        print(f"💥 Kesempatan habis! Angka yang benar adalah {angka_rahasia}")

if _name_ == "_main_":
    main()