chars = input("Enter a pass: ")

res = []
for ele in chars:
    if ele.strip():
        res.append(ele)
# chars1 = chars.replace(" ", "")
# print(len(res))
print(res)