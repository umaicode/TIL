# 특정 구간을 반복 ---> for문
# 무한반복 + break ---> while문

"""
arr = list(map(int, input().split()))

# 최대값 초기화(문제에서 음수가 없을 때는 0으로 초기화)
# max_v = 0
# 최대값의 범위가 문제에 주어지지 않을 때
max_v = float("-inf")  # 음의 무한대
# min_v = float('inf')  # 양의 무한대

for idx, value in enumerate(arr):
    # 최대값 코드
    if value > max_v:
        max_v = value  # 최대값 갱신 되었을 때 인덱스
        result = idx  # 그 때의 인덱스

print(result)
"""

# find 메서드
# 이론 2가지
# 1. str.find() : str에서 특정 문자나 문자열을 찾아주는 메서드
# 찾으면 첫번째로 발견된 인덱스 반환, 못찾으면 -1
# 2. str.find('a', n)
# n번째 인덱스부터 시작해서 'a' 문자를 찾아라

"""
text = "B[45]AB[2234]"
start1 = text.find("[")
end1 = text.find("]", start1 + 1)
start2 = text.find("[", end1 + 1)
end2 = text.find("]", start2 + 1)
"""

# for - break ---> 함수
# if - else ---> 함수

# 함수로 변환하는 연습


# def get_domain(email):
#     idx = email.find("@")
#     # 기호 없으면 "Invalid email" return
#     if idx == -1:
#         return "Invalid email"

#     # @있으면 슬라이싱 return
#     domain = email[idx + 1 :]
#     return domain


# email = input()

# result = get_domain(email)
# print(result)

# 유니코드
# 알파벳의 유니코드 ---> 아스키코드

# 암기 2개
# 대문자 'A' == 65
# 소문자 'a' == 97

"""
char1 = "K" # 대문자
char2 = ord(char1) + 32 # 소문자
print(chr(char2))
"""


# 문자열은 불변시퀀스 ---> 원본은 바뀌지 않는다.
"""
text = "seungchan.park"
text2 = text.replace("seungchan", "bogeom")
print(text2)
"""

# element 한개 추가 ---> append
# iterable 추가 ---> extend
# pop() ---> 맨 끝 element 제거, 반환
# pop(0) ---> 맨 앞 element 제거, 반환

"""
arr = [1, 2, 3]
arr.extend("str")
print(arr)
"""


"""
cnt = 0
for i in arr:
    if i == 1:
        cnt += 1
        # 다른 로직 ....
print(cnt)

arr = [1, 2, 3, 4, 5]
arr2 = arr[::-1]
arr.reverse()
print(arr2)
print(arr)
"""

"""
stack = []

while True:
    char = int(input())
    # 0이 입력되면 append하지 않고 break 먼저
    if char == 0:
        break
    stack.append(char)  # 스택에 추가

word = ""
while stack:  # stack이 빌 때까지 반복
    word += str(stack.pop())    # 후입선출 ---> 역순으로

print(word)
"""

"""
n = int(input())

friends = [1, 2, 3]

# n번 자리 바꾸기
for _ in range(n):
    front = friends.pop(0)
    # 맨 뒤에 추가
    friends.append(front)

print(friends[0])
"""


# sort와 sorted 차이 반환값이 없는지 있는지(원본이 변경 되는지 안되는지)
# 반환값이 없으면 원본이 변경된 것, 반환값이 있으면 원본 변경이 안됨
# 즉, 원본을 변경하기 싫으면 sorted() 써야한다.

# arr = [3, 2, 5, 1, 4]
# arr.sort()  # 오름차순 정렬
# print(arr)
# arr.sort(reverse=True)
# print(arr)

"""
n = int(input())
numbers = list(map(int, input().split()))
# 오름차순 정렬
numbers.sort()
result = ""
for num in numbers:
    result += str(num)  # 문자열로 바꿔서 연결

print(result)
"""


"""
result = []
arr = [0] * 5
for _ in range(5):
    result.append(arr)
"""

# 파이써닉하다 (파이썬 스러우면서 코드가 간결하다)
arr = [[0] * 5 for _ in range(5)]
print(arr)

# 2차원 배열 입력(n행)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(5)]
