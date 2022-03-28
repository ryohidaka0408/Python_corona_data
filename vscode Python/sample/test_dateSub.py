import dateCalc

wy, wm, wd = input( "日付1 > " ).split("/")
date1 = ( int(wy), int(wm), int(wd) )
wy, wm, wd = input( "日付2 > " ).split("/")
date2 = ( int(wy), int(wm), int(wd) )

days = dateCalc.dateSub( date1, date2 )
print( f"{date1[0]}年{date1[1]}月{date1[2]}日から{date2[0]}年{date2[1]}月{date2[2]}は{days}日間" )

import datetime
d1 = datetime.date(date1[0], date1[1], date1[2])
d2 = datetime.date(date2[0], date2[1], date2[2])
print( f"答合せ {d2-d1}" )
