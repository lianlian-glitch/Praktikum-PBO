# Laporan Posttest Praktikum PBO

**Nama:** Nur Fitri Ramadhani  
**NIM:** 2509106089  
**Kelas:** Informatika B'25  
**Tema:** Sistem Pengelolaan Stok Perlengkapan Seni Rupa Terapan di Toko Alat Tulis  

---

## 1. Penjelasan Program
Program ini adalah purwarupa sistem manajemen inventaris untuk sebuah toko perlengkapan seni rupa terapan. Sistem ini dirancang menggunakan paradigma Pemrograman Berorientasi Objek (PBO) dengan bahasa Python untuk mengelola tiga entitas utama yang saling berinteraksi di dalam operasional toko, yaitu data barang fisik (Alat Lukis), data staf (Karyawan), dan data mitra penyuplai barang (Pemasok). 

Program ini mengimplementasikan konsep fundamental OOP dari Modul 1 hingga Modul 3, termasuk pendefinisian *Class* & *Object*, penggunaan berbagai jenis *Method* (*Instance, Class, Static*), serta pengamanan data sensitif menggunakan *Encapsulation* (Getter & Setter).

## 2. Struktur Class
Sistem ini terdiri dari 3 *class* utama yang berdiri sendiri:

### A. Class `AlatLukis`
Berfungsi untuk mendata dan mengelola informasi barang jualan.
* **Atribut Kelas:** `nama_toko`, `total_jenis_barang`, `kategori_tersedia`.
* **Atribut Instance:** `kode`, `nama`, `kategori` (Public), serta `__stok` dan `__harga` (Private).
* **Method:** 
  * `info_barang(self)`: Instance method untuk menampilkan rincian barang.
  * `dari_dict(cls, data)`: Class method (Factory) untuk merakit objek dari tipe data dictionary.
  * `validasi_kategori(kategori_input)`: Static method untuk mengecek ketersediaan kategori barang di toko.

### B. Class `Karyawan`
Berfungsi untuk mengelola data staf dan mengontrol keamanan akses lewat sistem PIN.
* **Atribut Kelas:** `cabang`, `total_karyawan`, `shift_tersedia`.
* **Atribut Instance:** `id_karyawan`, `nama`, `jabatan` (Public), dan `__pin` (Private).
* **Method:** 
  * `info_karyawan(self)`: Instance method untuk mencetak data staf.
  * `ubah_cabang(cls, cabang_baru)`: Class method untuk merubah atribut kelas (lokasi cabang) secara global.
  * `sapaan_toko()`: Static method untuk mencetak teks sapaan standar toko kepada pelanggan.

### C. Class `Pemasok`
Berfungsi untuk melacak mitra *supplier* dan mencatat tagihan hutang toko.
* **Atribut Kelas:** `daftar_mitra`, `total_mitra`, `pajak_pembelian`.
* **Atribut Instance:** `kode_pemasok`, `nama_perusahaan`, `nomor_kontak` (Public), dan `__saldo_hutang` (Private).
* **Method:** 
  * `info_pemasok(self)`: Instance method untuk menampilkan rincian mitra.
  * `tampilkan_semua_mitra(cls)`: Class method untuk mencetak daftar nama seluruh mitra yang bekerjasama.
  * `validasi_kontak(kontak)`: Static method untuk memvalidasi apakah nomor telepon diawali dengan "08" atau "+62".

## 3. Penerapan Encapsulation & Validasi Data
Sistem ini mengamankan data sensitif menggunakan atribut *private* (awalan `__`) dan menjembataninya dengan *decorator* idiomatis Python:
* **Getter (`@property`):** Digunakan untuk membaca nilai atribut *private* (seperti `stok`, `pin`, `saldo_hutang`).
* **Setter (`@nama.setter`):** Digunakan untuk mengubah nilai dengan menyertakan perlindungan validasi:
  * **Stok & Hutang:** Dilarang menggunakan angka negatif.
  * **Harga:** Dilarang diisi 0 atau kurang dari 0 (menggunakan `raise ValueError`).
  * **PIN:** Dibatasi harus persis 6 digit dan hanya boleh berisi karakter angka.

## 4. Panduan Pengujian (Cara Run)
Untuk mendemonstrasikan berjalannya seluruh persyaratan tugas, ikuti langkah berikut:

1. Pastikan perangkat Anda sudah terinstal Python 3.x.
2. Unduh atau *clone* *repository* ini.
3. Buka terminal atau Command Prompt pada direktori tempat file disimpan.
4. Jalankan perintah eksekusi berikut:
   ```bash
   python 2509106089-NurFitriRamadhani-PT1.py