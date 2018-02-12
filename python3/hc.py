dic_date = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
dic_month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
             7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
dic_week = {1: 'Mon ', 2: 'Tue ', 3: 'Wen ',
            4: 'Thu ', 5: 'Fri ', 6: 'Sat ', 7: 'Sun '}
space = '    '  # 4 spaces
year_base = 2018
month_base = 5
week_base = 2


def is_leapyear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 172800 == 0:
        return True
    else:
        return False


def get_week_start(year, month):
    day_total = 0
    if year + ((10 / 12) * 0.1 * month) >= year_base + ((10 / 12) * 0.1 * month_base):
        change_date(year_base)
        if year > year_base:
            for i in range(month_base, 13):
                day_total += dic_date[i]
        for i in range(year_base + 1, year):
            day_total += 365
            if is_leapyear(i):
                day_total += 1
        change_date(year)
        for i in range(1, month):
            day_total += dic_date[i]
        day_residual = day_total % 7
        week = week_base + day_residual
        if week > 7:
            week -= 7
    else:
        change_date(year_base)
        for i in range(1, month_base):
            day_total += dic_date[i]
        for i in range(year + 1, year_base):
            day_total += 365
            if is_leapyear(i):
                day_total += 1
        if year < year_base:
            change_date(year)
            for i in range(month, 13):
                day_total += dic_date[i]
        day_residual = day_total % 7
        week = week_base - day_residual
        if week < 1:
            week += 7
    return week


def print_body(week_start, month):
    week = week_start
    for i in range(1, dic_date[month] + 1):
        print(str(i) + ' ' * (4 - len(str(i))), end='')
        i += 1
        week += 1
        if week == 7:
            print('\n' + space, end='')
        elif week == 8:
            week = 1


def print_month(year, month):
    week_start = get_week_start(year, month)
    print(space + 'Sun Mon Tue Wen The Fri Sat')  # head
    print(space, end='')
    if week_start != 7:
        print(space * (week_start), end='')
    print_body(week_start, month)


def change_date(year):
    global dic_date
    dic_date[2] = 28
    if is_leapyear(year):
        dic_date[2] = 29


def print_calendar(year, month):
    print()
    change_date(year)
    print(year, dic_month[month])
    print_month(year, month)
    print()


year = int(input('输入年份: '))
month = int(input('输入月份: '))
print_calendar(year, month)
