# get과 setdefault의 차이
# setdefault는 k의 key가 없으면 추가해준다.

seen = {1, 6, 3, 5, 9, 999, -10, -3}
a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)
a = seen.pop()
print(a)


# Q) 이 소스코드를 실행할 때마다 결과가 다를까? 같을까?
# A) 정수의 해시값은 일정하기 때문에 결과가 같다

# Q) 정수의 해시값은 일정하다. pop을 했을 때 작은 값 먼저 제거, 반환?
# A) X

# Q) 세트의 요소에 문자가 있을 때도 실행할 때마다 결과가 같을까? 다를까?
# A) 정수의 해시값은 일정하고, 문자의ㅏ 해시값은 일정하지 않다.
