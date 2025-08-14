'''
def tree(level):
    if level == 3:
        return

    tree(level+1)
    tree(level+1)
    print(level)

tree(0)
'''

def KFC(lev):
    if lev == 3:
        return

    for i in range(2):
        KFC(lev+1)

    print(lev)

KFC(0)