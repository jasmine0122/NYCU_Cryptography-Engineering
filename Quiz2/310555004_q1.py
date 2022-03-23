text = "ECDTM ECAER AUOOL EDSAM MERNE NASSO DYTNR VBNLC RLTIQ LAETR IGAWE BAAEI HOR"
text = text.replace(" ", "")
L = len(text)
for i in range(1, L+1):
    if(L%int(i) == 0):
        print("For", i, "x", int(L/i) ,"rectangle, the sum of the difference is ", end='')
        vowel = L/i*0.4
        freq = [0] * i
        diff = 0.0
        for j in range(L):
            if(text[j] == "A" or text[j] == "E" or text[j] == "I" or text[j] == "O" or text[j] == "U"):
                freq[j%i] += 1
        for j in range(i):
            diff += abs(freq[j]-vowel)
        print(round(diff, 2))
            