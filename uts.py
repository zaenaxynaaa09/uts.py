# 1. Bilangan di input dari Pengguna
# Kita gunakan try-except untuk menangani jika pengguna memasukkan selain angka
try:
    nilai =int(input("masukkan sebuah bilangan (maksimal 7 digit): "))
   
    # 2.Proses Perhitungan Nilai Tempat
    # Batas Hingga 2000000
    if 0 <= nilai <= 2000000:

        print("=======================================")
        
        # nilai jutaan 
        jutaan = nilai // 1000000
        # sisa setelah diambil jutaannya
        sisa_jutaan = nilai % 1000000
        
        # nilai ratusan_ribu dari sisa_jutaan
        ratusan_ribu = sisa_jutaan // 100000
        # sisa setelah diambil ratusan ribunya 
        sisa_ratusan_ribu = sisa_jutaan % 100000
        
        # nilai puluhan_ribu dari sisa_ratusan ribu
        puluhan_ribu = sisa_ratusan_ribu // 10000
        # sisa setelah diambil puluhan_ribu
        sisa_puluhan_ribu = sisa_ratusan_ribu % 10000

        # nilai ribuan dari sisa_puluhan ribu
        ribuan = sisa_puluhan_ribu // 1000
        # sisa setelah diambil ribuan 
        sisa_ribuan = sisa_puluhan_ribu % 1000

        # nilai ratusan dari sisa_ribuan
        ratusan = sisa_ribuan // 100
        # sisa setelah diambil ratusan 
        sisa_ratusan = sisa_ribuan % 100

        # nilai puluhan dari sisa_ratusan
        puluhan = sisa_ratusan // 10
        # sisa setelah diambil puluhan
        sisa_puluhan = sisa_ratusan % 10

        # nilai satuan dari sisa_puluhan
        satuan = sisa_puluhan // 1
        # sisa setelah diambil satuan
        sisa_satuan = sisa_puluhan % 1
        
        print("===========================================")

        # 3. Tampilkan hasil sesuai format
        print(f"\nAnda memasukkan bilangan {nilai} dimana;")
        print(f"{jutaan} adalah jutaan")
        print(f"{ratusan_ribu} adalah ratusan ribu")
        print(f"{puluhan_ribu} adalah puluhan ribu")
        print(f"{ribuan} adalah ribuan")
        print(f"{ratusan} adalah ratusan")
        print(f"{puluhan} adalah puluhan")
        print(f"{satuan} adalah satuan")

    else:
        print("Harap masukkan angka antara 0 dan 2000000.")
   
except:
    print("Yang anda masukkan tidak valid! Harap memasukkan angka saja.")