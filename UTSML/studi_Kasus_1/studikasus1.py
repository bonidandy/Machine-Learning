#Bonifasius Dandy Krisnanda
#20210801002
#Teknik Informatika

import pandas as pd

# Data pada soal
data = {
    'HARI': ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'],
    'DATANG': [2, 3, 4, 1, 2, 5, 2],
    'BIAYA': [30000*2, 35000*3, 25000*4, 15000*1, 20000*2, 30000*5, 35000*2],
    'MAHASISWA': ['Ani', 'Budi', 'Jono', 'Lono', 'Joni', 'Ani', 'Budi']
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan DataFrame
print("Dataset:")
print(df)
print("\n")

# a) Berapa rata-rata mahasiswa datang pada minggu ini?
rata_rata_kehadiran = df['DATANG'].mean()
print("1.A Rata-rata mahasiswa datang pada minggu ini:", rata_rata_kehadiran, "\n")

# b) Kapan biaya tertinggi terjadi?
hari_biaya_tertinggi = df.loc[df['BIAYA'].idxmax()]['HARI']
print("1.B Biaya tertinggi terjadi pada hari:", hari_biaya_tertinggi, "\n")

# c) Hari apa biaya lebih dari 110000?
hari_diatas_110000 = df[df['BIAYA'] > 110000]['HARI'].tolist()
print("1.C Hari di mana biaya lebih dari 110000:", ', '.join(hari_diatas_110000), "\n")

# d) Siapa yang paling banyak datang ke kampus?
mahasiswa_terbanyak_datang = df['MAHASISWA'].value_counts().idxmax()
print("1.D Mahasiswa yang paling banyak datang ke kampus:", mahasiswa_terbanyak_datang, "\n")

# e) Siapa yang datang pada hari minggu?
mahasiswa_hari_minggu = df[df['HARI'] == 'Minggu']['MAHASISWA'].tolist()
print("1.E Mahasiswa yang datang pada hari Minggu:", ', '.join(mahasiswa_hari_minggu), "\n")

# f) Berapa biaya tertinggi dan terendah?
biaya_tertinggi = df['BIAYA'].max()
biaya_terendah = df['BIAYA'].min()
print("1.F Biaya tertinggi:", biaya_tertinggi)
print("1.F Biaya terendah:", biaya_terendah, "\n")

# g) Berapa frekuensi datang tertinggi dan terendah?
frekuensi_datang_tertinggi = df['DATANG'].max()
frekuensi_datang_terendah = df['DATANG'].min()
print("1.G Frekuensi datang tertinggi:", frekuensi_datang_tertinggi)
print("1.G Frekuensi datang terendah:", frekuensi_datang_terendah)
