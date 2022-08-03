import sys
sys.stdin = open('input.txt','r')
from datetime import date
year, month, day = map(int, input().split())
f_year, f_month, f_day = map(int, input().split())

date_now = date(year, month, day)
date_future = date(f_year, f_month, f_day)
day = date_future - date_now

dday = day.days

if dday < 365243:
    print(f'D-{dday}')
else:
    print('gg')


# if f_year - year != 0:
#     for i in range(year, f_year):
#         yun = False
#         if i % 4 == 0:
#             yun = True
#             if i % 100 == 0:
#                 yun = False
#                 if i % 400 == 0:
#                     yun = True
#         if yun == True:
#             days += 366
#         else:
#             days += 365
# yun = False
# if year % 4 == 0:
#     yun = True
#     if year % 100 == 0:
#         yun = False
#         if year % 400 == 0:
#             yun = True
# if yun == False:
#     for i in range(1, month + 1):
#         if i == 2:
#             days -= 28
#         elif i < 8:
#             if i % 2:
#                 days -= 31
#             else:
#                 days -= 30
#         else:
#             if i % 2:
#                 days -= 30
#             else:
#                 days -= 31
# else:
#     for i in range(1, month + 1):
#         if i == 2:
#             days -= 29
#         elif i < 8:
#             if i % 2:
#                 days -= 31
#             else:
#                 days -= 30
#         else:
#             if i % 2:
#                 days -= 30
#             else:
#                 days -= 31
    
# days -= day
# yun = False
# if f_year % 4 == 0:
#     yun = True
#     if f_year % 100 == 0:
#         yun = False
#         if f_year % 400 == 0:
#             yun = True
# if yun == False:
#     for i in range(1, f_month + 1):
#         if i == 2:
#             days += 28
#         elif i < 8:
#             if i % 2:
#                 days += 31
#             else:
#                 days += 30
#         else:
#             if i % 2:
#                 days += 30
#             else:
#                 days += 31
# else:
#     for i in range(1, f_month + 1):
#         if i == 2:
#             days += 29
#         elif i < 8:
#             if i % 2:
#                 days += 31
#             else:
#                 days += 30
#         else:
#             if i % 2:
#                 days += 30
#             else:
#                 days += 31
# days += f_day