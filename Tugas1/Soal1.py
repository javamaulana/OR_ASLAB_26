waktu_sinyal = [5, 6, 7, 15, 16, 30, 31, 32, 60]

semua_sesi = []
sesi_saat_ini = [waktu_sinyal[0]]

for i in range(1, len(waktu_sinyal)):
    
    if waktu_sinyal[i] == waktu_sinyal[i-1] + 1:
        sesi_saat_ini.append(waktu_sinyal[i]) 
    else:
        semua_sesi.append(sesi_saat_ini)
        sesi_saat_ini = [waktu_sinyal[i]]

semua_sesi.append(sesi_saat_ini)

print("===========================================")
print("      HASIL ANALISIS KOMUNIKASI NASA       ")
print("===========================================")

print(f"\nWaktu sinyal aktif: {waktu_sinyal}")
print("\n--- Daftar Sesi yang Ditemukan ---")
sesi_terbaik = []
durasi_terlama = 0

nomor = 1
for sesi in semua_sesi:
    durasi = sesi[-1] - sesi[0] + 1
    print(f"Sesi {nomor}: {sesi} -> Durasinya {durasi} menit")
    
    if durasi > durasi_terlama:
        durasi_terlama = durasi
        sesi_terbaik = sesi
    nomor += 1

print("\n-------------------------------------------")
print(f"🌟 Sesi Terbaik: {sesi_terbaik}")
print(f"⏱️ Durasi: {durasi_terlama} menit")

total_data = durasi_terlama * 10
print(f"📊 Total data yang bisa dikirim: {total_data} data")
print("-------------------------------------------")