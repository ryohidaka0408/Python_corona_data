
def postscript():
    with open("C:/HIdaka ryo/Python/ToDoList/ToDo.csv","a",encoding="UTF-8")as out:
    # 読み込み/書き込み処理の記入
        do = input("項目の追加を入力してください")
        out.write(do)