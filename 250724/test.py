# import math
# from math import ceil, floor, pi
# from math import ceil as olim

# PI = pi

# print(math.ceil(PI))
# print(ceil(PI))
# print(math.floor(PI))
# print(round(PI))  # built-in scope
# print(olim(PI))


# json 과 dict의 공통점
# key : value 쌍

# 차이점
# json은 반드시 key 값이 문자열, 큰따옴표

# json 파싱을 어떻게 할까?
# 1. 터미널로 출력결과를 확인하기에는 가독성이 많이 떨어진다.
#   -> viewer로 확인한다.
# 2. json을 viewer로 복사 붙여넣기하고 확인(parsing 준비)


# import requests

# url = "https://date.nager.at/api/v3/publicholidays/2025/KR"

# .json ---> 딕셔너리? json : 딕셔너리
# response = requests.get(url).json()

# .text ---> json
# response = requests.get(url).text

# print(response)

"""
people = ["장상호", "박보검", "아이유"]

# 리스트를 순회하려고 한다. ---> 파이써닉 하지 않은 방식
for i in range(len(people)):
    print(people[i], end=" ")

# 리스트를 순회하려고 한다. ---> 파이써닉한 방식 : 이터레이블

for i in people:
    print(i, end=" ")
"""

# for문은 언제 쓰고 while문은 언제 써야 할까
# 특정 구간을 반복(예를 들어 2부터 8까지 반복)
# for문 쓰는게 낫다
# 무한 loop 특정 조건에서 break
# while문 쓰는게 낫다 - while-break

# for i in range(2, 10, 3):
# 이걸 while문으로 바꿀 수 있나?

"""
i = 2
while i < 10:
    i+=3
"""


"""
while 문 : 조건식이 참인동안 반복하는 반복문
초기식
while 조건식 : 
    code ...
    증감식
"""
