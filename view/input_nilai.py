def input_data(data):
    nama = input("Masukkan Nama : ")
    
    while len(nama) < 3:
        nama = input("Masukkan Nama : ")
        
    while nama in data['nama']:
        print("Mahasiswa dengan nama yang sudah ada")
        nama = input("Masukkan Nama : ")
        
    nilai = input("Masukkan Nilai : ")
    while not nilai.isnumeric():
        nilai = input("Masukkan Nilai : ")
        
    data['nama'].append(nama)
    data['nilai'].append(int(nilai))
    print("Data Berhasil ditambah!")
    return data    