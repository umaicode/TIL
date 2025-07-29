# scores = {"bogeom": 89, "sangho": 100, "IU": 78, "sori": 76, "hejun": 85}

# scores_list = list(scores.items())

# max_score = 0
# for name in scores_list:
#     if name[1] >= max_score:
#         max_score = name[1]
#         best_student = name[0]

# print(best_student)


scores = {"bogeom": 89, "sangho": 100, "IU": 78, "sori": 76, "hejun": 85}

# 최대 점수 초기화
max_v = 0
best = ""
for key, value in scores.items():
    if value > max_v:
        max_v = value  # 최대값 갱신 코드
        best = key  # 최대값 갱신 되었을 때 학생

print(best)
