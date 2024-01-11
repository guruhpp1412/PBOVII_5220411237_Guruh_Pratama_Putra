class Showroom:
    def __init__(self, brend, model, tahun, pajak, harga):
        self.brend = brend
        self.model = model
        self.tahun = tahun
        self.__pajak = pajak
        self.__harga = harga
    
    def jenis(self, roda):
        if roda == 2:
            print("Motor")
        if roda == 4:
            print("Mobil")

    def _engine(self, mesin=None):
        if mesin != "Start" :
            print('Mesin tidak menyala!')
        else:
            print('Mesin telah menyala')

    def driver(self, nama):
        print(f"Nama Driver: {nama}")

    def __hitung_harga(self):
        hitung= self.__pajak + self.__harga
        print(f"Harga dari kendaraan ini adalah Rp{hitung}")
    
    def accessHarga(self):
        self.__hitung_harga()

class Motor(Showroom):
    def __init__(self, brend, model, tahun, pajak, harga, jenis_bensin, jumlah_ban):
        super().__init__(brend, model, tahun, pajak, harga)
        self.__jenis_bensin = jenis_bensin
        self.jumlah_ban = jumlah_ban
    
    def ket_ban(self, jenis):
        print(f"Motor ini memakai ban {jenis} dan jumlahnya ada {self.jumlah_ban}")
    
    def driver(self, nama):
        print(f"Nama Driver: {nama}")

    def _engine(self, standar=None):
        if standar != "Turun" or standar != "turun":
            print('Mesin telah menyala!')
        else:
            print('Mesin tidak menyala!')
    
    def _kecepatan(self, cepat):
        print(f"Kecepatannya bisa sampai {cepat} km/h.")
    
    def tamipilMotor(self):
        print("Brend Motor: ", self.brend,"\nModel Motor: ", self.model,"\nJenis Bensin: ", self.__jenis_bensin)

class Mobil(Showroom):
    def __init__(self, brend, model, tahun, pajak, harga, jumlah_pintu, jenis_bensin):
        super().__init__(brend, model, tahun, pajak, harga)
        self.jumlah_pintu = jumlah_pintu
        self.__jenis_bensin = jenis_bensin

    def ket_kapasitas(self, kapasitas):
        print(f"Mobil ini memiliki {self.jumlah_pintu} pintu dan memiliki kapasitas {kapasitas} orang")
    
    def driver(self, nama):
        print(f"Nama Driver: {nama}")

    def _engine(self, pintu=None):
        if pintu != "Terbuka" or pintu != "terbuka" :
            print('Lampu peringatan tidak menyala!')
        else:
            print('Lampu peringatan menyala!')

    def _kecepatan(self, cepat):
        print(f"Kecepatannya bisa sampai {cepat} km/h.")
    
    def tamipilMobil(self):
        print("Brend Mobil: ", self.brend,"\nModel Mobil: ", self.model,"\nJenis Bensin: ", self.__jenis_bensin)

class ElectricMobil(Mobil):
    def __init__(self, brend, model, tahun, pajak, harga, jumlah_pintu, battery_capacity, volt, jenis_bensin="Listrik"):
        super().__init__(brend, model, tahun, pajak, harga, jumlah_pintu, jenis_bensin)
        self.__battery_capacity = battery_capacity
        self.volt = volt
        self.__jenis_bensin = jenis_bensin

    def __ngecharge_battery(self):
        lamaCharge= self.__battery_capacity / self.volt
        print(f"Lama untuk mengisi daya mobil listrik ini adalah {lamaCharge} menit")
    
    def accessBattery(self):
        self.__ngecharge_battery()
    
    def driver(self, nama):
        print(f"Nama Driver: {nama}")

    def _engine(self, baterai=None):
        if baterai != "Habis" or baterai != "habis" :
            print('Mesin Tidak Bisa Menyala, Harap di Charge!')
        else:
            print('Mesin Bisa Menyala!')

    def _kecepatan(self, cepat):
        print(f"Kecepatan mobil listrik ini bisa sampai {cepat} km/h.")

    def tamipilMobilListrik(self):
        print("Brend Mobil Listrik: ", self.brend,"\nModel Mobil: ", self.model,"\nJenis Bensin: ", self.__jenis_bensin)

