# 閏年判別関数

def is_leapyear(y):
    if y % 400 == 0:
        flag = True
    elif y % 100 == 0:
        flag = False
    elif y % 4 == 0:
        flag = True
    else:
        flag = False
    return flag