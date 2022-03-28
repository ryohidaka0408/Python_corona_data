import csv

# 対象月リスト
months = [
"2020/01","2020/02","2020/03","2020/04","2020/05","2020/06","2020/07","2020/08","2020/09","2020/10","2020/11","2020/12","2021/01","2021/02","2021/03","2021/04","2021/05","2021/06","2021/07","2021/08","2021/09"
]

PREF_NUM = 48

# 日別感染者数データ
with open("/Volumes/mac OS- Data/Pyhon3/vscode Python/4.月別千分率表作成/corona_monthly.txt","r", encoding="UTF-8") as file1 :
    csvData = csv.reader( file1 )
    months_Data = [monthData for monthData in csvData]

# 日本国内　都道府県別　人口データ
with open("/Volumes/mac OS- Data/Pyhon3/vscode Python/4.月別千分率表作成/population.txt","r", encoding="UTF-8") as file2 :
    csvData = csv.reader( file2 )
    popular_Data = [aData for aData in csvData]


# 書き込み用ファイルオープン
with open("/Volumes/mac OS- Data/Pyhon3/vscode Python/4.月別千分率表作成/corona_pre_mille.txt","w",encoding="UTF-8",newline = "\n")as wf:
    writer = csv.writer(wf)
    writer.writerow(months_Data[0])

    # 北海道から沖縄までループ
    for pref in range(1, PREF_NUM+1) :

        # 書き込み用リスト準備
        writeData = []

        # 都道府県名
        writeData.append(months_Data[pref][0])

        # 月別ループ
        for month in months:
            aMonthData = filter(lambda x:x[0][:7] == month, months_Data[pref::PREF_NUM])
            kazulist = [int(x[2]) for x in aMonthData]
            writeData.append(sum(kazulist))






"""
    # 1行目（年月）書き込み
    writer.writerow([""] + months)

    # 北海道から沖縄までループ
    for pref in range(2, PREF_NUM+1) :
        # 書き込み用リスト準備
        writeData = []

        # 都道府県名
        writeData.append(allData[pref][1])

        # 月別ループ
        for month in months:
            aMonthData = filter(lambda x:x[0][:7] == month, allData[pref::PREF_NUM])
            kazulist = [int(x[2]) for x in aMonthData]
            writeData.append(sum(kazulist))
        
        # １県分終了したので出力
        writer.writerow(writeData)
"""


