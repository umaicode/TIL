arr = ["O", "X"]
path = []
name = ["Luffy", "Zoro", "Sanji"]


def kfc(lev):
    if lev == 3:  # level : 3
        print_name()  # 함수호출 (이름 출력)
        return

    for i in range(2):  # branch : 2
        path.append(arr[i])
        kfc(lev + 1)
        path.pop()


def print_name():
    for i in range(3):
        if path[i] == "O":
            print(name[i], end=" ")
    print()


kfc(0)
