import dateCalc

print("通算日数算出プログラムテスト")
      
for m in range( 1, 12 + 1 ) :
    for d in range( 1, dateCalc.days_in_month[0][m] + 1 ) :
        print( f"2021/{m}/{d} は {dateCalc.from_1_1( 2021, m, d )} 日目" )

m, d = 2, 28
print( f"2020/{m}/{d} : {dateCalc.from_1_1( 2020, m, d )}" )
m, d = 2, 29
print( f"2020/{m}/{d} : {dateCalc.from_1_1( 2020, m, d )}" )
m, d = 3, 1
print( f"2020/{m}/{d} : {dateCalc.from_1_1( 2020, m, d )}" )
m, d = 12, 31
print( f"2020/{m}/{d} : {dateCalc.from_1_1( 2020, m, d )}" )
