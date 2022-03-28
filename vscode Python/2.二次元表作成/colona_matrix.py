import csv

with open("/Volumes/mac OS- Data/Pyhon3/vscode Python/2.二次元表作成/corona_base.txt","r", encoding="UTF-8") as file :
    csvData = csv.reader( file )
    allData = [aData for aData in csvData] #allDataは二重listである。つまり[[2020,01,26]=[添え字の0]......]である。aDataは、一行が代入されている。

# 日付の構成
with open("/Volumes/mac OS- Data/Pyhon3/vscode Python/2.二次元表作成/corona_matrix.txt","w",encoding="UTF-8")as f:
    for day in allData[1::48]:
        #print(day[0],day[1],day[2])
        f.write(f",{day[0]}")
    f.write("\n")
# 都道府県の構成
with open("/Volumes/mac OS- Data/Pyhon3/vscode Python/2.二次元表作成/corona_matrix.txt","a",encoding="UTF-8")as f:
    for spot in range(2,49):
        f.write(allData[spot][1]+",")
        for infected in allData[spot::48]:
            f.write(f"{infected[2]},")
        f.write("\n")
        