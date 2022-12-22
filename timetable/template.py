from csv import get_dialect
from django import template
from django.utils import timezone

from .models import *

tz = timezone.get_default_timezone()

register = template.Library()



@register.filter
def to_str(value):
    """converts int to string"""
    return str(value)


@register.filter
def time(value):
    return(value.astimezone(tz).strftime("%H:%M:%S"))

# from .parsing.parsing_site import file_info
from .views import student_shedule, teacher_shedule

dayweek = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]

@register.filter
def get_current_monday(value):
    global current_monday
    current_monday = value
    return value

@register.filter
def student_day(value, arg):
    date_list = student_shedule(group_name="date_list", request="", get_date=f"{current_monday}")
    
    # dates = Timetable.objects.filter(day_name="Понедельник").order_by('datetime')
    # preDate = []
    
    # for x in dates:
    #     preDate.append(x.datetime.date().strftime('%Y-%m-%d'))
    
    # date = list(set(preDate))
    # monday = max(date)
    
    # date_list = [f'{monday}', f'{(datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")}', f'{(datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=2)).strftime("%Y-%m-%d")}', f'{(datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")}', f'{(datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=4)).strftime("%Y-%m-%d")}']
    
    Date = {f'{dayweek[0]}': f'{date_list[0]}', f'{dayweek[1]}': f'{date_list[1]}', f'{dayweek[2]}': f'{date_list[2]}', f'{dayweek[3]}': f'{date_list[3]}', f'{dayweek[4]}': f'{date_list[4]}'}
    for day in dayweek:
        if f"{day}" in arg:
            for x in range(1, 6 + 1):
                if f"{x}Пара" in arg:
                    for z in range(1, 2 + 1):    
                        if f"Пара{z}" in arg:
                            if "Название" in arg:
                                if value[f"{day}"][f"{Date.get(day)}"][f"{x}"]["lesson"][f"{z}"] == "":
                                    return ""
                                else:
                                    return value[f"{day}"][f"{Date.get(day)}"][f"{x}"]["lesson"][f"{z}"]
                            if "Кабинет" in arg:
                                if value[f"{day}"][f"{Date.get(day)}"][f"{x}"]["audience"][f"{z}"] == "":
                                    return ""
                                else:
                                    return value[f"{day}"][f"{Date.get(day)}"][f"{x}"]["audience"][f"{z}"]
                            if "Преподаватель" in arg:
                                if value[f"{day}"][f"{Date.get(day)}"][f"{x}"]["audience"][f"{z}"] == "":
                                    return ""
                                else:
                                    return value[f"{day}"][f"{Date.get(day)}"][f"{x}"]["teacher"][f"{z}"]


@register.filter
def teacher_day(value, arg):
    date_list = teacher_shedule(teacher_name="date_list", request="", get_date=f"{current_monday}")
    
    Date = {f'{dayweek[0]}': f'{date_list[0]}', f'{dayweek[1]}': f'{date_list[1]}', f'{dayweek[2]}': f'{date_list[2]}', f'{dayweek[3]}': f'{date_list[3]}', f'{dayweek[4]}': f'{date_list[4]}'}
    
    for day in dayweek:
        if f"{day}" in arg:
            for x in range(1, 6 + 1):
                if f"{x}Пара" in arg:
                    if "Название" in arg:
                        if value[f"{day}"][f"{Date.get(day)}"][f"{x}"]["lesson"] == "":
                            return ""
                        else:
                            return value[f"{day}"][f"{Date.get(day)}"][f"{x}"]["lesson"]
                    if "Кабинет" in arg:
                        if value[f"{day}"][f"{Date.get(day)}"][f"{x}"]["audience"] == "":
                            return ""
                        else:
                            return value[f"{day}"][f"{Date.get(day)}"][f"{x}"]["audience"]
                    if "Группа" in arg:
                                if value[f"{day}"][f"{Date.get(day)}"][f"{x}"]["group"] == "":
                                    return ""
                                else:
                                    return value[f"{day}"][f"{Date.get(day)}"][f"{x}"]["group"]