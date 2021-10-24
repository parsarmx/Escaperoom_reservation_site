# this function take a weekday and convert it to persian week days
def week_day_convert(day):
    if day == 'Saturday':
        return 'شنبه'
    elif day == 'Sunday':
        return 'یکشنبه'
    elif day == 'Monday':
        return 'دوشنبه'
    elif day == 'Tuesday':
        return 'سشنبه'
    elif day == 'Wednesday':
        return 'چهارشنبه'
    elif day == 'Thursday':
        return 'پنجشنبه'
    elif day == 'Friday':
        return 'جمعه'


# this method does the same thing for months
def month_convertor(month):
    if month == 1:
        return 'فروردین'
    elif month == 2:
        return 'اردیبهشت'
    elif month == 3:
        return 'خرداد'
    elif month == 4:
        return 'تیر'
    elif month == 5:
        return 'مرداد'
    elif month == 6:
        return 'شهریور'
    elif month == 7:
        return 'مهر'
    elif month == 8:
        return 'آبان'
    elif month == 9:
        return 'آذر'
    elif month == 10:
        return 'دی'
    elif month == 11:
        return 'بهمن'
    elif month == 12:
        return 'اسفند'
