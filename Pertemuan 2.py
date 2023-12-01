def matkul():
    print("============================================")
    print("                 MATA KULIAH                ")
    print('============================================')
    print('1. Algoritma Pemrograman' )
    print('2. Struktur dan Basis Data')
    print('3. Teknolog Berbasis Objek')
    print('4. Metodelogi Desain Perangkat Lunak')
    print('5. Pemrograman Berbasis Objek')
    print('6. Coding Machine Learning')

def info():
    print("============================================")
    print("INFO")
    print("Kalau 3,5 - 4,0 = 6 Matkul")
    print("Kalau 3,0 - 3,49 = 4 Matkul")
    print("Kalau 2,5 - 2,99 = 3 Matkul")
    print("Kalau  0 - 2,4 = 2 Matkul")
    print("============================================")
    
def sistem():
    nama=str(input('Nama    : '))
    nim=int(input('NIM      : '))
    ipk=float(input('Nilai IPK: '))
    info()
    if (3.5<= ipk <=4.0):
        i=0
        m=[]
        while i < 6:
            matkul()
            i += 1
            pilih=int(input('Pilih Matkulnya: '))
            if pilih == 1:
                matkul1="Algoritma Pemrograman"
                m.append(matkul1)
                continue
            elif pilih == 2:
                matkul2="Struktur dan Basis Data"
                m.append(matkul2)
                continue
            elif pilih == 3:
                matkul3="Teknolog Berbasis Objek"
                m.append(matkul3)
                continue
            elif pilih == 4:
                matkul4="Metodelogi Desain Perangkat Lunak"
                m.append(matkul4)
                continue
            elif pilih == 5:
                matkul5="Pemrograman Berbasis Objek"
                m.append(matkul5)
                continue
            elif pilih == 6:
                matkul6="Coding Machine Learning"
                m.append(matkul6)
                continue
            else:
                print('Error')
        print("\nMatkul Anda!")
        print(m)
        print("Terima Kasih")
        
    elif (3.0<= ipk <=3.49):
        i=0
        m=[]
        while i < 4:
            matkul()
            i += 1
            pilih=int(input('Pilih Matkulnya: '))
            if pilih == 1:
                matkul1="Algoritma Pemrograman"
                m.append(matkul1)
                continue
            elif pilih == 2:
                matkul2="Struktur dan Basis Data"
                m.append(matkul2)
                continue
            elif pilih == 3:
                matkul3="Teknolog Berbasis Objek"
                m.append(matkul3)
                continue
            elif pilih == 4:
                matkul4="Metodelogi Desain Perangkat Lunak"
                m.append(matkul4)
                print(m)
                continue
            elif pilih == 5:
                matkul5="Pemrograman Berbasis Objek"
                m.append(matkul5)
                continue
            elif pilih == 6:
                matkul6="Coding Machine Learning"
                m.append(matkul6)
                continue
            else:
                print('Error')
        print("\nMatkul Anda!")
        print(m)
        print("Terima Kasih")
        
    elif (2.5<= ipk <=2.99):
        i=0
        m=[]
        while i < 3:
            matkul()
            i += 1
            pilih=int(input('Pilih Matkulnya: '))
            if pilih == 1:
                matkul1="Algoritma Pemrograman"
                m.append(matkul1)
                print(m)
                continue
            elif pilih == 2:
                matkul2="Struktur dan Basis Data"
                m.append(matkul2)
                print(m)
                continue
            elif pilih == 3:
                matkul3="Teknolog Berbasis Objek"
                m.append(matkul3)
                print(m)
                continue
            elif pilih == 4:
                matkul4="Metodelogi Desain Perangkat Lunak"
                m.append(matkul4)
                print(m)
                continue
            elif pilih == 5:
                matkul5="Pemrograman Berbasis Objek"
                m.append(matkul5)
                print(m)
                continue
            elif pilih == 6:
                matkul6="Coding Machine Learning"
                m.append(matkul6)
                print(m)
                continue
            else:
                print('Error')
        print("\nMatkul Anda!")
        print(m)
        print("Terima Kasih")
        
    elif (ipk <=2.5):
        i=0
        m=[]
        while i < 2:
            matkul()
            i += 1
            pilih=int(input('Pilih Matkulnya: '))
            if pilih == 1:
                matkul1="Algoritma Pemrograman"
                m.append(matkul1)
                print(m)
                continue
            elif pilih == 2:
                matkul2="Struktur dan Basis Data"
                m.append(matkul2)
                print(m)
                continue
            elif pilih == 3:
                matkul3="Teknolog Berbasis Objek"
                m.append(matkul3)
                print(m)
                continue
            elif pilih == 4:
                matkul4="Metodelogi Desain Perangkat Lunak"
                m.append(matkul4)
                print(m)
                continue
            elif pilih == 5:
                matkul5="Pemrograman Berbasis Objek"
                m.append(matkul5)
                print(m)
                continue
            elif pilih == 6:
                matkul6="Coding Machine Learning"
                m.append(matkul6)
                print(m)
                continue
            else:
                print('Error')
        print("\nMatkul Anda!")
        print(m)
        print("Terima Kasih")
    else:
        print('Error')
sistem()      