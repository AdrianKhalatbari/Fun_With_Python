hame = []
first = open("/Users/mohammad/Downloads/Exercise4_stepdata.txt", "r", encoding="utf-8")
# second=open("second.txt","w")
asghar = first.readlines()
for row in asghar:
    hame.append(int(row.replace("\n", "")))
    # akbar = second.write(row + '\n')
hame.sort()
print(hame)
# print(str(min(hame)))
# m = min(hame)
# print(m)
# second.close()
first.close()
