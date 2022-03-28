with open("C:/HIdaka ryo/Python/file_open/test2.txt","w",encoding="UTF-8")as d:
    # 読み込み/書き込み処理の記入
    str = "Hello Python"
    d.write(str)
    d.write("ここ")
    d.write("場所の指定が大事")

with open("C:/HIdaka ryo/Python/file_open/test2.txt","r",encoding="UTF-8")as f:
    data = f.read()

print(f"READ DATA is [{data}]")