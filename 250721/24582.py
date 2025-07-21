a = 10.25
b = 20.31
sum_v = a + b


# 1. 포맷팅 (옛날 스타일)
print("%.1f" % sum_v)

# 2. format() 메서드
print("{:.1f}".format(sum_v))

# 3. f-string (가장 파이써닉한 방법)
print(f"{sum_v:.1f}")

print(round(sum_v, 1))
