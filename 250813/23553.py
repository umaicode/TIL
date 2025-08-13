def pwr(level):
    if level == 0:
        return
    for i in level:
        pwr(level)
    print(1, 1, 1)
    level -= 1


pwr(3)
