def count_IC(t):
    fsum = 0.0
    L = 0
    for i in range(65,91):
        f = int(t.count(chr(i)))
        fsum += f*(f-1)
        L += f
    return fsum/(L*(L-1))

text = input()
# text = ""
# print("Please press ENTER and CTRL-C after typing: ")
# while 1:
#     try:
#         text += input("")
#     except:
#         break
text = text.upper().replace(" ", "").replace("\n", "")
data = ""
max_IC = 0
m = 0
for i in range(4,8): # 3 < the keyword length < 8
    sum = 0
    for j in range(0, i):
        c = j
        while (c < len(text)):
            data += text[c]
            c += i
        #print(data)
        sum += count_IC(data)
        data = ""
    # print("Group", i, "IC: ", sum/i)
    if (sum/i > max_IC):
        max_IC = sum/i
        m = i;
print(m)