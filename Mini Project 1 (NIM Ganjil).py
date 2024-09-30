
#Masukkan Nama dan NIM

Nama = input("\n▶️ Nama: ")
NIM = input("▶️ NIM: ")

print("\nHalo,", Nama, "🤗")
print("Ayo Hitung Gaji Kamu👇")

# Input Jam Kerja dan Tarif Kerja Per Jam

while True:
    
    print("\n----------------------------------------------------------------------------------------")
    A = float(input("\n🕛 Total jam bekerja: "))

    B = float(input("💵 Tarif kerja per jam: Rp "))

#Hitungan

    gaji_pokok = A * B
    print("\nGaji Pokok Kamu👉: Rp ", gaji_pokok)

    if A > 160:
        jumlah_bonus = 0.1 * gaji_pokok  
        print("Selamat❗ Kamu mendapat bonus 10% dari gaji pokok kamu sebanyak: Rp ",jumlah_bonus, "🎉")
        total_gaji = jumlah_bonus + gaji_pokok
        print("\n💸 Total Gaji Kamu: Rp", total_gaji, "💸")
        print("\n----------------------------------------------------------------------------------------")
    else:
        print("❌ Bonus: Rp 0 ❌")
        print("\n💸 Total Gaji Kamu: Rp ",gaji_pokok, "💸")
        print("\n----------------------------------------------------------------------------------------")

#Beri Pilihan Ingin Menghitung Ulang Atau Tidak

    ulang = input("\nMau Menghitung Gaji Lagi? 🤔 (ya/tidak): ")
    if ulang == "ya":
        continue
    else:
        print("\n----------------------------------------------------------------------------------------")
        print("\nBaik, Terima Kasih Atas Waktunya🤗")
        break
