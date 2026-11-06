x = input()
num = x.split()
lst = []

for i in num:
    lst.append(chr(int(i)))
print(lst)