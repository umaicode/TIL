# 1. 아스키코드
# 대문자 A : 65, 소문자 a : 97
# 대문자 + 32 = 소문자

# 2. find 메서드
# (1) str.find() : 찾으면 발견된 인덱스 반환, 못찾으면 -1 반환
# (2) str.find('a', n):
# : n번 인덱스부터 시작해서 문자 'a'를 찾아라
# ex) [123]456[87] ---> 87을 parsing하고 싶다.

"""
test = "banana"
print(test.find("a"))  # 1
print(test.find("a", 2))  # 3
print(test.find("a", 4))  # 5
"""

# 회문 : 'level'
# 거꾸로 뒤집는 방법 [::-1]
"""
text = "level"


def is_p(text):
    return text == text[::-1]  # 맞으면 1, 다르면 0 반환


print(int(is_p(text)))
"""

"""
text = "helloworld[92084]answer"

# 1. '[' 위치 찾기
start_idx = text.find("[") + 1

# 2. ']' 위치 찾기
end_idx = text.find("]")

# 슬라이싱
number = text[start_idx:end_idx]
print(number)
"""

"""
arr = ["ABCQ", "B[4]R", "CCDA", "BT[15]"]


def get_find(text):
    # 못찾으면 빈문자열 return
    if text.find("[") == -1:
        return ""
    start = text.find("[") + 1
    end = text.find("]")
    # 찾으면 슬라이싱 return
    return text[start:end]


for text in arr:
    result = get_find(text)
    # 문자열이 비어있으면 False
    # 문자열이 있으면 True
    if result:
        print(result, end=" ")
"""

"""
text = "B[45]AB[9994]"

a = text.find("[")
b = text.find("]", a + 1)
c = text.find("[", b + 1)
d = text.find("]", c + 1)

t1 = text[a + 1 : b]
t2 = text[c + 1 : d]
"""


"""
text = "ABCDEFABCKKKKKABC"

a = 0
b = 0
cnt = 0

while True:
    b = text.find("ABC", a)
    # 더 이상 찾을 수 없을 때까지 반복
    if b == -1:
        break
    cnt += 1
    a = b + 1

print(cnt)
"""


def is_p(text):
    return text == text[::-1]


def find_p():
    # 가로방향 회문(행순회)
    for y in range(n):
        for x in range(n - m + 1):
            word = ""
            for k in range(m):
                word += arr[y][x + k]
            if is_p(word):
                return word  # 1번

    # 세로방향 회문(열순회)
    for x in range(n):
        for y in range(n - m + 1):
            word = ""
            for k in range(m):
                word += arr[y + k][x]
            if is_p(word):
                return word  # 2번

    return ""  # 3번 : 회문을 찾지 못한 경우


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    result = find_p()  # 원본을 바꾸려거나 , 디버깅에 필요하면 매개변수로 넣기
    print(f"#{tc} {result}")
