from prettytable import PrettyTable
from numpy import *
table = PrettyTable()

judul = input("Masukkan judul kasus : ")
kriteria = []
ketKriteria =[]
subKriteria = []
bobot = []
alternatif = []

def inputKriteria(jumlahKrit):
    for x in range(jumlahKrit):
        kriteria.append(input("Nama kriteria "+str(x+1)+" : "))
        ketKriteria.append(input("Kriteria ini termasuk (untung/rugi) ? "))
        kondisi = input("Apakah kriteria ini mempunyai sub kriteria (y/n) ? ")
        if kondisi == "y":
            jumlahSubKriteria = int(input("Berapa jumlah sub kriteria ? "))
            subKriteriaSementara = []
            for y in range(jumlahSubKriteria):
                subKriteriaSementara.append(input("Masukkan sub kriteria yang ke-"+str(y+1)+" : "))
            subKriteria.append(subKriteriaSementara)
        else:
            subKriteria.append([])

        
def inputBobot(paramBobot):
    for x in range(paramBobot):
        bobot.append(int(input("Masukkan bobot untuk kriteria '"+kriteria[x]+"' (1 - 100) : ")))

def inputAlternatif(jumlahAlt, dataKrit, dataSubKriteria):
    for x in range(jumlahAlt):
        namaAlternatif = input("Nama alternatif ke-"+str(x+1)+"? ")
        nilaiAlternatifSementara = []
        for y in range(len(dataKrit)):
            if dataSubKriteria[y] == []:
                inputNilai = int(input("Masukkan nilai '"+dataKrit[y]+"' : "))
                nilaiAlternatifSementara.append(inputNilai)
            else:
                inputNilai = input("Masukkan nilai "+str(dataSubKriteria[y])+" : ")
                nilaiAlternatifSementara.append(dataSubKriteria[y].index(inputNilai)+1)
        alternatif.append([namaAlternatif, nilaiAlternatifSementara])
                
        
jumlahKriteria = int(input("Berapa kriteria yang ingin anda masukkan? "))
inputKriteria(jumlahKriteria)
inputBobot(len(kriteria))
jumlahAlternatif = int(input("Berapa jumlah alternatif yang ingin anda masukkan? "))
inputAlternatif(jumlahAlternatif, kriteria, subKriteria)



# tabel nilai alternatif
title = ["Alternatif"]
for item in kriteria:
    title.append(item)
table.field_names = title

for x in range(len(alternatif)):
    content = []
    content.append(alternatif[x][0])
    for y in alternatif[x][1]:
        content.append(y)
    table.add_row(content)
print("============================")
print("tabel nilai alternatif")
print(table)

# normalisasi
matrix = []
for baris in range(len(alternatif)):
    matrixSementara = []
    for kolom in range(len(kriteria)):
        r = alternatif[baris][1][kolom]
        nilaiBagi = []
        for x in range(len(alternatif)):
            nilaiBagiSementara = alternatif[x][1][kolom]
            nilaiBagi.append(nilaiBagiSementara)
        if ketKriteria[kolom] == "untung":
            hasil = r/max(nilaiBagi)
        else :
            hasil = min(nilaiBagi)/r
        matrixSementara.append(hasil)
    matrix.append(matrixSementara)

print("============================")
print("hasil matrix normalisasi")
tampilanMatrix = reshape(matrix, (len(matrix), len(matrix[0])))
print(tampilanMatrix)

# perankingan
print("============================")
print("hasil perankingan")
ranking = []
for baris in range(len(matrix)):
    nilai = 0
    nilaiPerBaris = []
    for kolom in range(len(matrix[baris])):
        nilaiBobot = bobot[kolom]/100
        posisi = matrix[baris][kolom]
        nilaiPerPosisi = posisi*nilaiBobot
        nilaiPerBaris.append(nilaiPerPosisi)
    for item in nilaiPerBaris:
        nilai += item
    ranking.append(nilai)

for x in range(len(ranking)):
    print(alternatif[x][0]+" => "+ str(ranking[x]))


# kesimpulan yang dihasilkan
print("============================")
nama = ranking.index(max(ranking))
print("rekomendasi untuk kasus "+judul+" adalah = "+alternatif[nama][0])

