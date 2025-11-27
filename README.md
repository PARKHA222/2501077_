# 과제 11
b = input("숫자 5개를 입력하세요:").split()    
b = list(map(int,b))

z = input("문자 하나를 입력하세요:")

b.append(z)

print(b)

**숫자 입력을 받은 뒤 리스트로 형변환을 하였으며,    
입력 받은 문자 1개는 append를 이용하여 리스트 끝에 추가하였습니다.**

# 과제 12
b = input("숫자 5개를 입력하세요:").split()    
b = list(map(int,b))

del b[-2:]

print (b)

**숫자 5개를 입력 받은 뒤 리스트로 형변환을 하였고    
del을 이용하여 마지막 두 개의 값을 삭제하였습니다.**

# 과제 13
b = input("숫자 5개를 입력하세요:").split()

b = list(map(int,b))

for index, value in enumerate(b, start = 101):    
    print(index, value)

**숫자 5개를 입력 받은 뒤 리스트로 형변환을 하였고    
enumerate을 이용하여 101번 index부터 값을 출력하였습니다.**

# 과제 14
a = [10, 20, 30, 40, 30, 20, 10]    
result = a.count(20)

print(result)

**count를 이용하여 [10, 20, 30, 40, 30, 20, 10]에서    
20이 몇 개 있는지를 출력하였습니다.**

# 과제 15
b = input("숫자 10개를 입력하세요:").split()    
b = list(map(int,b))

b.sort()

print(b[0], " and ", b[-1])

**숫자 10개를 입력 받은 뒤 리스트로 형변환을 하였고    
sort로 정렬하였으며, 최저값과 최고값을 출력하였습니다**

# 과제 16
b = input("숫자 10개를 입력하세요:").split()    
b = list(map(int,b))    
min_value = min(b)    
max_value = max(b)    

z = sum(b)

result = z-max_value-min_value    
print(result)

**숫자 10개를 입력 받은 뒤 리스트로 형변환을 하였습니다.    
min과 max 함수를 이용하여 입력 받은 값의 최저값과 최고값을 찾아내었고    
그 값을 제외한 나머지 값의 합을 구하였습니다.**

# 과제 17
a = [10, 20, 30, 40, 30, 20, 10]    
a.remove(20)    
a.remove(20)    

print(a)

**특정 값을 찾아 삭제하는 remove를 사용하여 20을 삭제하였습니다.    
remove는 처음 찾은 값만 삭제하기 때문에 두 번을 이용하여 삭제했습니다.**

# 과제 18
b = list(i for i in range (1, 6))

print(b)

**list comprehension을 이용하여 1부터 5까지    
리스트를 만들어서 출력하였습니다.**

# 과제 19
b = [i for i in range(1, 21) if i % 2 == 1]

print (b)

**list comprehension을 이용하여 1부터 20까지 지정하였고,    
if 조건문을 사용하여 홀수만 출력하였습니다.**

# 과제 20
b, m = map(int,input("정수 2개를 입력하세요:").split())

z = [2 ** i for i in range(b, m + 1)]

del z[1]    
del z [-2]

print (z)

**첫 번째 입력 값의 범위는 1~20, 두 번째 입력 값의 범위는 10부터 30이며    
리스트 표현식인 comprehension을 이용하여 2의 거듭제곱 리스트를 출력하는     
프로그램을 만들었습니다. 리스트의 두 번째 요소와    
뒤에서 두 번째 요소는 삭제하라는 조건이 있어 del을 이용하였습니다.**

# 과제 21
sting_var = input("Hello, wolrd!를 입력하세요:")    
sting_var = sting_var.replace("Hello","Hi")     
print (sting_var)

**사용자로부터 Hello, wolrd! 입력 받은 뒤    
문자열 안의 문자열을 다른 문자열로 바꾸는 replace를 이용하여    
replaceHello를 Hi로 바꿔 출력하였습니다.    
바뀐 결과를 유지하고 싶어 문자열이 저장된 변수에 사용한 뒤    
다시 변수에 할당하는 방법을 사용하였습니다.**

# 과제 22
b = input("문자 4개를 입력하세요:").split()     
b = " / ".join(b)

print (b)

**4개의 문자를 입력 받은 후, 구분자 문자열과 문자열 리스트의    
요소를 연결해 문자열로 만드는 join을 이용하여    
입력 받았던 각 문자를 / 로 붙여서 출력하였습니다.**

# 과제 23
b = input("영어로 이름을 입력하세요:")     
z = b.lower().rjust(10)

print (z)

**성을 영어로 입력 받은 후, 소문자로 바꾸기 위해    
대문자를 소문자로 바꾸는 lower을 이용하였으며 문자열을 지정된 길이로    
만든 뒤 오른쪽으로 정렬하는 rjust을 이용해 출력하였습니다.**

# 과제 24
b = input("물품 가격을 입력하세요:")     
b = b.replace(';',' ')     
b = b.split()     
b = list(map(int,b))     
b.sort(reverse = True)     

for i in b:     
  print ('%9s' %(format(i)))

**물품 가격 여러 개가 문자열 한 줄로 입력 되고 각 가격은 ;으로 구분 되어있는데    
입력 받은 것을 list로 형변환 하였으며 sort 기능을 이용해 내림차순으로 정렬하였습니다.    
replace를 이용해 세미콜론 또한 공백으로 바꾸었으며,    
문자열 서식 지정해 전체 너비를 9자리로 맞추고 오른쪽 정렬을 하였습니다.**

# 감사합니다!
