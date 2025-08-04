# for문 이론 1
"""
# n번 반복하는 반복문

for i in range(n):
    print(i, end = ' ') # 0, 1, 2, 3 .... n-1

# n번 반복하는 반복이다.
"""


# for 문 이론 2

"""
# start, end를 입력받고 (정수 두개를 입력)
# start부터 end까지 출력해보세요.(순회, 역순회)

# 1. start < end (증가 하는 경우) - 순회
for i in range(start, end + 1):

# 2. start > end (감소하는 경우) - 거꾸로 순회
for i in range(start, end - 1, -1):

핵심 : 수직선 상에서 end를 항상 포함하지 않는다.
"""

"""
리스트(배열) : 여러개의 객체를 하나의 객체로 묶고싶다.

리스트 이론 1.
sequence 자료형 (순서가 있다.) - 인덱싱 O, 슬라이싱 O, 순회 O...
가변 자료형

arr = [1, 2, 3, 4, 5]
1. 인덱싱 : 항상 0부터 시작
마지막 원소를 인덱싱
arr[-1], arr[len(arr) - 1]

2. 슬라이싱, 이 리스트를 거꾸로 슬라이싱
arr[::-1]
"""

"""
arr = [9, 5, 1, 15, 7, 3]

# 순회하는 방식 
# 1. iterator 방식
# 2. indexing 방식
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end = ' ')
"""


# 리스트 이론 2
"""
arr = [10, 10, 10, 10, 10, 10] 이렇게 채우고싶다

첫 번째 방법 append

arr = []
for _ in range(6):
    arr.append(10)
    
두 번째 방법 인덱싱

arr = [0] * 6
for i in range(6):
    arr[i] = 10
    
결론 : 두 가지 방법 다 알고 있어야 한다. 능숙도 올려주세요.
"""

"""
arr = []

for i in range(10, -3, -3): # 10, 7, 4, 1, -2
    arr.append(i)

# temp = 10
# for i in range(5):
#     arr.append(temp) # 10, 7, 4, 1, -2
#     temp -= 3

print(*arr)
"""
