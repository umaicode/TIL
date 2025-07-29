scores = {"bogeom": 89, "sangho": 100, "IU": 78, "sori": 76, "hejun": 85}

scores_list = list(scores.items())

max_score = 0
for name in scores_list:
    if name[1] >= max_score:
        max_score = name[1]
        best_student = name[0]

print(best_student)
