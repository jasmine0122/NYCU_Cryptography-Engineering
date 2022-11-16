from random import randint, shuffle

def chaffing_by_tail_tweaking(password, t, honeypot):
    words = [password]
    tmp_head = password[:len(password)-t]
    tmp_tail = password[len(password)-t:]

    while (len(words)-1 < honeypot):
        tmp = tmp_head
        for i in range(t):
            if(tmp_tail[i].isdigit()):
                tmp += str(randint(0, 9));
            elif(tmp_tail[i].islower()):
                tmp += str(chr(randint(97, 122)));
            elif(tmp_tail[i].isupper()):
                tmp += str(chr(randint(65, 90)));
            else:
                j = randint(1, 3)
                if j == 1:
                    tmp += str(chr(randint(32, 47)));
                elif j == 2:
                    tmp += str(chr(randint(58, 64)));
                else:
                    tmp += str(chr(randint(91, 96)));
        words.append(tmp)

    shuffle(words)
    return words

def chaffing_by_tweaking_digits(password, t, honeypot):
    words = [password]

    while (len(words)-1 < honeypot):
        tmp = ''
        count = 0
        flag = 1
        for i in range(len(password)-1, -1, -1):
            if(count == t):
                flag = 0;
            if(password[i].isdigit() and flag):
                count+=1
                tmp += str(randint(0, 9))
            else:
                tmp += password[i]
        tmp = tmp[::-1]
        words.append(tmp)

    shuffle(words)    
    return words

def take_a_tail(head, tail, honeypot):
    words = [head+tail]

    while (len(words)-1 < honeypot):
        tmp = head
        for i in range(3):
            tmp += str(randint(0, 9))
        if(tmp not in words):
            words.append(tmp)
    shuffle(words)
    return words

if __name__ == '__main__':
    print("Password is @310555004_Stu")
    print("<Chaffing_by_tail_tweaking>")
    h1 = chaffing_by_tail_tweaking('@310555004_Stu', 6, 5)
    print(h1)
    print("<Chaffing_by_tweaking_digits>")   
    h2 = chaffing_by_tweaking_digits('@310555004_Stu', 6, 5)      
    print(h2, '\n')

    print("Password is stu_310555004")
    print("<Take_a_tail>") 
    h3 = take_a_tail('stu_310555', '004', 5)
    print(h3, '\n')
