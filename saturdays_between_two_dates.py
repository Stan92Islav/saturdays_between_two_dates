'''Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция должна возвращать количество суббот между датами start и end включительно.

Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.'''


from datetime import date

def saturdays_between_two_dates(start, end):
    if start < end:
        a = list(range(start.toordinal(), end.toordinal() + 1))
    else:
        a = list(range(end.toordinal(), start.toordinal() + 1))

    b = [date.fromordinal(i) for i in a]
    count = 0
    for i in b:
        if i.weekday() == 5:
            count += 1
    return count

