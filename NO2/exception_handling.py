#exception handling
print("--------------------------")
print("NAMA  :RIZKI DWI SANJAYA ")
print("NIM   :20210801091 ")
print("--------------------------")
try:
    a = int(input('masukkan nilai a '))
    b = int(input('masukkan nilai b '))
    hasil = a/b
except Exception as err:
    print(err)
else:
    print('hasil a/b adalah',hasil)
finally:
    print('blok kode finally dijalankan')
