# print("this is the key")


chars = list("this is the key")


res = []
for ele in chars:
    if ele.strip():
        res.append(ele)
# chars1 = chars.replace(" ", "")
# print(len(res))
print(res)
