# 함수 : 나만의 명령어 만들기
# ex) a와 b를 입력받으면 이 두 변수를 더해라
# ex) 리스트를 입력받고 각 element의 최대값을 구해라

# parameter와 argument 차이점??


# 재귀 함수란?
# 이 함수가 재귀함수다! 어떻게 알 수 있을까?
# 1. 재귀 호출(자기 자신을 호출)이 있으면 재귀 함수
# 단 주의 : 무한 loop에 빠질 수 있다.
# 무한 loop를 막으려면?
# 2. 기저 조건(종료 조건) - return
"""
def kfc(lev):
    # 2. 기저 조건
    if lev == 2:
        return
    print(lev)
    # 1. 재귀 호출
    kfc(lev + 1)
    # kfc(lev + 1)
    print(lev)


kfc(0)
"""

"""
# sort()와 sorted()의 차이??
# 공통점 : 오름차순 정렬
arr = [1, 2, 3, 4, 5]

# 반환 x, 원본 변경 ---> sort()
arr.sort()
# 반환 o, 원본 변경 x ---> sorted()
sorted_arr = sorted(arr, reverse=True)  # 내림 차순
"""

"""
a = 30  # global scope  # 10


def kfc():
    global a  # global 쓰는 목적? -> 전역변수를 수정 하고 싶을 때
    a = 10  # local scope
    b = 20
    print(a)  # 10


kfc()
print(a)  # 10  -> built-in scope
"""

# a, b = map(int, input().split())
# map(첫번째 인자 == 함수, 두번째 인자)

"""
arr = [1, 2, 3, 4]
char = "hello"
my_tuple = (1, 2, 3)
my_dict = {"apple": 1, "banana": 2, "kiwi": 3}
my_set = {1, 2, 3}

# 시퀸스 == iterator (x)
# iterator : 반복 가능한 객체

for i in arr:  # iterator 방식으로 순회했다.
    print(i, end=" ")

for i in char:
    print(i, end=" ")

for i in my_tuple:
    print(i, end=" ")

for i in my_dict:  # key를 기준으로 순회
    print(i, end=" ")

for i in my_set:  # hash 값이 작은 순서대로 순회
    print(i, end=" ")
"""
