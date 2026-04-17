<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&text=TUGAS%201&fontSize=75&descAlignY=53&descAlign=50&fontAlignY=37&desc=Analisis%20Komunikasi%20Artemis%20II" alt="Header Tugas 1" />
</p>


## Deskripsi
Program ini dirancang untuk melakukan analisis data waktu sinyal aktif pada misi komunikasi NASA Artemis II. Program ini mengolah data menit-menit sinyal menjadi informasi sesi yang terstruktur.

## Logika Program
Alur pengerjaan program ini mengikuti tahapan berikut:
1. Identifikasi Sesi: Mengelompokkan menit sinyal yang berurutan sebagai satu sesi komunikasi tunggal.
2. Perhitungan Durasi: Menentukan lama waktu tiap sesi menggunakan rumus: (Waktu Akhir - Waktu Awal) + 1.
3. Seleksi Sesi Terbaik: Memilih sesi dengan durasi terlama. Jika terdapat durasi yang sama, sesi yang terjadi lebih awal akan diprioritaskan.
4. Estimasi Data: Menghitung total data yang dapat dikirim berdasarkan durasi sesi terbaik dengan rasio 10 data per menit.


## Struktur Data Input
Data input berupa daftar menit aktif sebagai berikut:
[5, 6, 7, 15, 16, 30, 31, 32, 60]

---
Java Maulana
