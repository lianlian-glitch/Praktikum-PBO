from abc import ABC, abstractmethod

class AlatSeni(ABC):
    def __init__(self, kode, nama, stok, harga_modal):
        self.kode = kode
        self.nama = nama
        self._stok = stok
        self.__harga_modal = harga_modal

    @abstractmethod
    def hitung_harga_jual(self):
        pass

    @abstractmethod
    def info_spesifik(self):
        pass

    def get_harga_modal(self):
        return self.__harga_modal

    def kurangi_stok(self, qty):
        if qty <= self._stok:
            self._stok -= qty
            return True
        return False

class CatLukis(AlatSeni):
    def __init__(self, kode, nama, stok, harga_modal, volume_ml, jenis_cat):
        super().__init__(kode, nama, stok, harga_modal)
        self.volume_ml = volume_ml
        self.jenis_cat = jenis_cat

    def hitung_harga_jual(self):
        return self.get_harga_modal() * 1.3

    def info_spesifik(self):
        return f"Cat {self.jenis_cat} | {self.volume_ml}ml"

    def __str__(self):
        return f"[{self.kode}] {self.nama} ({self.info_spesifik()}) - Rp{self.hitung_harga_jual():,.0f}"

class Kuas(AlatSeni):
    def __init__(self, kode, nama, stok, harga_modal, tipe_bulu, ukuran):
        super().__init__(kode, nama, stok, harga_modal)
        self.tipe_bulu = tipe_bulu
        self.ukuran = ukuran

    def hitung_harga_jual(self):
        return self.get_harga_modal() * 1.4

    def info_spesifik(self):
        return f"Kuas {self.tipe_bulu} | Uk: {self.ukuran}"

    def __str__(self):
        return f"[{self.kode}] {self.nama} ({self.info_spesifik()}) - Rp{self.hitung_harga_jual():,.0f}"

class PembayaranTunai:
    def proses_bayar(self, nominal):
        print(f"Menerima pembayaran TUNAI sebesar Rp{nominal:,.0f}")
        return True

class PembayaranQRIS:
    def proses_bayar(self, nominal):
        print(f"Memproses pembayaran QRIS wondr by BNI sebesar Rp{nominal:,.0f}...")
        return True

def eksekusi_pembayaran(metode_pembayaran, nominal):
    metode_pembayaran.proses_bayar(nominal)

class DetailNota:
    def __init__(self, nama_barang, qty, subtotal):
        self.nama_barang = nama_barang
        self.qty = qty
        self.subtotal = subtotal

    def __add__(self, other):
        return self.subtotal + other.subtotal

    def __str__(self):
        return f"{self.nama_barang:<24} x{self.qty} = Rp{self.subtotal:,.0f}"

class Nota:
    def __init__(self, id_nota, nama_pelanggan):
        self.id_nota = id_nota
        self.nama_pelanggan = nama_pelanggan
        self.total = 0
        self._daftar_item = []

    def tambah_item(self, barang, qty):
        if barang.kurangi_stok(qty):
            subtotal = barang.hitung_harga_jual() * qty
            item = DetailNota(barang.nama, qty, subtotal)
            self._daftar_item.append(item)
            self.total += subtotal
        else:
            print(f"[!] Stok {barang.nama} tidak mencukupi.")

    def cetak_nota(self):
        print(f"\n=== NOTA: {self.id_nota} | Pelanggan: {self.nama_pelanggan} ===")
        for item in self._daftar_item:
            print(f"- {item}")
        print(f"TOTAL: Rp{self.total:,.0f}")

class Karyawan:
    def __init__(self, nama, id_karyawan):
        self.nama = nama
        self.id_karyawan = id_karyawan

    def proses_transaksi(self, nota, metode_pembayaran):
        print(f"\nKasir {self.nama} memproses transaksi...")
        nota.cetak_nota()
        eksekusi_pembayaran(metode_pembayaran, nota.total)

class Toko:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self._daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self._daftar_karyawan.append(karyawan)

if __name__ == "__main__":
    try:
        barang_invalid = AlatSeni("A00", "Barang Abstrak", 10, 50000)
    except TypeError as e:
        print("\n[BUKTI ABSTRAKSI]")
        print(f"Error instansiasi Abstract Class:\n{e}\n")

    cat1 = CatLukis("AL01", "Gouache Paint Refill 50ml", 12, 45000, 50, "Gouache")
    kuas1 = Kuas("AL02", "Script Liner Paintbrush", 8, 35000, "Sintetis", 2)

    print("--- POLIMORFISME VIA PEWARISAN ---")
    daftar_barang = [cat1, kuas1]
    for barang in daftar_barang:
        print(barang)

    toko = Toko("Toko Perlengkapan Seni Terapan")
    kasir = Karyawan("Daffa", "K-001")
    toko.tambah_karyawan(kasir)

    nota_intan = Nota("TRX-001", "Intan")
    nota_intan.tambah_item(cat1, 2)
    nota_intan.tambah_item(kuas1, 1)

    print("\n--- OPERATOR OVERLOADING (__add__) ---")
    if len(nota_intan._daftar_item) >= 2:
        item_pertama = nota_intan._daftar_item[0]
        item_kedua = nota_intan._daftar_item[1]
        kombinasi_harga = item_pertama + item_kedua
        print(f"Total penggabungan 2 subtotal item via magic method: Rp{kombinasi_harga:,.0f}")

    print("\n--- DUCK TYPING & TRANSAKSI ---")
    qris = PembayaranQRIS()
    kasir.proses_transaksi(nota_intan, qris)

    tunai = PembayaranTunai()
    kasir.proses_transaksi(nota_intan, tunai)