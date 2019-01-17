import time

print('## timestamp to format time')

t_stamp = time.time() + 86400
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t_stamp)), type(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t_stamp))))
# 2019-01-17 09:22:39 <class 'str'>
print(time.asctime(time.localtime(t_stamp)), type(time.asctime(time.localtime(t_stamp))))
# Thu Jan 17 09:22:56 2019 <class 'str'>
print(time.localtime(t_stamp), type(time.localtime(t_stamp)))
# time.struct_time(tm_year=2019, tm_mon=1, tm_mday=17, tm_hour=9, tm_min=23, tm_sec=9, tm_wday=3, tm_yday=17, tm_isdst=0) <class 'time.struct_time'>
print(time.localtime(t_stamp).tm_year, type(time.localtime(t_stamp).tm_year))
# 2019 <class 'int'>
print(time.localtime(t_stamp).tm_wday, type(time.localtime(t_stamp).tm_wday))
# 3 <class 'int'> 
# Python 3 Mon = 0, Tue = 1, ..., Sat = 5, Sun = 6
print()
print('## format time to timestamp')
print('# strptime')
print(time.strptime('2019-01-17 09:18:53', '%Y-%m-%d %H:%M:%S'), type(time.strptime('2019-01-17 09:18:53', '%Y-%m-%d %H:%M:%S')))
# time.struct_time(tm_year=2019, tm_mon=1, tm_mday=17, tm_hour=9, tm_min=18, tm_sec=53, tm_wday=3, tm_yday=17, tm_isdst=-1) <class 'time.struct_time'>
print('# mktime')
print(time.mktime(time.localtime()), type(time.mktime(time.localtime())))
# 1547692010.0 <class 'float'>
print(
    time.mktime(
        (time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday,
        time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec,
        time.localtime().tm_wday, time.localtime().tm_yday, time.localtime().tm_isdst)
    )
)
# 1547692025.0
print(time.mktime(time.strptime('2019-01-17 09:18:53', '%Y-%m-%d %H:%M:%S')), type(time.mktime(time.strptime('2019-01-17 09:18:53', '%Y-%m-%d %H:%M:%S'))))
# 1547687933.0 <class 'float'>
