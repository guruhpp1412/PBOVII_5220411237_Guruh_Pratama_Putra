import mysql.connector

class Evangelion:
    def __init__(self, id_corp, nama_corp):
        self.id_corp = id_corp
        self.nama_corp = nama_corp
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='5220411237'
        )
        self.cursor = self.connection.cursor()

    def tambah_eva(self):
        self.cursor.execute('''
            INSERT INTO evangelion (id_corp, nama_corp)
            VALUES (%s, %s)
        ''', (self.id_corp, self.nama_corp))
        self.connection.commit()
        print("Data Berhasil Ditambahkan")
    
    def tampilkan_data_eva(self):
        self.cursor.execute('SELECT * FROM evangelion')
        return self.cursor.fetchall()
    
    def cari_eva(self, id):
        self.cursor.execute('SELECT * FROM evangelion WHERE id_corp = %s', (id,))
        print(f'\nEva dengan id {id}:' )
        return self.cursor.fetchone()
    
    def update_eva(self):
        self.cursor.execute('''
            UPDATE evangelion
            SET nama_corp=%s
            WHERE id_corp=%s
        ''', (self.nama_corp, self.id_corp))
        self.connection.commit()
        print("Data Berhasil Diupdate")
    
    def hapus_eva(self, id):
        self.cursor.execute('DELETE FROM evangelion WHERE id_corp = %s', (id,))
        self.connection.commit()
        print("Berhasil Dihapus")

class Pilot(Evangelion):
    def __init__(self, id_corp, nama_corp, id_pilot, nama_pilot, umur, asal_pilot):
        super().__init__(id_corp, nama_corp)
        self.id_pilot = id_pilot
        self.nama_pilot = nama_pilot
        self.umur = umur
        self.asal_pilot = asal_pilot
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='5220411237'
        )
        self.cursor = self.connection.cursor()
    
    def tambah_pilot(self):
        self.cursor.execute('''
            INSERT INTO pilot (id_pilot, nama_pilot, umur, asal_pilot)
            VALUES (%s, %s, %s, %s)
        ''', (self.id_pilot, self.nama_pilot, self.umur, self.asal_pilot))
        self.connection.commit()
        print("Data Berhasil Ditambahkan")
    
    def tampilkan_data_pilot(self):
        self.cursor.execute('SELECT * FROM pilot')
        return self.cursor.fetchall()
    
    def cari_pilot(self, id):
        self.cursor.execute('SELECT * FROM pilot WHERE id_pilot = %s', (id,))
        print(f'\nPilot dengan id {id}:' )
        return self.cursor.fetchone()
    
    def update_pilot(self):
        self.cursor.execute('''
            UPDATE pilot
            SET nama_pilot=%s, umur=%s, asal_pilot=%s
            WHERE id_pilot=%s
        ''', (self.nama_pilot, self.umur, self.asal_pilot, self.id_pilot))
        self.connection.commit()
        print("Data Berhasil Diupdate")
    
    def hapus_pilot(self, id):
        self.cursor.execute('DELETE FROM pilot WHERE id_pilot = %s', (id,))
        self.connection.commit()
        print("Berhasil Dihapus")
    

class Unit(Pilot):
    def __init__(self, id_corp, nama_corp, id_pilot, nama_pilot, umur, asal_pilot, id_unit, nama_unit, asal_unit):
        super().__init__(id_corp, nama_corp, id_pilot, nama_pilot, umur, asal_pilot)
        self.id_unit = id_unit
        self.nama_unit = nama_unit
        self.asal_unit = asal_unit
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='5220411237'
        )
        self.cursor = self.connection.cursor()
    
    def tambah_unit(self):
        self.cursor.execute('''
            INSERT INTO unit (id_unit, nama_unit, asal_unit)
            VALUES (%s, %s, %s)
        ''', (self.id_unit, self.nama_unit, self.asal_unit))
        self.connection.commit()
        print("Data Berhasil Ditambahkan")
    
    def tampilkan_data_unit(self):
        self.cursor.execute('SELECT * FROM unit')
        return self.cursor.fetchall()
    
    def cari_unit(self, id):
        self.cursor.execute('SELECT * FROM unit WHERE id_unit = %s', (id,))
        print(f'\nUnit dengan id {id}:' )
        return self.cursor.fetchone()
    
    def update_unit(self):
        self.cursor.execute('''
            UPDATE unit
            SET nama_unit=%s, asal_unit=%s
            WHERE id_unit=%s
        ''', (self.nama_unit, self.asal_unit, self.id_unit))
        self.connection.commit()
        print("Data Berhasil Diupdate")
    
    def hapus_unit(self, id):
        self.cursor.execute('DELETE FROM unit WHERE id_unit = %s', (id,))
        self.connection.commit()
        print("Berhasil Dihapus")

