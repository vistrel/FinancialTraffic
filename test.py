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

print("\n- - - - - - - - - - - -\n")

print(type(tup))
tup2 = [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]]
print(type(tup2))
tup3 = {"key1": 1.1, "key2": 2.2, "key3": 3.3}
print(type(tup3))
print(tup3["key2"])

# first symbol is always BIG
bolean_value = True
print("Boolean value:", bolean_value)

#max
print("Max value:", max(tup))
#min
print("Min value:", min(tup))
#abs
print("Abs value:", abs(-544.5))

#round
print("Round value:", round(3.14159, 2))
print("Round value2:", round(3.14159))  # without second argument
print("Round value3:", round(3.14159, 0))  # rounding to nearest integer
print("Round value4:", round(23.14159, -1))  # rounding to nearest ten
#sum
print("Sum value:", sum(tup))
#sorted
print("Sorted value:", sorted(tup))
#len
print("Length of tuple:", len(tup))

# ostatok %
a = 5
b = 3
print("Ostatok:", a % b)

# pow
print("Power:", pow(a, b))  # a raised to the power of b, or
print("Power:", a ** b)  # same as a ** b

# delenie 
print("Delenie:", a / b)  # float division
print("Delenie2:", a // b)  # integer division
print("Delenie3:", round(a / b))  # delenie d bolshuy storonu



#print info
print("comment example", "..", "0 ", sep=" | ", end="!\n\n")