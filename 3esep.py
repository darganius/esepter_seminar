row = "1541 asdasd1 154da/ asdasd/ adsad/dasdas"
slash_sum = 0
for each in row:
    if each == "/":
        slash_sum += 1
        if slash_sum == 2:
            print(row(range(each:)))
print(slash_sum)