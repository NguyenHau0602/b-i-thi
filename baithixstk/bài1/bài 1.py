n=int(input("Nhập vào một số nguyên:"))
d = dict()
for i in range(1, n + 1):
    d[i] = i * i
print(d)
ten = input("Nhập tên:")
print(ten)
print ("Độ dài tên của "+ten+" là n = " +  str (len (ten)))
