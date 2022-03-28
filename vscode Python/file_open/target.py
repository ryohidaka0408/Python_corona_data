
alllines = []
with open("C:/HIdaka ryo/Python/file_open/test_target.csv","r",encoding="UTF-8")as f:
    for i in range(4):
        alines = f.readline()
        alllines.append(alines)

print(f"READ DATA is {alllines}")

with open("C:/HIdaka ryo/Python/file_open/result_target.csv","w",encoding="UTF-8")as d:
    # 読み込み/書き込み処理の記入
    d.write(f"{alllines[0]}{alllines[1]}{alllines[2]}{alllines[3]}")
