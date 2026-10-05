# Laporan Posttest Praktikum PBO (Relasi UML & Inheritance)

**Nama:** Nur Fitri Ramadhani  
**NIM:** 2509106089  
**Kelas:** Informatika B'25  
**Tema:** Sistem Pengelolaan Stok Perlengkapan Seni Rupa Terapan di Toko Alat Tulis  

---

## 1. Penjelasan Program
Program ini merupakan pengembangan dari sistem pengelolaan inventaris toko alat seni terapan dengan menerapkan empat jenis hubungan antar kelas, yaitu Asosiasi, Agregasi, Komposisi, dan Pewarisan (Inheritance). Program mensimulasikan alur operasional di mana Karyawan yang bekerja di Toko dapat memproses transaksi pembelian (Nota) berisi berbagai macam Alat Seni (seperti Cat Lukis dan Kuas).

## 2. Penerapan Relasi UML
Program ini mengimplementasikan tiga relasi UML yang menghubungkan objek dengan objek[cite: 66]:
1. **Asosiasi ("Menggunakan"):** Terjadi pada method `proses_pembayaran` di class `Karyawan`. Objek `Nota` diterima sebagai parameter (dilewatkan dari luar) untuk diproses, tanpa adanya kepemilikan permanen antara Karyawan dan Nota[cite: 66].
2. **Agregasi ("Memiliki"):** Terjadi antara class `Toko` dan `Karyawan`. Objek `Karyawan` dibuat secara mandiri di luar class induknya, lalu dikirim ke penampung (list `_daftar_karyawan`) milik objek `Toko`[cite: 66]. Jika objek Toko dihapus, Karyawan tetap ada di memori.
3. **Komposisi ("Terdiri dari"):** Terjadi antara class `Nota` dan `DetailNota`. Objek `DetailNota` tidak memiliki arti mandiri dan dibuat langsung di dalam method `tambah_item` milik class `Nota`[cite: 66]. Bagian ini akan ikut musnah bersama Induknya jika Nota dihapus[cite: 66].

## 3. Penerapan Inheritance (Pewarisan)
Pewarisan ("Adalah jenis dari") menghubungkan kelas dengan kelas[cite: 66].
* **Superclass:** `AlatSeni` bertindak sebagai *parent class* yang menurunkan atribut dan method dasarnya.
* **Subclass:** `CatLukis` dan `Kuas` bertindak sebagai *child class* (adalah jenis dari `AlatSeni`).
* **Penggunaan `super().__init__`:** Kedua subclass memanggil konstruktor milik superclass untuk mengisi atribut bawaan (`kode`, `nama`, `stok`, `harga_modal`) tanpa perlu menulisnya ulang.
* **Atribut Tambahan:** Subclass `CatLukis` memiliki atribut unik `volume_ml` dan `jenis_cat`. Subclass `Kuas` memiliki atribut unik `tipe_bulu` dan `ukuran`.
* **Method Overriding:** Subclass mendefinisikan ulang method `info()` milik superclass[cite: 55]. Pada subclass, method ini memodifikasi string kembalian dengan menambahkan detail spesifik masing-masing alat seni dan mengakses logika protected.

## 4. Tingkat Akses (Encapsulation pada Pewarisan)
* **Protected (`_stok`):** Atribut stok pada superclass ditulis menggunakan satu garis bawah. Atribut ini sengaja dibuat *protected* agar subclass (seperti `CatLukis`) dapat mengakses nilainya secara langsung untuk memproses logika tertentu, misalnya menentukan string "Tersedia" atau "Habis" di dalam method `info()`[cite: 62].
* **Private (`__harga_modal`):** Atribut harga beli barang dibuat menggunakan dua garis bawah agar mengalami *name mangling*[cite: 62]. Atribut ini benar-benar rahasia milik superclass dan tidak bisa diakses/dimanipulasi secara langsung, bahkan oleh subclass-nya sendiri[cite: 62].

## 5. Panduan Pengujian (Cara Run)
Untuk mendemonstrasikan keseluruhan alur relasi dan pewarisan sistem, jalankan perintah berikut di terminal:
```bash
python 2509106089-NurFitriRamadhani-PT2.py