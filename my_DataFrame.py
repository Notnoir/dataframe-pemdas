import pandas as pd

file_path = "jumlah-produksi-sampah.csv"  
data = pd.read_csv(file_path)

df = data[['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'tahun']]
print(df)

# Menghitung total produksi sampah untuk tahun tertentu
tahun = 2021
total_produksi = 0

for i, j in df.iterrows():
    if j['tahun'] == tahun:
        total_produksi += j['jumlah_produksi_sampah']
print(f"Total produksi sampah pada tahun {tahun}: {total_produksi:.2f} ton")

# Menghitung total produksi sampah per tahun
total_per_tahun = {}

for i, j in df.iterrows():
    tahun = j['tahun']
    if tahun not in total_per_tahun:
        total_per_tahun[tahun] = 0
    total_per_tahun[tahun] += j['jumlah_produksi_sampah']

print("Total produksi sampah per tahun:")
for tahun, total in total_per_tahun.items():
    print(f"tahun {tahun}: {total:.2f} ton")

# Menghitung total produksi sampah per kota/kabupaten per tahun
kota_per_tahun = {}

for i, j in df.iterrows():
    kota = j['nama_kabupaten_kota']
    tahun = j['tahun']
    if kota not in kota_per_tahun:
        kota_per_tahun[kota] = {}
    if tahun not in kota_per_tahun[kota]:
        kota_per_tahun[kota][tahun] = 0
    kota_per_tahun[kota][tahun] += j['jumlah_produksi_sampah']

print("Total produksi sampah per kota/kabupaten per tahun:")
for kota, data_tahun in kota_per_tahun.items():
    print(f"{kota}:")
    for tahun, total in data_tahun.items():
        print(f"  Tahun {tahun}: {total} ton")

# Ekspor hasil ke CSV dan Excel
df.to_csv('hasil_data.csv', index=False)
df.to_excel('hasil_data.xlsx', index=False)
print("Data berhasil disimpan dalam hasil_data.csv dan hasil_data.xlsx")