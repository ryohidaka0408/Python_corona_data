days_in_month = ( ( 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ),\
                  ( 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ) )

set = [1992,7,3]
set2 = [2021,8,27]
flag = False

#1月1日は0とする

#Step1:1992年は閏年の為、まず閏年用の年数計算をanswerへ代入
answer1 = 0
for m in range(set[1],12):
    answer1 += days_in_month[1][m]#タプル[1]は、閏年用
    
answer1 -= set[2]
print(answer1)

#Step2:2021年は平年の為、まず平年用の年数計算をanswerへ代入
answer2 = 0
for n in range(1,set2[1]+1):
    answer2 += days_in_month[0][n]#タプル[0]は、平年用
    
answer2 += set2[2]
print(answer2) 

def is_leapyear(year):
    if year % 400 == 0:
        flag = True
    elif year % 100 == 0:
        flag = False
    elif year % 4 == 0:
        flag = True
    else:
        flag = False
    return flag

answer3 = 0
for i in range(set[0]+1,set2[0]):
    if is_leapyear(i):#関数の呼び出し→関数名(引数)
        answer3 += 366
    else:
        answer3 += 365
    
print(answer3)

answer = 0
answer += answer1 + answer2 +answer3 + 1 #1月1日を0としている為、+1日となる。

print("誕生日から現在日までの日数は{}である。".format(answer))
