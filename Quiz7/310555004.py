import re

silence = '010101010101010101010101010'
speech = '000000000011111111111110000000000111111111100000000'


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

result = ''
if __name__ == '__main__':
    # seq = re.sub(r"[^01]", "", input("Input sequence = "))
    seq = re.sub(r"[^01]", "", "0000000000000000111111111111101100000000000000001111101011001111000000000000010010111110101111110000010101100010111000001111101100000100000000001011111011001010001100000101001010001010111111100000010100110010110000101011011101000011111010111111101011001111000000010011000010111110101111100111000100010010111000011101110000011010010000011101110110110111011010100110011110111110111011010000010000110110101001011010001000001010101001111000111000101011011100010000101100010111011000000000010101100010101000011011111100000100010100101010010011111010011101010001011010001111111010010010111100000110101011001011001010101001010001101110001110110101101011010010001010011110111010001110001011110010100010110110101110000111001000101001001011000001100110101111110111111001101000111010101111001010101101011000011110011100001100101100100100001100111110100111001101110110110001011000000010101000010011001000111111010000111010011010111100110000010000100111101001101100010001001010101110011000110100111110001111011001000101111001111011101011101010111100111010001000111001111001100100110001111011111000100010000101100010011111110110010111100001001011111110111101110100101111001000000100111010101100011110001000101100011101111000011101101011111011010101000111000010101100111000111100101110010101010110101111110101010111101001101010101101001000111110011111101100111000111101101111100010010110101110100111111111000000101011101000111101100100110101111011011110101110000000101110110001110011000111110001111011101000110110010000100010001011010111111011001110011010101010101000100101111011111010101000000000011110011101011000101101001100001101111100011010111101001111100000001101101000001110011101111011110001100000111101010110010100111111000110010001011110011000100011101010101111001001010111100001101110011111001100110100000010011111001011111001001011101011001101001110000111011000010110011111100001110010101110010111101100011001000111010101111010111110101000111100001111001011010100011111011101111101101001110001011110010001100000000010001111000010011111110111111111110110101011111111001101011110001111101001101010001011011011010110011111000010100101011011010111000110011110110111011010011011100110101100100000000110100110111001001000110010010001101001000100110010110110010100111011100110011001111110011101000110000000011110101101100101111111001100110000011111011011101011111100011101011001101000101010001011111101001101001100000010001011001100011101000011111010110111011011100001010101000000100001100000110110111010111101001111001111011010001000001110111000101000010001000000010000111110111000110110000001010101000000100111101110010110111010111010101000010100111010001110011000010110110110011111101100011010010000100001110011010111101001110100001101000110100100101111101001000000001010011010011100100101111000100001010001110110111011001100100110101000000001001110000001101001110101001101001100111111100010000010001100011010101001101000101001111001100011110100100001011101111101111110001011100111110100100100101111111101010010011100001001000011001110110001010100001000110100011101101101111000010000000101010100101111101111011000001110101000101011100011011110010001010100110100110011011001000010000111100110000101001010001100010111111111011000001101111101111000100011110101001011101110010010101111000010110110110111011111000011101101001110001101101001010010100110101111011010110011001000101100011001001111011100010010101011000110110101001110001101001010011111010001000011000001010110000111100100001011110011110000010101010100011100100100111011111110101011011011100111000011110010010011110110100101111001001101111111100110000110101001001101011111000001011011011010010001100000001101000101100100111001000010000011000010010101100101011110110111111010010001011001110111101100111000111000111111111100101111111111001000001100011101001011111011011011011101000001010111010000000100110010111110101110011001110011110111001001110001111110011110101110100100001100110101010110111101100111010010101111000101111000111110111100111001010011111000011100100001110011111100100011001111001001101000011101110101101010011001101101110010010101")
    (poly, span) = Berlekamp_Massey(seq)
    # print('Characteristic polynomial is (%s)' % poly)
    for i in poly:
        result += str(i)
    print(result)
    print('linear span is (%d)'% span)