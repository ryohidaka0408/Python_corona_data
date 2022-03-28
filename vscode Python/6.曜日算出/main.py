# 誕生日の曜日算出プログラム
# 誕生日の記入

from day_of_the_week import day_of_the_week
from totaldays import total_days
#import numpy as np 「numpyというある程度の計算を可能にするライブラリがある」

birthday = []
print("誕生日を入力してください")
year = int(input("年"))
birthday.append(year)

month = int(input("月"))
birthday.append(month)

day = int(input("日"))
birthday.append(day)

total_days(birthday)
day_of_the_week(total_days(birthday))

print(f"あなたの誕生日は、総日数:{total_days(birthday)}で、{day_of_the_week(total_days(birthday))}になります。")
