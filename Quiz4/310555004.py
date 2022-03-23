from typing import Collection
import numpy as np
import math

plain = "WITHMALICETOWARDNONEWITHCHARITYFORALLWITHFIRMNESSINTHERIGHTASGODGIVESUSTOSEETHERIGHTLETUSSTRIVEONTOFINISHTHEWORKWEAREINTOBINDUPTHENATIONSWOUNDSTOCAREFORHIMWHOSHALLHAVEBORNETHEBATTLEANDFORHISWIDOWANDHISORPHANTODOALLWHICHMAYACHIEVEANDCHERISHAJUSTANDLASTINGPEACEAMONGOURSELVESANDWITHALLNATIONSGREECEANNOUNCEDYESTERDAYTHEAGRAGREEMENTWITHTRUKEYENDTHECYPRUSTHATTHEGREEKANDTURKISHCONTINGENTSWHICHARETOPARTICIPATEINTHETRIPARTITEHEADQUARTERSSHALLCOMPRISERESPECTIVELYGREEKOFFICERSNONCOMMISSIONEDOFFICERSANDMENANDTURKISHOFFICERSNONCOMMISSIONEDOFFICERSANDMENTHEPRESIDENTANDVICEPRESIDENTOFTHEREPUBLICOFCYPRUSACTINGINAGREEMENTMAYREQUESTTHEGREEKANDTURKISHGOVERNMENTSTOINCREASEORREDUCETHEGREEKANDTURKISHCONTINGENTSITISAGREEDTHATTHESITESOFTHECANTONMENTSFORTHEGREEKANDTURKISHCONTINGENTSPARTICIPATINGINTHETRIPARTITEHEADQUARTERSTHEIRJURIDICALSTATUSFACILITIESANDEXEMPTIONSINRESPECTOFCUSTOMSANDTAXESASWELLASOTHERIMMUNITIESANDPRIVILEGESANDANYOTHERMILITARYANDTECHNICALQUESTIONSCONCERNINGTHEORGANIZATIONANDOPERATIONOFTHEHEADQUARTERSMENTIONEDABOVESHALLBEDETERMINEDBYASPECIALCONVENTIONWHICHSHALLCOMEINTOFORCENOTLATERTHANTHETREATYOFALLIANCE"
c1 = "ECDTMECAERAUOOLEDSAMMERNENASSODYTNRVBNLCRLTIQLAETRIGAWEBAAEIHOR"
c2 = "EOEYEGTRNPSECEHHETYHSNGNDDDDETOCRAERAEMHTECSEUSIARWKDRIRNYARANUEYICNTTCEIETUS"

def rectangle(text):
    Column = 0
    Row = 0
    min = 100
    L = len(text)
    for i in range(4, L+1):
        if(L%int(i) == 0):
            #print("For", i, "x", int(L/i) ,"rectangle, the sum of the difference is ", end='')
            vowel = L/i*0.4
            freq = [0] * i
            diff = 0.0
            for j in range(L):
                if(text[j] == "A" or text[j] == "E" or text[j] == "I" or text[j] == "O" or text[j] == "U"):
                    freq[j%i] += 1
            for j in range(i):
                diff += abs(freq[j]-vowel)
            #print(round(diff, 2))
            if diff < min:
                min  = diff
                Column = i
                Row = int(L/i)

    Matrix = [['']*Column for i in range(Row)]
    for i in range(Row):
        for j in range(Column):
            Matrix[i][j] += text[(i*Column + j)]
    return Matrix, Row, Column

def getAnswer(freq, data, row, column, first, second):
    check = [False]*row
    ans = [['']*column for i in range(row)]
    ans[0] = data[first]
    ans[1] = data[second]
    check[first] = True
    check[second] = True
    count = 2
    while (count < row):
        prob = [0]*row
        for i in range(row):
            if check[i]:
                continue
            for j in range(column):
                if (freq[ord(ans[count-2][j])-ord('A')][ord(ans[count-1][j])-ord('A')][ord(data[i][j])-ord('A')] == 0):
                    continue
                prob[i] += math.log10(26*freq[ord(ans[count-2][j])-ord('A')][ord(ans[count-1][j])-ord('A')][ord(data[i][j])-ord('A')])
        ans[count] = data[np.argmax(prob)]
        check[np.argmax(prob)] = True
        count += 1
        
    for line in np.array(ans).T:
        for c in line:
            print(c, end='')
            

if __name__ == "__main__":
    freq = np.zeros((26, 26, 26))

    for i in range(len(plain) - 2):
        freq[ord(plain[i])-ord('A')][ord(plain[i+1])-ord('A')][ord(plain[i+2])-ord('A')] += 1

    for i in range(26):
        for j in range(26):
            sum = 0
            for k in range(26):
                sum += freq[i][j][k]
            if (sum == 0):
                continue
            for k in range(26):
                freq[i][j][k] = freq[i][j][k]/sum

    data, row, column = rectangle(c1)
    print("Cipher: ECDTM ECAER AUOOL EDSAM MERNE NASSO DYTNR VBNLC RLTIQ LAETR IGAWE BAAEI HOR")
    print("Ans: ", end = '')
    getAnswer(freq, data, row, column, 5, 2)

    data, row, column = rectangle(c2)
    print("\nCipher: EOEYE GTRNP SECEH HETYH SNGND DDDET OCRAE RAEMH TECSE USIAR WKDRI RNYAR ANUEY ICNTT CEIET US")
    print("Ans: ", end = '')
    getAnswer(freq, data, row, column, 2, 5)
            