eva1 = Evangelion(21132, "Nerv Antartika")
plt1 = Pilot(21132, "Nerv Antartika", 534, "Ikari Gendo", 50, "Jepang")
unt1 = Unit(21132, "Nerv Antartika", 534, "Ikari Gendou", 50, "Jepang", 11, "EVA-11", "Jepang")

print("TAMPILKAN SELURUH DATA PADA TIAP TABEL")
semua_eva = eva1.tampilkan_data_eva()
print('Semua Eva:')
for eva in semua_eva:
    print(eva)

semua_pilot = plt1.tampilkan_data_pilot()
print('\nSemua Pilot:')
for plt in semua_pilot:
    print(plt)

semua_unit = unt1.tampilkan_data_unit()
print('\nSemua Unit:')
for unt in semua_unit:
    print(unt)

print("\nINSERT DATA PADA TIAP TABEL")
eva1.tambah_eva()

plt1.tambah_pilot()

unt1.tambah_unit()

print("\nTAMPILKAN SELURUH DATA PADA TIAP TABEL (Setelah Insert)")
semua_eva = eva1.tampilkan_data_eva()
print('Semua Eva:')
for eva in semua_eva:
    print(eva)

semua_pilot = plt1.tampilkan_data_pilot()
print('\nSemua Pilot:')
for plt in semua_pilot:
    print(plt)

semua_unit = unt1.tampilkan_data_unit()
print('\nSemua Unit:')
for unt in semua_unit:
    print(unt)

print("\nMENCARI DATA PADA TIAP TABEL")
eva_cari = eva1.cari_eva(12345)
print(eva_cari)

pilot_cari = plt1.cari_pilot(146)
print(pilot_cari)

unit_cari = unt1.cari_unit(1)
print(unit_cari)

print("\nUPDATE DATA PADA TIAP TABEL")
eva1.nama_corp = 'Nerv Green Land'
eva1.update_eva()

plt1.nama_pilot = 'Ikari Gendou'
plt1.update_pilot()

unt1.nama_unit = 'EVA-X'
unt1.update_unit()

print("\nTAMPILKAN SELURUH DATA PADA TIAP TABEL (Setelah Update)")
semua_eva = eva1.tampilkan_data_eva()
print('Semua Eva:')
for eva in semua_eva:
    print(eva)

semua_pilot = plt1.tampilkan_data_pilot()
print('\nSemua Pilot:')
for plt in semua_pilot:
    print(plt)

semua_unit = unt1.tampilkan_data_unit()
print('\nSemua Unit:')
for unt in semua_unit:
    print(unt)

print("\nHAPUS DATA BERDASARKAN ID")
eva1.hapus_eva(21132)
plt1.hapus_pilot(534)
unt1.hapus_unit(11)

print("\nTAMPILKAN SELURUH DATA PADA TIAP TABEL (Setelah Delete)")
semua_eva = eva1.tampilkan_data_eva()
print('Semua Eva:')
for eva in semua_eva:
    print(eva)

semua_pilot = plt1.tampilkan_data_pilot()
print('\nSemua Pilot:')
for plt in semua_pilot:
    print(plt)

semua_unit = unt1.tampilkan_data_unit()
print('\nSemua Unit:')
for unt in semua_unit:
    print(unt)