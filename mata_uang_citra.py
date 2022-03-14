# Code ini dibuat dan dimodifikasi untuk pengerjaan Responsi Pengolahan Citra Digital Praktik

import cv2
import matplotlib.pyplot as plt
import numpy as np

# inisialisasi direktori penyimpanan image
image_dir = " "

# membaca data image
image = cv2.imread(image_dir)

# memisahkan matriks B, G, dan R (openCV menggunakan model BGR, bukan RGB)
B, G, R = cv2.split(image)

# hitung tinggi dan lebar image
height = len(image)
width = len(image[0])
tot_pixel = height * width

# Pisahkan ketiga channel agar tinggi pixel dapat dihitung
channel_blue = height
channel_green = height
channel_red = height

# hitung kemunculan tiap nilai pixel pada matrix B, G, dan R
hist_B = np.zeros((256))  # buat histogram untuk B
hist_G = np.zeros((256))  # buat histogram untuk G
hist_R = np.zeros((256))  # buat histogram untuk R

for i in range(height):
    for j in range(width):

        # proses matrix B
        pixel0 = B[i][j]
        hist_B[pixel0] += 1

        # proses matrix G
        pixel1 = G[i][j]
        hist_G[pixel1] += 1

        # proses matrix R
        pixel2 = R[i][j]
        hist_R[pixel2] += 1

        # Proses Menampilkan Pixel Biru
        if pixel0 > pixel1 and pixel0 > pixel2:
            channel_blue += 1

        # Proses Menampilkan Pixel Hijau
        elif pixel1 > pixel0 and pixel1 > pixel2:
            channel_green += 1

        # Proses Menampilkan Pixel Merah
        else:
            channel_red += 1

# tampilkan histogram
plt.bar(range(len(hist_R)), hist_R, color=[1, 0, 0])
plt.bar(range(len(hist_G)), hist_G, color=[0, 1, 0])
plt.bar(range(len(hist_B)), hist_B, color=[0, 0, 1])

# Menampilkan Jumlah pixel dari masing-masing channel warna
print("Total Pixel Biru : ", channel_blue)
print("Total Pixel Hijau : ", channel_green)
print("Total Pixel Merah : ", channel_red)

# dilakukan if statments untuk menentukan jenis nilai mata uangnya
if channel_blue > channel_green and channel_blue > channel_red:
    print("Nilai Uang Adalah 50 Ribu Rupiah")
elif channel_green > channel_blue and channel_green > channel_red:
    print("Nilai Uang Adalah 20 Ribu Rupiah")
else:
    print("Nilai Uang Adalah 100 Ribu Rupiah")

# tutup histogram ketika user menekan sembarang tombol
plt.waitforbuttonpress()
