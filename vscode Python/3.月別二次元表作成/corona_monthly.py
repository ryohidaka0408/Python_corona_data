import csv


# 対象月リスト
months = [
"2020/01","2020/02","2020/03","2020/04","2020/05","2020/06","2020/07","2020/08","2020/09","2020/10","2020/11","2020/12","2021/01","2021/02","2021/03","2021/04","2021/05","2021/06","2021/07","2021/08","2021/09"
]

# ファイル読み込み
with open("/Volumes/mac OS- Data/Pyhon3/vscode Python/3.月別二次元表作成/corona_base.txt","r", encoding="UTF-8") as file :
    csvData = csv.reader( file )
    allData = [aData for aData in csvData] #allDataは二重listである。つまり[[2020,01,26]=[添え字の0]......]である。aDataは、一行が代入されている。
PREF_NUM = 48

"""
# 月別感染者数の計算
dict = 2
total = []

for dict in range(2,49):
    for month in months:
        aMonthData = filter(lambda x:x[0][:7] == month, allData[dict::PREF_NUM])
        kazulist = [int(x[2]) for x in aMonthData]
        total.append(sum(kazulist))
print(total)
"""

# 書き込み用ファイルオープン
with open("/Volumes/mac OS- Data/Pyhon3/vscode Python/3.月別二次元表作成/corona_monthly.txt","w",encoding="UTF-8",newline = "\n")as f:
    writer = csv.writer(f)

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

