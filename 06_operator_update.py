# 산술연산자 
# + = * / //(몫) %(나머지) **(거듭제곱)
print(3 + 5) # 8
print(10 - 4) # 6
print(4 * 5) # 20
print(20/4) # 5 (나눗셈 결과는 항상 float)
print(7//3) # 2
print(7 % 3) #1 (7개의 음료수를 3봉투에 담으면 2봉투와 1개의 음료수가 나옴)
print(2**5) #32

#========================
# 연산 우선순위와 우선순위 지정
# **(거듭제곱)> *(곱하기) /(나누기) //(몫) %(나머지) > 더하기 빼기 

print(2 + 8 *3) # 8 곱하기 3 먼저 다음 2 더하기
print((2 + 8)* 3) # 괄호 안의 연산을 먼저 한뒤 곱하기 계산  

#==========================
# 복합연산자 

result = 3 * 5
print(result) # 15

# +=: 기존 값에서 오른쪽 값을 더한뒤 재할당
# -=: 기존 값에서 오른쪽 값을 뺀뒤 재할당
# *=: 기존 값에서 오른쪽 값을 곱한 뒤 재할당
# /+=: 기존 값에서 오른쪽 값을 나눈 뒤 재할당

result += 10 # 25
print(result)
result -= 5 # 20
print(result)
result *= 3 # 60
print(result)
result /= 2 # 30.0
print(result)

# ================================
# 문자연 연산 
print("안녕" + "하세요") #안녕하세요

# 만약 "안녕"과 "하세요" 사이에 공백을 넣고 싶다면

# 방법1) , 사용
print(("안녕" , "하세요"))

# 방법2) 안녕 뒤에 공백 추가
print("안녕" + "하세요")
# 방법3) 공백만 있는 문자열 더하기 
print("안녕" + " " + "하세요")

# 문자열 곱하기 
print("안녕" * 5) #안녕안녕안녕안녕안녕

#문자열에 연산자를 사용할 경우 모두 이어져서 나옴

a = 17
b = 5
print(a+b) # 22
print(a-b) # 12
print(a*b) # 85
print(a/b) # 3.4
print(a//b) # 3
print(a%b) # 2
print(a**b) # 1419857

x = 90
y = 85
z = 100
print((x+y+z)/3) #91.67
side = 6
print(side**2) #36
가로 = 3
세로 = 4
높이 = 6
print(가로*세로*높이) #72


#===================================
print("===비교연산자===")
# < (미만), >(초과), <=(이하), >=(이상), ==(같다), !=(다르다)
# 비교 결과는 무조건 True or False (b00l)
print(7 < 16) # True
print(7 > 16) # False
print(7 <= 7) # True
print(7 >= 7) # True
print(7 == 7) # True
print(7 != 7) # False

#비교연산자는 문자열 비교도 가능
print("hello" == "hello") # True
print("정상" == "정상") # True

# 비교연산자를 사용해 문자열을 비교할 때 주의사항

# 1. 대소문자 구분 
print("hello" == "hello") # False

# 2.공백이 있어도 다르다고 판단
print("정상" == "정상 ") # False

# 부정연산자 != (not)
# 두 값이 동일한데 !로 인해서 값이 반대로 출력됨
print("hello" != "hello") # False
print("hello" != "hello ") # True
print("hello" != "Hello") # False

# 변수에 문자열을 할당하고, 변수로 문자열 비교
# 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교
# print("=== 질문 1) hello 변수에 할당하는 값을 따옴표로 감싸지 않고 비교 ===")
# hello = hi
# print(hello == hi)  # NameError(선언하지 않은 이름 호출했을 때)
# hi는 따옴표에 감싸져있지 않기 때문에 변수로 취급됨
# 그런데 우리는 hi 변수를 선언한 적이 없기 때문에 에러

# 질문 1) 해결방법
# print("=== 질문 1) 해결 방법 ===")
hi = "안녕"  # hello 변수에 hi 변수를 할당하기 전 hi 변수 선언
hello = hi  # print(hello) > 안녕
print("=== 변수 hello(안녕)와 변수 hi(안녕) 비교 ===")
print(hello == hi)  # True




hello = "hi"
print(hello == "hi") # True
# 위 비교에서 헬로는 따옴표로 감싸지지 않아서 변수로 취급
# 만약 헬로를 "헬로"와 같이 따옴표로 감싸면 
# string으로 인싣해서 변수 취급을 하지 않음 
# ex) "헬로" 와 "하이"를 비교하는 것

# 변수로 비교연산자 사용
num1 = 123
num2 = 456

print(num1 >= num2) # False
# print(num1 >= "num2") #TypeError
#TypeError: '>=' not supported between instance 'ont' of 'str'

#=================================
# and / or / not - 논리연산자
# and:  둘다 True여야 True를 반환함
print(5 == 5 and 7 == 7) # True + True = True
print(5 == 7 and 7 == 7) # False + True = False # 첫번째 조건이 false 라면 뒤에 조건은 확인 안함
print(5 == 7 and 7 != 7) # True + False = False

# or: 하나라도 True 라면 True
print(5 == 5 or 7 == 7) # True + True = True
print(5 == 7 or 7 == 7) # False + True = True
print(5 == 5 or 7 != 7) # True + False = True
# or 첫번째 조건이 True 라면 뒤에 조건은 확인 안함

# not: 값을 반대로 뒤집음
print(not True) # False 
print(not 5 == 5) # False 
# 5 == 5 를 연산하여 True 를 반환
# not 트루를 동작하여 트루를 뒤집어 펄스 반환
# 반환받은 펄스라는 값을 프린트가 터미널로 출력

# print( 5 == 8 ) # False
# print( 5 != 8 ) # True
# print( 5 > 8 ) # False
# print( 5 < 8 ) # True
# print( 5 >= 8 ) # False
# print( 5 <= 8 ) # True

print("실습 4")
temp = 85
temp_ok = temp > 60 and temp <= 90
print(temp_ok) # True

pressure = 5
pressure_ok = pressure >= 3 and pressure <= 7
print(pressure_ok) # True 

print(temp_ok and pressure_ok) # True

print("실습 5")
stock = 100
stock += 50
print(stock) # 150

stock -= 30 
print(stock) # 120

stock += 5 
print(stock) # 

print("실습 6")

total = 500
defect = 23
print(defect / total * 100) # 4.6 (불량률 %) 
run_h = 21
all_h = 24

print(run_h / all_h * 100) # 87.5 (가동률 %)

print("실습 7")
minutes = 500
print(minutes // 60 ) #8시간
print(minutes % 60 ) # 20분 

