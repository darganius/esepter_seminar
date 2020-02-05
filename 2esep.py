with open("esep.txt", "r") as f:
    a = f.read()
print(a)
a = a.split(" ")
print(a)
for each in a:
    each = int(each)
    if each%2!=0:
        each = each*each
        print(each)
    else:
        print(each, "Not a odd number")