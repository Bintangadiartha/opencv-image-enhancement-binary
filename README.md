# Pengolahan Citra Digital - Image Enhancement & Binarization

Repository ini berisi kode implementasi tugas mata kuliah Pengolahan Citra Digital (PCD) yang berfokus pada teknik **Image Enhancement**, **Histogram Equalization**, dan **Thresholding** menggunakan OpenCV di Python.

## Deskripsi Proyek
Skrip `enhancement_binary.py` melakukan serangkaian pemrosesan pada citra asli untuk menganalisis dan meningkatkan kualitas visualnya, serta memisahkan objek dari latar belakang.

Proses yang dilakukan meliputi:
1. **Konversi Grayscale**: Mengubah citra RGB menjadi skala keabuan.
2. **Visualisasi Histogram**: Menampilkan distribusi intensitas piksel asli.
3. **Brightness Enhancement**: Meningkatkan tingkat kecerahan citra secara global.
4. **Contrast Enhancement**: Mempertegas perbedaan antara area gelap dan terang.
5. **Histogram Equalization**: Meratakan distribusi intensitas cahaya untuk mengekspos detail yang tersembunyi.
6. **Otsu Thresholding**: Mengonversi citra menjadi biner (hitam putih) menggunakan pencarian nilai ambang batas (*threshold*) optimal secara otomatis.

## Struktur Repositori
- `Gambar1.jpeg`: Citra asli yang digunakan sebagai objek uji.
- `enhancement_binary.py`: Skrip utama pemrosesan citra.
- `output_tugas_enhancement.png`: Hasil plot grid 3x3 yang memvisualisasikan perbandingan setiap tahapan pemrosesan.

## Prasyarat Lingkungan
Pastikan library Python berikut telah terinstal sebelum menjalankan skrip:
- `opencv-python`
- `matplotlib`
- `numpy`

Instalasi melalui pip:
```bash
pip install opencv-python matplotlib numpy
