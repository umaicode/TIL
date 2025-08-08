arr = ["ABCQ", "B[4]R", "CCDA", "BT[15]"]


def get_find(text):
    start = text.find("[")
    end = text.find("]")
    if start == -1 or end == -1:
        return None
    num_str = ""
    for i in range(start + 1, end):
        num_str += text[i]

    num = int(num_str)

    return num


for text in arr:
    if get_find(text) is not None:
        print(get_find(text), end=" ")
    else:
        continue
