import dateCalc

with open("C:/HIdaka ryo/Python/sample/test_target.csv","r",encoding="UTF-8")as f:
    allDate = f.readlines()


with open("C:/HIdaka ryo/Python/sample/result_target.csv","w",encoding="UTF-8")as d:
    # 読み込み/書き込み処理の記入
    for aDate in allDate:
        wY, wM, wD, wDays = aDate.split(",")
        baseDate = (int(wY), int(wM), int(wD))
        days = int( wDays.replace("\n", "" ))
        
        ans = dateCalc.targetDate(baseDate,days)
        d.write(f"{baseDate[0]}/{baseDate[1]}/{baseDate[2]},{days},{ans[0]}/{ans[1]}/{ans[2]}")
