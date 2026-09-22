class AlatLukis:
    nama_toko = "Toko Perlengkapan Seni Terapan"
    total_jenis_barang = 0
    kategori_tersedia = ["Cat", "Kuas", "Medium", "Kertas", "Lainnya"]

    def __init__(self, kode, nama, kategori, stok, harga):
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.__stok = stok
        self.__harga = harga
        AlatLukis.total_jenis_barang += 1

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, stok_baru):
        if not isinstance(stok_baru, int) or stok_baru < 0:
            print(f"[X] Gagal ubah stok {self.nama}: Stok harus berupa angka dan tidak boleh negatif!")
        else:
            self.__stok = stok_baru
            print(f"[v] Stok {self.nama} berhasil diubah menjadi {self.__stok}.")

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            raise ValueError(f"Harga {self.nama} harus lebih dari 0!")
        self.__harga = harga_baru

    def info_barang(self):
        print(f"[{self.kode}] {self.nama} | Kategori: {self.kategori} | Stok: {self.stok} | Harga: Rp{self.harga}")

    @classmethod
    def dari_dict(cls, data):
        return cls(data['kode'], data['nama'], data['kategori'], data['stok'], data['harga'])

    @staticmethod
    def validasi_kategori(kategori_input):
        return kategori_input in AlatLukis.kategori_tersedia


class Karyawan:
    cabang = "Samarinda"
    total_karyawan = 0
    shift_tersedia = ["Pagi", "Siang", "Malam"]

    def __init__(self, id_karyawan, nama, jabatan, pin):
        self.id_karyawan = id_karyawan
        self.nama = nama
        self.jabatan = jabatan
        self.__pin = pin
        Karyawan.total_karyawan += 1

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin_baru):
        if len(str(pin_baru)) != 6 or not str(pin_baru).isdigit():
            print(f"[X] Gagal ubah PIN {self.nama}: PIN harus persis 6 digit angka!")
        else:
            self.__pin = pin_baru
            print(f"[v] PIN {self.nama} berhasil diperbarui.")

    def info_karyawan(self):
        print(f"Karyawan: {self.nama} ({self.jabatan}) - Cabang {self.cabang}")

    @classmethod
    def ubah_cabang(cls, cabang_baru):
        cls.cabang = cabang_baru
        print(f"[*] Informasi: Seluruh karyawan sekarang dipindahkan ke cabang {cls.cabang}")

    @staticmethod
    def sapaan_toko():
        print(">>> 'Selamat datang di Toko Perlengkapan Seni! Ada yang bisa dibantu?'")


class Pemasok:
    daftar_mitra = []
    total_mitra = 0
    pajak_pembelian = 0.11

    def __init__(self, kode_pemasok, nama_perusahaan, nomor_kontak, saldo_hutang):
        self.kode_pemasok = kode_pemasok
        self.nama_perusahaan = nama_perusahaan
        self.nomor_kontak = nomor_kontak
        self.__saldo_hutang = saldo_hutang
        Pemasok.total_mitra += 1
        Pemasok.daftar_mitra.append(self.nama_perusahaan)

    @property
    def saldo_hutang(self):
        return self.__saldo_hutang

    @saldo_hutang.setter
    def saldo_hutang(self, nominal):
        if nominal < 0:
            print(f"[X] Gagal ubah hutang {self.nama_perusahaan}: Nominal tidak boleh negatif.")
        else:
            self.__saldo_hutang = nominal
            print(f"[v] Saldo hutang {self.nama_perusahaan} di-update menjadi Rp{self.__saldo_hutang}")

    def info_pemasok(self):
        print(f"Mitra: {self.nama_perusahaan} | Kontak: {self.nomor_kontak} | Tagihan: Rp{self.saldo_hutang}")

    @classmethod
    def tampilkan_semua_mitra(cls):
        print(f"Total {cls.total_mitra} Mitra Aktif: {', '.join(cls.daftar_mitra)}")

    @staticmethod
    def validasi_kontak(kontak):
        valid = str(kontak).startswith("08") or str(kontak).startswith("+62")
        status = "Valid" if valid else "Tidak Valid"
        print(f"Pengecekan kontak '{kontak}': {status}")
        return valid


if __name__ == "__main__":
    print("\n" + "="*50)
    print("--- DEMONSTRASI CLASS ALAT LUKIS ---")
    
    barang1 = AlatLukis("AL01", "Gouache Paint Refill 50ml", "Cat", 12, 45000)
    
    data_barang2 = {'kode': 'AL02', 'nama': 'Script Liner Paintbrush', 'kategori': 'Kuas', 'stok': 8, 'harga': 35000}
    barang2 = AlatLukis.dari_dict(data_barang2)
    
    barang1.info_barang()
    barang2.info_barang()
    
    print("\n-- Uji Setter dan Validasi Alat Lukis --")
    barang1.stok = 10
    barang1.stok = -5
    print(f"Kategori 'Cat' valid? {AlatLukis.validasi_kategori('Cat')}")

    print("\n" + "="*50)
    print("--- DEMONSTRASI CLASS KARYAWAN ---")
    kar1 = Karyawan("K01", "Daffa", "Kasir", "123456")
    kar2 = Karyawan("K02", "Sifwah", "Manager Gudang", "654321")
    
    Karyawan.sapaan_toko()
    kar1.info_karyawan()
    
    print("\n-- Uji Setter dan Validasi Karyawan --")
    kar2.pin = "112233"
    kar2.pin = "999"
    
    Karyawan.ubah_cabang("Balikpapan")
    kar1.info_karyawan()

    print("\n" + "="*50)
    print("--- DEMONSTRASI CLASS PEMASOK ---")
    sup1 = Pemasok("P01", "PT Warna Abadi", "08123456789", 500000)
    sup2 = Pemasok("P02", "CV Kuas Nusantara", "021987654", 150000)
    
    sup1.info_pemasok()
    Pemasok.tampilkan_semua_mitra()
    
    print("\n-- Uji Setter dan Validasi Pemasok --")
    sup1.saldo_hutang = 200000
    sup2.saldo_hutang = -50000
    
    Pemasok.validasi_kontak(sup2.nomor_kontak)
    print("="*50 + "\n")