import csv

dict = {"ALL":"合計",
"Hokkaido":"北海道",
"Aomori":"青森県",
"Iwate":"岩手県",
"Miyagi":"宮城県",
"Akita":"秋田県",
"Yamagata":"山形県",
"Fukushima":"福島県",
"Ibaraki":"茨城県",
"Tochigi":"栃木県",
"Gunma":"群馬県",
"Saitama":"埼玉県",
"Chiba":"千葉県",
"Tokyo":"東京都",
"Kanagawa":"神奈川県",
"Niigata":"新潟県",
"Toyama":"富山県",
"Ishikawa":"石川県",
"Fukui":"福井県",
"Yamanashi":"山梨県",
"Nagano":"長野県",
"Gifu":"岐阜県",
"Shizuoka":"静岡県",
"Aichi":"愛知県",
"Mie":"三重県",
"Shiga":"滋賀県",
"Kyoto":"京都府",
"Osaka":"大阪府",
"Hyogo":"兵庫県",
"Nara":"奈良県",
"Wakayama":"和歌山県",
"Tottori":"鳥取県",
"Shimane":"島根県",
"Okayama":"岡山県",
"Hiroshima":"広島県",
"Yamaguchi":"山口県",
"Tokushima":"徳島県",
"Kagawa":"香川県",
"Ehime":"愛媛県",
"Kochi":"高知県",
"Fukuoka":"福岡県",
"Saga":"佐賀県",
"Nagasaki":"長崎県",
"Kumamoto":"熊本県",
"Oita":"大分県",
"Miyazaki":"宮崎県",
"Kagoshima":"鹿児島県",
"Okinawa":"沖縄県",
}

with open("/Volumes/mac OS- Data/Pyhon3/vscode Python/1.基本データ作成/newly_confirmed_cases_daily.csv","r", encoding="UTF-8") as file :
    csvData = csv.reader( file )
    allData = [aData for aData in csvData] #allDataは二重listである。つまり[[2020,01,26]=[添え字の0]......]である。aDataは、一行が代入されている。

with open("/Volumes/USB/Python3/vscode Python/1.基本データ作成/corona_base.txt","w",encoding="UTF-8",newline = "\n")as f:
    writer = csv.writer(f)
    title = ["日付","都道府県名","人数"]
    writer.writerow(title)

    for aData in allData[1:]:
        write_data = []
        y,m,d = aData[0].split("/")
        write_data.append(f"{y}/{int(m):02d}/{int(d):02d}")
        write_data.append(dict[aData[1]])
        write_data.append(aData[2])
        writer.writerow(write_data)
