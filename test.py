a = 10
b = 70
s = "1"
#print("1) a ? b = ", a % b)

print("2) a ^ 2 = ", a ** 2)

print("3) a // 2 = ", a // 2)

print("4) a // 2 = ", a // 2)

print("5) a % b = ", a / 100 * b)

s = float(s)
print(s)


tup = [sd, asd, qwe] = [1.1, 2.2, 3]
print("====:", tup[1], sd, asd, qwe)
sd = 1.9
tup[1] = tup[1] + sd + 0.001 / 2
print("====:", tup[1], sd, asd, qwe)

for i in range(len(tup)):
    print("for ====:", i)
    print("for 2====:", tup[i])
    tup[i] = tup[i] + sd + 0.001 / 2