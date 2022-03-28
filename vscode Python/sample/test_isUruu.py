import dateCalc

print("閏年判定プログラムテスト")
testData = ( 1, 2, 3, 4, 5, 99, 100, 101, 399, 400, 401 )
for year in testData :
    print( f"{year} : {dateCalc.isUruu( year )}" )
