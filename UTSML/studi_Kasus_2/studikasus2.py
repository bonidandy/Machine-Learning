import pandas as pd
import matplotlib.pyplot as plt

# Data
fakultas = ["Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain"]
jumlah_mahasiswa = [260, 28, 284, 465, 735]
akreditasi = ["A", "A", "B", "A", "A"]

# Buat DataFrame
info_mahasiswa = pd.DataFrame({
    "Fakultas": fakultas,
    "Jumlah Mahasiswa": jumlah_mahasiswa,
    "Akreditasi": akreditasi
})

print(info_mahasiswa)

# Plot data
plt.figure(figsize=(10, 6))
plt.bar(info_mahasiswa["Fakultas"], info_mahasiswa["Jumlah Mahasiswa"], color='skyblue')
plt.xlabel('Fakultas')
plt.ylabel('Jumlah Mahasiswa')
plt.title('Jumlah Mahasiswa per Fakultas')
plt.show()
plt.savefig('plot.png')