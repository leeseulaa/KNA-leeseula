# # 변수 선언 방법
# # 변수 이름 + 값
# # 오른쪽 값을 왼쪽 이름에 저장하라는 코드
# temp = 36 # 숫자로 저장하고 싶다면 따옴표 금지
# name = 센서 A # 글자는 무조건 따옴표로 감싸기

# print(temp) # 36
# print("temp") # temp

# # = 는 같다가 아니라 저장하는 것
# # 비교는 ==을 사용 

# ===========================================
# print("=========변수 사용 활용=========")

# x = 5
# x = x + 5 # 변수를 재할당 할 때 변수 기존 자신의 값을 활용할 수 없음 
# # 변수에 할당 할 때 오른쪽에 먼저 계산한뒤 x 에 값을 재할당
# x = x + 5
# print(x) # 10

# y = y + 5 # 오류 발생 y가 선언되지 않았기 때문
# # =========================================
# print("=========재할당=========")

# print("재할당하기 전 temp: ", temp)
# temp = 15 # 위에서 할당했던 36이라는 값을 15로 재할당 (수정)
# Temp = 15 # temp와 다른 변수로 동작
# print("trmp: ", temp)
# print("Temp: ", Temmp)

# # 재할당은 지금까지 실행된 코드 중 가장 마지막으로 저장된 값이 불러옴 
# # print(score) # nameError
# score = 10
# score = 20
# score = 30
# print(score) # 30

# # =========================================
# print("=========값 복사=========")

# a = 10
# b = a # b변수에는 10이 저장 (저장할 때의 그 순간의 a값을 b에 복사)
# a = 100 # a의 변수를 재할당해도 
# print(b) # 10 b 변수의 값은 10이 그래도 유지됨 

# # =========================================
# print("=========여러 변수 한번에 선언 및 할당=========")

# # 형식: 변수 1, 변수 2 + 값 1, 2 < 변수와 같이 갯수가 같아야 함 
# width , height = 10, 20 # 앞에선 10 뒤에건 20 
# print("width" , widt,  "height" , height)

# x, y, z = 10, 20 # 변수 3개, 값 2개 벨류에러

# # =====================================
# print("=========주석으로 변수 설명=========")
# temp = 25 # 온도(섭씨)
# count = 3 # 센서 갯수 
# temp = 1000000000 # 주석처리된 코드는 작동하지 않음 
# print(temp) # 25
# ========================================

# temp = 25
# print(temp) 
# name = "센서 A"
# print(name) 

# =======================================
# temp = 30 
# print(temp)
# temperture = 25 
# print(temperture) 
# print("실습 3")
# my_numer = 22
# print(my_numer)
# mood = "good"
# print(mood)
# print("실습 4")
# age = 21
# label = "나이"
# print(label)
# print(age)
# print("실습 5")
# x = 10
# print(x) # 5
# x = x + 5 # 15
# print(x) # 15
# x = x*2 #30
# print("실습 6")
# a = 100
# print(a)
# b = a
# print(b)
# a = 999
# print(a)
# print(b)
# temp = 25
# print(temp)
# score = 90
# print(Score)
# print(score)
# temp = 25 # 온도(섭씨)
# count = 3 #센서개수
# #temp = 100
# print(temp)
# x = 5
# print(x)
# x = 10 
# print(x)
# x = x+1
# print(x)
# name = "이슬아"
# age = 21
# print("자기소개")
# print(name)
# print(age)
# a = 25 
# device_temp = 25
# b = 3
# sensor_count = 3
# print(device_temp)
# print(sensor_count)
# x,y,z = 1,2,3
# width, height = 4, 3 
# print(width)
# print(height)


