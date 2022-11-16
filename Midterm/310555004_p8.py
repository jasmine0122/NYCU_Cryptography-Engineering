import os
import re

silence = '010101010101010101010101010'
speech = '000000000011111111111110000000000111111111100000000'
values = []
st = ''
result = ''

def Berlekamp_Massey(sequence):
    N = len(sequence)
    seq = [int(i) for i in sequence]

    for k in range(N):
        if seq[k] == 1:
            break
    f = set([k + 1, 0])
    l = k + 1

    g = set([0])
    a = k
    b = 0

    for n in range(k + 1, N):
        d = 0
        for ele in f:
            d ^= seq[ele + n - l]

        if d == 0:
            b += 1
        else:
            if 2 * l > n:
                f ^= set([a - b + ele for ele in g])
                b += 1
            else:
                temp = f.copy()
                f = set([b - a + ele for ele in f]) ^ g
                l = n + 1 - l
                g = temp
                a = b
                b = n - l + 1

    def print_poly(polynomial):

        lis = sorted(polynomial, reverse=True)

        lf = [0] * 2049
        
        for i in lis:

            lf[int(i)] = 1
            # if i == 0:
            #     result += '1'
            # else:
            #     result += 'x^%s' % str(i)
            #     # result += '1'

            # if i != lis[-1]:
            #     result += ' + '

        # return result
        return lf

    return (print_poly(f), l)

if __name__ == '__main__':
    filepath ='ciphertext.bin'
    binfile = open(filepath, 'rb') 
    size = os.path.getsize(filepath)
    for i in range(size):
        data = bin(ord(binfile.read(1)))

        a = data[2:]
        while(len(a) != 8):
            a = '0'+a
        # print(a)
        st += a
        # values.append(data[2:])

    binfile.close()
    # print(values)
    seq = re.sub(r"[^01]", "",st)
    (poly, span) = Berlekamp_Massey(seq)
    # print('Characteristic polynomial is (%s)' % poly)
    for i in poly:
        result += str(i)
    print(result)
    print('linear span is (%d)'% span)
