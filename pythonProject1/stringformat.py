a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

print(str.format("{2} = {0} - {1}", a, b, a - b))
print(str.format("{re} = {a} - {b}", a = a, b = b,re = a - b))
print(str.format("{re} = {0} - {1}",a, b,re = a - b))