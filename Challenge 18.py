def drawStars(underscore, asterisk):
    us = "_"
    ak = "*"
    uans = ""
    aans = ""
    for i in range(0,int(underscore)):
        uans = uans + us
    for i in range(0,int(asterisk)):
        aans = aans + ak

    res = uans + aans
    return res

under = input("Input number of underscores: ")
at = input("Input number of asterisks: ")
final = drawStars(int(under), int(at))
print(final)


