import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Tampilkan citra asli
img_bgr = cv2.imread('Gambar1.jpeg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 2. Konversi grayscale
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# 4. Tingkatkan brightness (tambah offset iluminasi)
brightness_value = 45
img_bright = cv2.add(img_gray, brightness_value)

# 5. Tingkatkan contrast (scaling alpha)
contrast_alpha = 1.4
img_contrast = cv2.convertScaleAbs(img_gray, alpha=contrast_alpha, beta=0)

# 6. Histogram equalization
img_eq = cv2.equalizeHist(img_gray)

# 7. Thresholding (Otsu / Global T=127, di sini pakai Otsu untuk hasil adaptif optimal)
ret_otsu, img_binary = cv2.threshold(
    img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
print(f'Threshold otomatis (Otsu) terpilih: {ret_otsu}')

# Visualisasi dan simpan 9 grid/plot pendukung
fig = plt.figure(figsize=(14, 10))

# 1. Citra Asli
ax1 = fig.add_subplot(3, 3, 1)
ax1.imshow(img_rgb)
ax1.set_title('1. Citra Asli (RGB)')
ax1.axis('off')

# 2. Grayscale
ax2 = fig.add_subplot(3, 3, 2)
ax2.imshow(img_gray, cmap='gray')
ax2.set_title('2. Grayscale')
ax2.axis('off')

# 3. Histogram Asli/Grayscale
ax3 = fig.add_subplot(3, 3, 3)
ax3.hist(img_gray.ravel(), 256, [0, 256], color='black')
ax3.set_title('3. Histogram Grayscale')
ax3.set_xlim([0, 256])

# 4. Brightness Enhancement
ax4 = fig.add_subplot(3, 3, 4)
ax4.imshow(img_bright, cmap='gray')
ax4.set_title(f'4. Brightness (+{brightness_value})')
ax4.axis('off')

# 5. Contrast Enhancement
ax5 = fig.add_subplot(3, 3, 5)
ax5.imshow(img_contrast, cmap='gray')
ax5.set_title(f'5. Contrast (x{contrast_alpha})')
ax5.set_xlim([0, 256])
# Perbaikan tampilkan gambar kontras murni
ax5.imshow(img_contrast, cmap='gray')

# 6. Histogram Equalization (Gambar hasil)
ax6 = fig.add_subplot(3, 3, 6)
ax6.imshow(img_eq, cmap='gray')
ax6.set_title('6. Hasil Hist Equalization')
ax6.axis('off')

# Histogram dari hasil Equalization
ax7 = fig.add_subplot(3, 3, 7)
ax7.hist(img_eq.ravel(), 256, [0, 256], color='blue')
ax7.set_title('Hist Sesudah Equalization')
ax7.set_xlim([0, 256])

# 7. Citra Biner
ax8 = fig.add_subplot(3, 3, 8)
ax8.imshow(img_binary, cmap='gray')
ax8.set_title(f'7. Citra Biner (T={ret_otsu})')
ax8.axis('off')

plt.tight_layout()
plt.savefig('output_tugas_enhancement.png', dpi=300)
plt.show()