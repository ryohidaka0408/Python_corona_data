import dateCalc

wy, wm, wd = input( "日付 > " ).split("/")
year, month, day = int(wy), int(wm), int(wd)
youbi = dateCalc.weekday( year, month, day )

print( f"{year}年{month}月{day}日は{youbi}曜日")