alllines = []
with open("C:/HIdaka ryo/Python/file_open/mode=.txt","r",encoding="UTF-8")as f:
    for i in range(10):
        alines = f.readline()
        alllines.append(alines)

print(f"READ DATA is {alllines}")

with open("C:/HIdaka ryo/Python/file_open/mode一覧表.csv","w",encoding="UTF-8")as d:
    # 読み込み/書き込み処理の記入
    d.write(f"{alllines[0]}{alllines[1]}{alllines[2]}{alllines[3]}{alllines[4]}{alllines[5]}{alllines[6]}{alllines[7]}{alllines[8]}{alllines[9]}")