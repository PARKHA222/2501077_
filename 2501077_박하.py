# 과제 11
b = input("숫자 5개를 입력하세요:").split()
b = list(map(int,b))

z = input("문자 하나를 입력하세요:")

b.append(z)

print(b)

# 과제 12
b = input("숫자 5개를 입력하세요:").split()
b = list(map(int,b))

del b[-2:]
print (b)

# 과제 13
b = input("숫자 5개를 입력하세요:").split()
b = list(map(int,b))

for index, value in enumerate(b, start = 101):
    print(index, value)

# 과제 14
a = [10, 20, 30, 40, 30, 20, 10]
result = a.count(20)

print(result)

# 과제 15
b = input("숫자 10개를 입력하세요:").split()
b = list(map(int,b))

b.sort()

print(b[0], " and ", b[-1])

# 과제 16
b = input("숫자 10개를 입력하세요:").split()
b = list(map(int,b))
min_value = min(b)
max_value = max(b)

z = sum(b)

result = z-max_value-min_value
print(result)

# 과제 17
a = [10, 20, 30, 40, 30, 20, 10]
a.remove(20)
a.remove(20)

print(a)

# 과제 18
b = list(i for i in range (1, 6))

print(b)

# 과제 19
b = [i for i in range(1, 21) if i % 2 == 1]

print (b)

# 과제 20
b, m = map(int,input("정수 2개를 입력하세요:").split())

z = [2 ** i for i in range(b, m + 1)]

del z[1]
del z [-2]

print (z)

# 과제 21
sting_var = input("Hello, wolrd!를 입력하세요:")
sting_var = sting_var.replace("Hello","Hi")
print (sting_var)

# 과제 22
b = input("문자 4개를 입력하세요:").split()
b = " / ".join(b)

print (b)

# 과제 23
b = input("영어로 이름을 입력하세요:")
z = b.lower().rjust(10)

print (z)

# 과제 24
b = input("물품 가격을 입력하세요:")
b = b.replace(';',' ')
b = b.split()
b = list(map(int,b))
b.sort(reverse = True)

for i in b:
  print ('%9s' %(format(i)))