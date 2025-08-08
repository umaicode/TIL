text = "B[45]AB[9994]"

start1 = text.find("[")
end1 = text.find("]")

start2 = text.find("[", start1 + 1)
end2 = text.find("]", end1 + 1)

string1 = ""
string2 = ""

for i in range(start1 + 1, end1):
    string1 += text[i]

for i in range(start2 + 1, end2):
    string2 += text[i]

num1 = int(string1)
num2 = int(string2)

print(num1 + num2)
