freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
        0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

def group_word(klen, t):
    data = ""
    G = []
    for j in range(0, int(klen)):
        c = j
        while (c < len(t)):
            data += t[c]
            c += int(klen)
        G.append(data)
        data = ""
    return G

def count_IC(t):
    fsum = 0.0
    L = 0
    for i in range(65,91):
        f = int(t.count(chr(i)))
        fsum += f*(f-1)
        L += f
    return fsum/(L*(L-1))

def KeyLen(text):
    max_IC = 0
    m = 0
    data = ""
    for i in range(4,8): # 3 < the keyword length < 8
        sum = 0
        for j in range(0, i):
            c = j
            while (c < len(text)):
                data += text[c]
                c += i
            sum += count_IC(data)
            data = ""
        if (sum/i > max_IC):
            max_IC = sum/i
            m = i;
    return m


def getKey(t):
    L = len(t)
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    f = []
    for i in alpha:
        f.append(t.count(i)/L)
    inner = []
    for i in range(26):
        sum = 0;
        for j in range(26):
            sum += freq[j]*f[j]
        inner.append(sum)
        f = f[1:] + f[:1]
    return alpha[inner.index(max(inner))]

# while 1:
text = input()
# print("Please press ENTER and CTRL-C after typing cipher: ")
# while 1:
#     try:
#         text += input("")
#     except:
#         break
text = text.upper().replace(" ", "").replace("\n", "")
Klen = KeyLen(text)
group = group_word(Klen, text);

key = ""
for i in range(int(Klen)):
    key += getKey(group[i])
print(key)