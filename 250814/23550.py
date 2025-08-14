def KFC(lev):
    if lev == 6:
        return
    print(lev, end = " ")
    KFC(lev+1)
    print(lev, end = " ")

KFC(0)