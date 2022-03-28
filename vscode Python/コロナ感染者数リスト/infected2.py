
# このプログラムは日別の日本国内の総感染者のリストを抽出したもの
with open("C:/HIdaka ryo/Python/コロナ感染者数リスト/newly_confirmed_cases_daily.csv","r",encoding="UTF-8")as f:
    alllines = f.readlines()
    row_num = len(alllines)
    for row_n in range(1,row_num,48):# alllines(1:row_numは省略可能:48)でもOK!!　間を空白にしてても問題ない。
        print(alllines[row_n])


