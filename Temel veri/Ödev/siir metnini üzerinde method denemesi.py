bas_harfler = ""

with open("C:/Users/asus/Desktop/siir.txt","r",encoding="utf-8") as file:
    for satır in file:
        bas_harfler += satır[0]
print(bas_harfler)