def menu():
    print('='*70)
    print("1. Motor")
    print("2. Mobil")
    print("3. Mobil Listrik")
    print("0. Exit Program")
    print('='*70)

def main():
    print("Apakah ingin menjalankan Program?","\nYa/Tidak")
    jawab=str(input(">"))
    while jawab == "Ya" or jawab == "ya":
        menu()
        pilih = int(input("pilih menu: "))
        if pilih == 1:
            nama = str(input("Masukan Nama: "))
            brand = str(input("Masukan Brand: "))
            model = str(input("Masukan Model: "))
            tahun = int(input("Masukan Tahun: "))
            pajak = int(input("Masukan pajak: Rp"))
            harga = int(input("Masukan Harga: Rp"))
            jenis_bensin = str(input("Masukan Jenis Bensin: "))
            jumlah_ban = int(input("Masukan Jumlah Ban: "))
            ket_ban = str(input("Masukkan jenis ban Motor: "))
            mesin = str(input("Status Standar Motor (Turun/Naik): "))
            kec = int(input("Masukan Kecepatan Max: "))
            objek1=Motor(brand, model, tahun, pajak, harga, jenis_bensin, jumlah_ban)
            print('='*70)
            print('*    STRUK PEMBELANJAAN    *')
            print('='*70)
            objek1.driver(nama)
            objek1.tamipilMotor()
            objek1.ket_ban(ket_ban)
            objek1._engine(mesin)
            objek1._kecepatan(kec)
            print('='*70)
            objek11 = Showroom(brand,model, tahun,pajak,harga)
            print("TOTAL"), objek11.accessHarga()
        elif pilih == 2:
            nama = str(input("Masukan Nama: "))
            brand = str(input("Masukan Brand: "))
            model = str(input("Masukan Model: "))
            tahun = int(input("Masukan Tahun: "))
            pajak = int(input("Masukan pajak: Rp"))
            harga = int(input("Masukan Harga: Rp"))
            jenis_bensin = str(input("Masukan Jenis Bensin: "))
            jumlah_pintu = int(input("Masukan Jumlah Ban: "))
            ket_kap = str(input("Masukkan jumlah kapasitas mobil: "))
            mesin = str(input("Status Pintu Mobil (Terbuka/Tertutup): "))
            kec = int(input("Masukan Kecepatan Max: "))
            objek2=Mobil(brand, model, tahun, pajak, harga, jumlah_pintu, jenis_bensin,)
            print('='*70)
            print('*    STRUK PEMBELANJAAN    *')
            print('='*70)
            objek2.driver(nama)
            objek2.tamipilMobil()
            objek2.ket_kapasitas(ket_kap)
            objek2._engine(mesin)
            objek2._kecepatan(kec)
            print('='*70)
            objek22 = Showroom(brand,model, tahun,pajak,harga)
            print("TOTAL"), objek22.accessHarga()
        elif pilih == 3:
            nama = str(input("Masukan Nama: "))
            brand = str(input("Masukan Brand: "))
            model = str(input("Masukan Model: "))
            tahun = int(input("Masukan Tahun: "))
            pajak = int(input("Masukan pajak: Rp"))
            harga = int(input("Masukan Harga: Rp"))
            battery = int(input("Masukan Kapasitas Baterai: "))
            jumlah_pintu = int(input("Masukan Jumlah Ban: "))
            volt = int(input("Masukkan jumlah volt yang dibutuhkan mobil: "))
            mesin = str(input("Status Baterai Mobil (Habis/Full): "))
            kec = int(input("Masukan Kecepatan Max: "))
            objek3=ElectricMobil(brand, model, tahun, pajak, harga, jumlah_pintu, battery, volt)
            print('='*70)
            print('*    STRUK PEMBELANJAAN    *')
            print('='*70)
            objek3.driver(nama)
            objek3.tamipilMobilListrik()
            objek3._engine(mesin)
            objek3.accessBattery()
            objek3._kecepatan(kec)
            print('='*70)
            objek33 = Showroom(brand,model, tahun,pajak,harga)
            print("TOTAL"), objek33.accessHarga()
        else:
            print("Terima Kasih Sudah Menjalankan Program !!")
            break

if __name__ == "__main__":
    main()