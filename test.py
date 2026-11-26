# python 실습/261125.py
# #1) 출력
# print("안녕하세요")

# #2) 변수오 ㅏ자료형
# name="홍길동" #문자열 str
# age=17 #정수int
# height=172.5 #실수 float
# is_student = True #참/거짓 bool

# #cal f
# def add(num1, num2, giho)
#     if giho == "+":
#         return num1 + num2
#     elif giho == "-":
#         return num1 - num2
#     elif giho == "*":
#         return num1 * num2
#     else :
#         return "warning"

# 삼각형 출력
n = 5
for i in range(n, 0, -1):  # 시작,끝,범위
    if i > 0:
        print("*" * i)
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
