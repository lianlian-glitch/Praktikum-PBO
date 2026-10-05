class AlatSeni:
    def __init__(self, kode, nama, stok, harga_modal):
        self.kode = kode
        self.nama = nama
        self._stok = stok
        self.__harga_modal = harga_modal

    def get_harga_jual(self):
        return self.__harga_modal * 1.3 

    def kurangi_stok(self, qty):
        if qty <= self._stok:
            self._stok -= qty
            return True
        return False

    def info(self):
        return f"[{self.kode}] {self.nama} | Stok: {self._stok}"

class CatLukis(AlatSeni):
    def __init__(self, kode, nama, stok, harga_modal, volume_ml, jenis_cat):
        super().__init__(kode, nama, stok, harga_modal)
        self.volume_ml = volume_ml
        self.jenis_cat = jenis_cat

    def info(self):
        status = "Tersedia" if self._stok > 0 else "Habis"
        info_dasar = super().info()
        return f"{info_dasar} | Cat {self.jenis_cat} ({self.volume_ml}ml) - {status}"

class Kuas(AlatSeni):
    def __init__(self, kode, nama, stok, harga_modal, tipe_bulu, ukuran):
        super().__init__(kode, nama, stok, harga_modal)
        self.tipe_bulu = tipe_bulu
        self.ukuran = ukuran

    def info(self):
        info_dasar = super().info()
        return f"{info_dasar} | Kuas {self.tipe_bulu} (Uk: {self.ukuran}) - Harga: Rp{self.get_harga_jual():,.0f}"

class DetailNota:
    def __init__(self, nama_barang, qty, subtotal):
        self.nama_barang = nama_barang
        self.qty = qty
        self.subtotal = subtotal

    def __str__(self):
        return f"{self.nama_barang:<20} x{self.qty} = Rp{self.subtotal:,.0f}"

class Nota:
    def __init__(self, id_nota, nama_pelanggan):
        self.id_nota = id_nota
        self.nama_pelanggan = nama_pelanggan
        self.total = 0
        self._daftar_item = []

    def tambah_item(self, barang, qty):
        if barang.kurangi_stok(qty):
            subtotal = barang.get_harga_jual() * qty
            item = DetailNota(barang.nama, qty, subtotal)
            self._daftar_item.append(item)
            self.total += subtotal
        else:
            print(f"[!] Stok {barang.nama} tidak mencukupi untuk pesanan ini.")

    def cetak_nota(self):
        print(f"\n=== NOTA: {self.id_nota} | Pelanggan: {self.nama_pelanggan} ===")
        for item in self._daftar_item:
            print(f"- {item}")
        print(f"TOTAL BAYAR: Rp{self.total:,.0f}")
        print("==================================================")

class Karyawan:
    def __init__(self, nama, id_karyawan):
        self.nama = nama
        self.id_karyawan = id_karyawan

    def proses_pembayaran(self, nota, uang_bayar):
        print(f"\nKasir {self.nama} (ID: {self.id_karyawan}) memproses pembayaran...")
        nota.cetak_nota()
        if uang_bayar >= nota.total:
            kembalian = uang_bayar - nota.total
            print(f"Status: BERHASIL | Uang: Rp{uang_bayar:,.0f} | Kembalian: Rp{kembalian:,.0f}")
        else:
            print(f"Status: GAGAL | Uang tidak cukup. Kurang Rp{nota.total - uang_bayar:,.0f}")

class Toko:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self._daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self._daftar_karyawan.append(karyawan)
        print(f"[+] Karyawan {karyawan.nama} mulai bekerja di {self.nama_toko}")

if __name__ == "__main__":
    toko_seni = Toko("Toko Perlengkapan Seni Terapan")
    
    kasir1 = Karyawan("Daffa", "K-001")
    kasir2 = Karyawan("Sifwah", "K-002")
    
    toko_seni.tambah_karyawan(kasir1)
    toko_seni.tambah_karyawan(kasir2)

    cat1 = CatLukis("AL01", "Gouache Paint Set", 10, 80000, 50, "Gouache")
    kuas1 = Kuas("AL02", "Script Liner", 5, 25000, "Sintetis", 2)
    kuas2 = Kuas("AL03", "Flat Brush", 0, 30000, "Kolinsky", 6)

    print("\n--- INFO STOK BARANG ---")
    print(cat1.info())
    print(kuas1.info())
    print(kuas2.info())

    nota_budi = Nota("TRX-001", "Budi Santoso")
    
    nota_budi.tambah_item(cat1, 2)
    nota_budi.tambah_item(kuas1, 3)
    nota_budi.tambah_item(kuas2, 1)

    kasir1.proses_pembayaran(nota_budi, 300000)

    print("\n--- INFO STOK BARANG SETELAH TRANSAKSI ---")
    print(cat1.info())
    print(kuas1.info())