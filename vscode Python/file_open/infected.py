alllines = []
with open("C:/HIdaka ryo/Python/file_open/newly_confirmed_cases_daily.csv","r",encoding="UTF-8")as f:
    for i in range(28129):
        alines = f.readline()
        alllines.append(alines)

print(f"READ DATA is {alllines}")