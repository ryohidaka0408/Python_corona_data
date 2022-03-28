# 1991/12/31までの通算日数
y = 1992 - 1
ans1 = y * 365 + y // 4 - y // 100 + y //400

print(ans1)

#残りの1992年1月1日から誕生日までの通算日数
days_in_month = ( ( 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ),\
                  ( 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ) )
barth = [1992,7,3]
ans2 = 0
for n in range(1,barth[1]+1):
    ans2 += days_in_month[1][n]#タプル[1]は、閏年用
    
ans2 += barth[2]
print(ans2) 

answer = ans1 + ans2
print(answer)

#曜日　　１月１日を土曜日とする(本来はそうらしい)
youbi = ["土曜日","日曜日","月曜日","火曜日","水曜日","木曜日","金曜日"]

if answer % 7 == 0:
    f = youbi[0]
if answer % 7 == 1:
    f = youbi[1]
if answer % 7 == 2:
    f = youbi[2]
if answer % 7 == 3:
    f = youbi[3]
if answer % 7 == 4:
    f = youbi[4]
if answer % 7 == 5:
    f = youbi[5]
if answer % 7 == 6:
    f = youbi[6]
    
print(f"通算日数:{answer}は、{f}です。")