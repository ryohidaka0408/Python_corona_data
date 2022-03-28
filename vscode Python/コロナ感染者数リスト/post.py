"""
0:Date,Prefecture,Newly confirmed cases
1:ALL
2:Hokkaido
3:Aomori
4:Iwate
5:Miyagi
6:Akita
7:Yamagata
8:Fukushima
9:Ibaraki
10:Tochigi
11:Gunma
12:Saitama
13:Chiba
14:Tokyo
15:Kanagawa
16:Niigata
17:Toyama
18:Ishikawa
19:Fukui
20:Yamanashi
21:Nagano
22:Gifu
23:Shizuoka
24:Aichi
25:Mie
26:Shiga
27:Kyoto
28:Osaka
29:Hyogo
30:Nara
31:Wakayama
32:Tottori
33:Shimane
34:Okayama
35:Hiroshima
36:Yamaguchi
37:Tokushima
38:Kagawa
39:Ehime
40:Kochi
41:Fukuoka
42:Saga
43:Nagasaki
44:Kumamoto
45:Oita
46:Miyazaki
47:Kagoshima
48:Okinawa
"""

with open("C:/HIdaka ryo/Python/コロナ感染者数リスト/newly_confirmed_cases_daily.csv","r",encoding="UTF-8")as f:
    alllines = f.readlines()

row_num = len(alllines)
print(row_num)

date_list = []
pos_list = []
all_list = []

for row_n in range(1,49):# alllines(1::48)でもOK!!　間を空白にしてても問題ない。
    date,pos,num = alllines[row_n].split(",") # row_n にはint(セルNo)が代入されている。　alllines[row_n]で全件リストのセルを呼びだしている。
    all = int(num.replace("\n", "" )) 
    #print(f"日本全国の日別コロナ感染者数:{date}は、{all}人です。")
    date_list.append(date)
    pos_list.append(pos)
    all_list.append(all)


with open("C:/HIdaka ryo/Python/コロナ感染者数リスト/都道府県リスト.csv","w",encoding="UTF-8")as d:
    for result in zip(date_list,pos_list,all_list):
        #d.write(f"日本全国の日別コロナ感染者数:{result[0]}は、{result[2]:5d}人です。\n")
        d.write(f"{result[1]}\n")