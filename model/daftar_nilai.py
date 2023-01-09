from tabulate import tabulate
from view import input_nilai
from view import view_nilai

def tambah_data(data):
    newData = input_nilai.input_data(data)
    return data

def hapus_data(data, nama):
    if nama in data['nama']:
        
        dataMhs = {}
        index = data['nama'].index(nama)
        
        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])
        print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))
        confirm = input("anda yakin ingin menghapus data ini? (y/t)")
        
        while (confirm not in ['y', 't']):
            print("input salah")
            confirm = input("anda yakin ingin menghapus data ini? (y/t)")
            
        if confirm == "y":
            for key in data.keys():
                data[key].pop(index)
            print("data berhasil diapus\n")
        return data
    
    else:
        print("data tidak ditemukan")
        
def ubah_data(data, nama):
    if nama in data['nama']:
        dataMhs = {}
        index = data['nama'].index(nama)
        
        for key in data.keys():
            dataMhs[key] =[]
            dataMhs[key].append(data[key][index])
        print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))
        pilihan = input("pilih field yang akan diubah : \n1.Nama\n2.Nilai\n")
        
        match int(pilihan):
            case 1:
                print("data nama sebelumnya : " + dataMhs['nama'][0])
                nama = input("masukkan nama baru : ")
                while nama in data['nama']:
                    if nama == dataMhs['nama'][0]:
                        break
                    print("data mahasiswa dengan nama yang sama udah ada")
                    nama = input("masukkan nama baru")
                data['nama'][index] = nama
            case 2:
                print("data nilai sebelumnya : " , dataMhs['nilai'][0])
                nilai = input("masukkan nilai baru : ")
                data['nilai'][index] = nilai
                
        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])
        print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))
        return data
    else:
        print("data tidak ditemukan")
        
def cari_data(data, nama):
    dataMhs = {}
    if nama in data['nama']:
        index = data['nama'].index(nama)
        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])
        view_nilai.cetak_hasil_pencarian(dataMhs)
    else:
        print("data tidak ditemukan")
        
    