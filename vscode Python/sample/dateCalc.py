#                       1   2   3   4   5   6   7   8   9  10  11  12
days_in_month = ( ( 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ),\
                  ( 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ) )

# 閏年判定
# 引数：西暦年
# 返値：True(閏年) / False(平年)
def isUruu( year ) :
    if year % 400 == 0 :
        return True
    elif year % 100 == 0 :
        return False
    elif year % 4 == 0 :
        return True

    return False

# 日付妥当性チェック
# 引数：年 月 日
# 返値：True(OK) / False(NG)
def dateCheck( year, month, day ) :
    if not ( 1 <= year <= 5000 ) :
        return False
    
    if not ( 1 <= month <= 12 ) :
        return False

    if isUruu( year ) == True :
        uruu = 1
    else :
        uruu = 0

    if  not ( 1 <= day <= days_in_month[uruu][month] ) :
        return False
    
    return True

# 指定日付がその年の1月1日から数えて通算何日目かを計算する
# 1月1日を指定された場合1、平年12月31日を指定された場合365を返す
# 引数：年 月 日
# 返値：日数
#       ただし、日付不当の場合は-1を返す
def from_1_1( year, month, day ) :
    # 妥当性チェック
    if dateCheck( year, month, day ) == False :
        return -1

    # 閏年判定
    if isUruu( year ) == True :
        uruu = 1
    else :
        uruu = 0

    # 算出
    answer = 0
    for m in range(1, month) :
        answer += days_in_month[uruu][m]
    
    answer += day

    return answer


# 指定日付が西暦1年1月1日から数えて通算何日目かを計算する
# 引数：年 月 日
# 返値：日数
#       ただし、日付不当の場合は-1を返す
def from_1_1_1( year, month, day ) :
    # 妥当性チェック
    if dateCheck( year, month, day ) == False :
        return -1

    # 算出
    answer = 0
    for y in range(1, year) :
        if isUruu(y) == True :
            answer += 366
        else :
            answer += 365
    
    answer += from_1_1( year, month, day )

    return answer

# 日数差算出
# 引数：年月日1 年月日2
#       引数は2個のタプルとして受け取る
# 戻り値：日数
def dateSub( date1, date2 ) :
    days1 = from_1_1_1( date1[0], date1[1], date1[2] )
    days2 = from_1_1_1( date2[0], date2[1], date2[2] )

    return days2 - days1

# 曜日算出
# 引数：年 月 日
# 戻り値：曜日
def weekday( year, month, day ) :
    youbiText = ( "日", "月", "火", "水", "木", "金", "土" )
    days = from_1_1_1( year, month, day )
    return youbiText[days % 7]

# 目的日付算出
# 引数：年月日 日数
#       年月日はタプルで受け取る
# 戻り値：目的の日付
#         戻り値はタプル
def targetDate( baseDate, days ) :
    targetDays = from_1_1_1( baseDate[0], baseDate[1], baseDate[2] ) + days

    year = 1
    while targetDays > 365 + isUruu( year ) :
        targetDays -= ( 365 + isUruu( year ) )
        year += 1
    
    for month in range(1, 12) :
        if targetDays > days_in_month[isUruu(year)][month] :
            targetDays -= days_in_month[isUruu(year)][month]
        else :
            break
    
    return ( year, month, targetDays )
            
