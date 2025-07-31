# 함수명 snake_case
# 클래스 명 짓는 규칙 - Paskal case (첫글자가 대문자)

"""
# 클래스 정의
class SetMenu:
    # 생성자 메서드
    def __init__(self):
        self.potato = 100  # 인스턴스 변수(속성), 필드
        self.hambug = 300

    # 메서드
    # append(), pop() ---> 호출할 수 있는 이유 : built-in scope기 때문에
    def eat(self):
        print("햄버거 세트 맛있다.")
        print(f"음 {self.potato + self.hambug}불이 들었네")


# 클래스 호출(변수 = 클래스명())
# 인스턴스 생성
sanghai = SetMenu()
# 메서드 호출
sanghai.eat()
print(id(sanghai))
"""

# a = 3  # 할당
# b = [1, 2, 3, 4, 5]  # 할당
# c = SetMenu()  # 할당
# a = 15  # 재할당
# b[3] = 2  # 할당 x
# a = SetMenu()  # 재할당

# Q) c에 할당 된 SetMenu()와 a에 할당된 SetMenu()는 서로 같은 객체? 다른 객체?
# A) 서로 다른 객체
# ex) 메이플스토리 캐릭터 생성 렌 하나 생성, 렌 하나 더 생성 : 서로 다른 캐릭터
# Q) 할당 횟수?
# A) 5번
# Q) 객체는 총 몇개?
# A) 11개 (리스트 안에 있는 정수 하나하나가 다 객체)

"""
class Calculator:
    pi = 3.141592  # 클래스 변수

    # 생성자
    def __init__(self, name):
        self.name = name  # 인스턴스 변수

    # 메서드
    def add(self, a, b):
        return a + b

    # 매직 메서드 ---> 객체를 문자열로 표현할때 호출됨
    def __str__(self):
        return f"Calculator name : {self.name}"

    # 클래스 메서드 ---> 클래스 자체를 첫번째 인자로 받는다.
    @classmethod
    def get_pi(cls):
        return f"pi 값은 {cls.pi}"

    # 스태틱 메서드 ---> self, cls가 없음, 독립적으로 실행 가능
    @staticmethod
    def multiply(a, b):
        return a * b


# 인스턴스 생성
calc = Calculator("공학용 계산기")
# 메서드 호출
print(calc.add(2, 3))
# 매직 메서드 호출 - 인스턴스를 할당한 변수만 작성
print(calc)
# 클래스 메서드 호출 - 클래스로 직접 호출
print(Calculator.get_pi())
# 스태틱 메서드 호출 - 클래스로 호출도 가능, 인스턴스로 호출도 가능
print(Calculator.multiply(4, 5))
print(calc.multiply(4, 5))
"""


# 상속으로 할 수 있는 것 2가지(부모 메서드 교체, 새로운 메서드 추가)
# 1. 오버라이딩

"""
# 부모 클래스
class Person:
    def walk(self):
        print("사람이 걷는다.")


# 자식 클래스
class SuperMan(Person):
    def fly(self):
        print("슈퍼맨이 난다.")

    def walk(self):  # 오버라이딩 == 메서드를 재정의 한다.(목적 : 부모 메서드를 교체)
        print("슈퍼맨이 뚜벅뚜벅 걷는다.")


a = SuperMan()  # 인스턴스 생성 (자식클래스의)
# 자식클래스의 인스턴스를 생성해도 부모클래스의 메서드 호출이 가능
a.walk()  # 메서드 호출
a.fly()
"""


# EAFP (try-except 구조)
# - IndexError


def get_v(arr, idx):
    try:
        return arr[idx]
    except IndexError:
        return -1


arr = [1, 2, 3]
result = get_v(arr, 5)
print(result)


# LBYL(if-else 구조
def get_v(arr, idx):
    if 0 <= idx <= len(arr) - 1:
        return arr[idx]
    return -1


arr = [1, 2, 3]
result = get_v(arr, 5)
print(result)
