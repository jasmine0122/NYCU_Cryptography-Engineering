while 1:
    text = ""
    while 1:
        try:
            text += input("")
        except:
            break
    fsum = 0.0
    L = 0
    for i in range(65,91):
        f = int(text.count(chr(i)))
        fsum += f*(f-1)
        L += f
    IC = fsum/(L*(L-1))
    print("%.5f" % IC, "({})".format(IC))