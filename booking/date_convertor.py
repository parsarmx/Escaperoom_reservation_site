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
    if month == 'Farvardin' or 1:
        return 'فروردین'
    elif month == 'Ordibehesht' or 2:
        return 'اردیبهشت'
    elif month == 'Khordad' or 3:
        return 'خرداد'
    elif month == 'Tir' or 4:
        return 'تیر'
    elif month == 'Mordad' or 5:
        return 'مرداد'
    elif month == 'Shahrivar' or 6:
        return 'شهریور'
    elif month == 'Mehr' or 7:
        return 'مهر'
    elif month == 'Aban' or 8:
        return 'آبان'
    elif month == 'Azar' or 9:
        return 'آذر'
    elif month == 'Dey' or 10:
        return 'دی'
    elif month == 'Bahman' or 11:
        return 'بهمن'
    elif month == 'Esfand' or 12:
        return 'اسفند'
