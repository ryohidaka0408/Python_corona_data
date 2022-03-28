
alllines = []
with open("C:/HIdaka ryo/Python/file_open/mode=.txt","r",encoding="UTF-8")as f:
    for i in range(9):
        alines = f.readline()
        alllines.append(alines)

print(f"READ DATA is {alllines}")

""" 実行結果

READ DATA is ['mode=一覧表,説明書き\n', 'mode = r,読み書き\n', 'mode = w,書き込み\n', 'mode = a,追記\n',
'mode = r+,既存ファイルの読み書き\n', 'mode = w+,新規ファイルの読み書き\n', 'mode = a+,追記・書き込み\n',
'mode = t,テキストモード\n', 'mode = b,バイナリモード']

"""