#fungsi rekursif
print("--------------------------")
print("NAMA  :RIZKI DWI SANJAYA ")
print("NIM   :20210801091 ")
print("--------------------------")
def tampilkanAngka (batas, i = 1):
  prefix = '--' * (i - 1)

  print(f'{prefix} Sebelum rekursif ({i})')
  if (i < batas):
    # di sini lah rekursifitas itu terjadi
    tampilkanAngka(batas, i + 1)

  print(f'{prefix} Sesudah rekursif ({i})')

# memanggil fungsi tampilkanAngka
# untuk pertama  kali
tampilkanAngka(5)
