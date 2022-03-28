# 指定日までの総日数計算プログラム
# 指定年数から-1年の12月31日までの総日数
from is_leapyear import is_leapyear

def total_days(birthday):
    y = birthday[0]-1
    ans1 = y * 365 + y // 4 - y // 100 + y //400
    
    #ここからは指定年数のみの総日数計算
    days_in_month = ( ( 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ),\
                  ( 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ) )
    ans2 = 0
    for n in range(1,birthday[1]):
        if is_leapyear(y):
            ans2 += days_in_month[1][n]#タプル[1]は、閏年用
        else:
            ans2 += days_in_month[0][n]#タプル[0]は、平年用
    ans2 += birthday[2] 
    
    totaldays = ans1 + ans2
    return totaldays
    