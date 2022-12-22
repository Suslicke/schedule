from django.shortcuts import render

from .models import *

global get_dates

# from .shedule_config import timetable

def index(request):
    news = News.objects.all()
    groups = Group.objects.all()
    teachers = Teacher.objects.all()

    # Хз
    # i = 0
    # for time in timetable:
    #     temp = None
    #     if time.datetime != temp:
    #         temp = time.datetime
    #     time.group
    #     time.datetime
    #     time.day_name
    
    
    teacher_name_list = []
    for x in teachers:
        if str(x) == " " or str(x) == "":
            continue
        teacher_name_list.append(str(x))
        
    teacher_name_list.sort()
        
    mainPage_dict = {
        'news': news,
        'groups': groups,
        'teachers': teacher_name_list
    }

    return render(request, 'timetable/index.html', mainPage_dict)


def student_shedule(request, group_name, get_date):
    # date = datetime.datetime.strptime(date)
    
    # get_date = datetime.datetime.date.now()
    
    dates = Timetable.objects.filter(day_name="Понедельник").order_by('datetime')
    preDate = []
    
    for x in dates:
        preDate.append(x.datetime.date().strftime('%Y-%m-%d'))
    
    
    date = list(set(preDate))
    
    all_monday = list(set(preDate))
    
    last_week = max(date)
    
    if get_date == "current" or get_date == last_week:
        monday = max(date)
        shedule = Timetable.objects.filter(group=group_name).filter(datetime__gte=monday)
    
    elif get_date != "current" or get_date != last_week:
        monday = get_date
        shedule = Timetable.objects.filter(group=group_name).filter(datetime__gte=monday).filter(datetime__lte=f'{datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=5)}')
        
    # shedule = Timetable.objects.filter(group=group_name).filter(datetime__lte=monday)
    date_list = [f'{monday}', f'{(datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")}', f'{(datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=2)).strftime("%Y-%m-%d")}', f'{(datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")}', f'{(datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=4)).strftime("%Y-%m-%d")}']
    
    if group_name == "date_list":
        return date_list
    
    groups = Group.objects.all()
    
    # создать список с днями неделями
    dayweek = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    
    # day = {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} }
    # day = {"lesson": "", "audience": "", "teacher": "" }
    timetable = {
    f'{dayweek[0]}': {f'{date_list[0]}': {
        "1": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "2": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "3": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "4": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "5": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "6": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
    }}, 
    f'{dayweek[1]}': {f'{date_list[1]}': {
        "1": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "2": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "3": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "4": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "5": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "6": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
    }}, 
    f'{dayweek[2]}': {f'{date_list[2]}': {
        "1": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "2": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "3": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "4": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "5": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "6": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
    }}, 
    f'{dayweek[3]}': {f'{date_list[3]}': {
        "1": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "2": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "3": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "4": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "5": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "6": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
    }}, 
    f'{dayweek[4]}': {f'{date_list[4]}': {
        "1": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "2": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "3": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "4": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "5": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
        "6": {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} },
    }}, 
    }
    
    for data in shedule:
        # timetable[name_day][date][f"{i}"]["lesson"]["2"] = data.lesson_name = {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} }
        # day = {"lesson": data.lesson_name, "audience": data.audience, "teacher": data.teacher}
        name_day = str(data.day_name)
        
        if name_day == "Понедельник":
            date = date_list[0]
        elif name_day == "Вторник":
            date = date_list[1]
        elif name_day == "Среда":
            date = date_list[2]
        elif name_day == "Четверг":
            date = date_list[3]
        elif name_day == "Пятница":
            date = date_list[4]
        
        if data.datetime.astimezone(tz).strftime("%H:%M:%S") == '08:30:00':
            if timetable[name_day][date]["1"]["lesson"]["1"] != '':
                if timetable[name_day][date]["1"]["lesson"]["1"] == data.lesson_name and timetable[name_day][date]["1"]["audience"]["1"] == data.audience and timetable[name_day][date]["1"]["teacher"]["1"] == data.teacher:
                    continue
                else:
                    if timetable[name_day][date]["1"]["lesson"]["1"] == data.lesson_name and timetable[name_day][date]["1"]["audience"]["1"] != data.audience and timetable[name_day][date]["1"]["teacher"]["1"] != data.teacher:
                        timetable[name_day][date]["1"]["audience"]["2"] = data.audience
                        timetable[name_day][date]["1"]["teacher"]["2"] = data.teacher
                    else:
                        timetable[name_day][date]["1"]["lesson"]["2"] = data.lesson_name
                        timetable[name_day][date]["1"]["audience"]["2"] = data.audience
                        timetable[name_day][date]["1"]["teacher"]["2"] = data.teacher
            else:
                timetable[name_day][date]["1"]["lesson"]["1"] = data.lesson_name
                timetable[name_day][date]["1"]["audience"]["1"] = data.audience
                timetable[name_day][date]["1"]["teacher"]["1"] = data.teacher
                
        elif data.datetime.astimezone(tz).strftime("%H:%M:%S") == '10:00:00':
            if timetable[name_day][date]["2"]["lesson"]["1"] != '':
                if timetable[name_day][date]["2"]["lesson"]["1"] == data.lesson_name and timetable[name_day][date]["2"]["audience"]["1"] == data.audience and timetable[name_day][date]["2"]["teacher"]["1"] == data.teacher:
                    continue
                else:
                    if timetable[name_day][date]["2"]["lesson"]["1"] == data.lesson_name and timetable[name_day][date]["2"]["audience"]["1"] != data.audience and timetable[name_day][date]["2"]["teacher"]["1"] != data.teacher:
                        timetable[name_day][date]["2"]["audience"]["2"] = data.audience
                        timetable[name_day][date]["2"]["teacher"]["2"] = data.teacher
                    else:
                        timetable[name_day][date]["2"]["lesson"]["2"] = data.lesson_name
                        timetable[name_day][date]["2"]["audience"]["2"] = data.audience
                        timetable[name_day][date]["2"]["teacher"]["2"] = data.teacher 
            else:
                timetable[name_day][date]["2"]["lesson"]["1"] = data.lesson_name
                timetable[name_day][date]["2"]["audience"]["1"] = data.audience
                timetable[name_day][date]["2"]["teacher"]["1"] = data.teacher
        elif data.datetime.astimezone(tz).strftime("%H:%M:%S") == "11:40:00":
            if timetable[name_day][date]["3"]["lesson"]["1"] != '':
                if timetable[name_day][date]["3"]["lesson"]["1"] == data.lesson_name and timetable[name_day][date]["3"]["audience"]["1"] == data.audience and timetable[name_day][date]["3"]["teacher"]["1"] == data.teacher:
                    continue
                else:
                    if timetable[name_day][date]["3"]["lesson"]["1"] == data.lesson_name and timetable[name_day][date]["3"]["audience"]["1"] != data.audience and timetable[name_day][date]["3"]["teacher"]["1"] != data.teacher:    
                        timetable[name_day][date]["3"]["audience"]["2"] = data.audience
                        timetable[name_day][date]["3"]["teacher"]["2"] = data.teacher
                    else:
                        timetable[name_day][date]["3"]["lesson"]["2"] = data.lesson_name
                        timetable[name_day][date]["3"]["audience"]["2"] = data.audience
                        timetable[name_day][date]["3"]["teacher"]["2"] = data.teacher

            else:
                timetable[name_day][date]["3"]["lesson"]["1"] = data.lesson_name
                timetable[name_day][date]["3"]["audience"]["1"] = data.audience
                timetable[name_day][date]["3"]["teacher"]["1"] = data.teacher
        elif data.datetime.astimezone(tz).strftime("%H:%M:%S") == "13:30:00":
            if timetable[name_day][date]["4"]["lesson"]["1"] != '':
                if timetable[name_day][date]["4"]["lesson"]["1"] == data.lesson_name and timetable[name_day][date]["4"]["audience"]["1"] == data.audience and timetable[name_day][date]["4"]["teacher"]["1"] == data.teacher:
                    continue
                else:
                    timetable[name_day][date]["4"]["lesson"]["2"] = data.lesson_name
                    timetable[name_day][date]["4"]["audience"]["2"] = data.audience
                    timetable[name_day][date]["4"]["teacher"]["2"] = data.teacher
            else:
                if timetable[name_day][date]["4"]["lesson"]["1"] == data.lesson_name and timetable[name_day][date]["4"]["audience"]["1"] != data.audience and timetable[name_day][date]["4"]["teacher"]["1"] != data.teacher:
                    timetable[name_day][date]["4"]["audience"]["1"] = data.audience
                    timetable[name_day][date]["4"]["teacher"]["1"] = data.teacher
                else:
                    timetable[name_day][date]["4"]["lesson"]["1"] = data.lesson_name
                    timetable[name_day][date]["4"]["audience"]["1"] = data.audience
                    timetable[name_day][date]["4"]["teacher"]["1"] = data.teacher
                    
        elif data.datetime.astimezone(tz).strftime("%H:%M:%S") == "15:00:00":
            if timetable[name_day][date]["5"]["lesson"]["1"] != '':
                if timetable[name_day][date]["5"]["lesson"]["1"] == data.lesson_name and timetable[name_day][date]["5"]["audience"]["1"] == data.audience and timetable[name_day][date]["5"]["teacher"]["1"] == data.teacher:
                    continue
                else:
                    if timetable[name_day][date]["5"]["lesson"]["1"] == data.lesson_name and timetable[name_day][date]["5"]["audience"]["1"] != data.audience and timetable[name_day][date]["5"]["teacher"]["1"] != data.teacher:
                        timetable[name_day][date]["5"]["audience"]["2"] = data.audience
                        timetable[name_day][date]["5"]["teacher"]["2"] = data.teacher
                    else:
                        timetable[name_day][date]["5"]["lesson"]["2"] = data.lesson_name
                        timetable[name_day][date]["5"]["audience"]["2"] = data.audience
                        timetable[name_day][date]["5"]["teacher"]["2"] = data.teacher
                    
            else:
                timetable[name_day][date]["5"]["lesson"]["1"] = data.lesson_name
                timetable[name_day][date]["5"]["audience"]["1"] = data.audience
                timetable[name_day][date]["5"]["teacher"]["1"] = data.teacher
        elif data.datetime.astimezone(tz).strftime("%H:%M:%S") == "16:30:00":
            if timetable[name_day][date]["6"]["lesson"]["1"] != '':
                if timetable[name_day][date]["6"]["lesson"]["1"] == data.lesson_name and timetable[name_day][date]["6"]["audience"]["1"] == data.audience and timetable[name_day][date]["6"]["teacher"]["1"] == data.teacher:
                    continue
                else:
                    if timetable[name_day][date]["6"]["lesson"]["1"] == data.lesson_name and timetable[name_day][date]["6"]["audience"]["1"] != data.audience and timetable[name_day][date]["6"]["teacher"]["1"] != data.teacher:
                        timetable[name_day][date]["6"]["audience"]["2"] = data.audience
                        timetable[name_day][date]["6"]["teacher"]["2"] = data.teacher
                    else:
                        timetable[name_day][date]["6"]["lesson"]["2"] = data.lesson_name
                        timetable[name_day][date]["6"]["audience"]["2"] = data.audience
                        timetable[name_day][date]["6"]["teacher"]["2"] = data.teacher
            else:
                timetable[name_day][date]["6"]["lesson"]["1"] = data.lesson_name
                timetable[name_day][date]["6"]["audience"]["1"] = data.audience
                timetable[name_day][date]["6"]["teacher"]["1"] = data.teacher
                
    all_monday.sort(reverse=True)
    timetable_dict = {
        'timetable': timetable,
        'groups': groups,
        'date': date_list,
        'group_name': group_name,
        'dates': all_monday,
        
    }
    
    
    return render(request, 'timetable/student_table.html', timetable_dict)
            
            

def teacher_shedule(request, teacher_name, get_date):
    dates = Timetable.objects.filter(day_name="Понедельник").order_by('datetime')
    preDate = []
    
    for x in dates:
        preDate.append(x.datetime.date().strftime('%Y-%m-%d'))
    
    date = list(set(preDate))
    
    all_monday = list(set(preDate))
    
    last_week = max(date)
    
    if get_date == "current" or get_date == last_week:
        monday = max(date)
        shedule = Timetable.objects.filter(teacher=teacher_name).filter(datetime__gte=monday)
    
    elif get_date != "current" or get_date != last_week:
        monday = get_date
        shedule = Timetable.objects.filter(teacher=teacher_name).filter(datetime__gte=monday).filter(datetime__lte=f'{datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=5)}')

    date_list = [f'{monday}', f'{(datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")}', f'{(datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=2)).strftime("%Y-%m-%d")}', f'{(datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")}', f'{(datetime.datetime.strptime(monday, "%Y-%m-%d").date() + datetime.timedelta(days=4)).strftime("%Y-%m-%d")}']
    
    if teacher_name == "date_list":
        return date_list
    
    teachers = Teacher.objects.all()
    
    # создать словарь по дням неделям
    
    dayweek = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    day = {"lesson": "", "audience": "", "group": "" }
    # day = {"lesson": "", "audience": "", "teacher": "" }
    teacher_timetable = {
    f'{dayweek[0]}': {f'{date_list[0]}': {
        "1": day,
        "2": day,
        "3": day,
        "4": day,
        "5": day,
        "6": day,
    }},
    f'{dayweek[1]}': {f'{date_list[1]}': {
        "1": day,
        "2": day,
        "3": day,
        "4": day,
        "5": day,
        "6": day,
    }},
    f'{dayweek[2]}': {f'{date_list[2]}': {
        "1": day,
        "2": day,
        "3": day,
        "4": day,
        "5": day,
        "6": day,
    }},
    f'{dayweek[3]}': {f'{date_list[3]}': {
        "1": day,
        "2": day,
        "3": day,
        "4": day,
        "5": day,
        "6": day,
    }},
    f'{dayweek[4]}': {f'{date_list[4]}': {
        "1": day,
        "2": day,
        "3": day,
        "4": day,
        "5": day,
        "6": day,
    }},
    }
    
    for data in shedule:
        # day = {"lesson": {"1": "", "2": ""}, "audience": {"1": "", "2": ""}, "teacher": {"1": "", "2": ""} }
        day = {"lesson": data.lesson_name, "audience": data.audience, "group": data.group}
        name_day = str(data.day_name)
    
        if name_day == "Понедельник":
            date = date_list[0]
        elif name_day == "Вторник":
            date = date_list[1]
        elif name_day == "Среда":
            date = date_list[2]
        elif name_day == "Четверг":
            date = date_list[3]
        elif name_day == "Пятница":
            date = date_list[4]
            
        if data.datetime.astimezone(tz).strftime("%H:%M:%S") == '08:30:00':
                teacher_timetable[name_day][date]["1"] = day
        elif data.datetime.astimezone(tz).strftime("%H:%M:%S") == '10:00:00':
                teacher_timetable[name_day][date]["2"] =day
        elif data.datetime.astimezone(tz).strftime("%H:%M:%S") == "11:40:00":
                teacher_timetable[name_day][date]["3"] = day
        elif data.datetime.astimezone(tz).strftime("%H:%M:%S") == "13:30:00":
                teacher_timetable[name_day][date]["4"] = day
        elif data.datetime.astimezone(tz).strftime("%H:%M:%S") == "15:00:00":
                teacher_timetable[name_day][date]["5"] = day
        elif data.datetime.astimezone(tz).strftime("%H:%M:%S") == "16:30:00":
                teacher_timetable[name_day][date]["6"] = day
        
    
    
    all_monday.sort(reverse=True)
    teacher_name_list = []
    for x in teachers:
        if str(x) == " " or str(x) == "":
            continue
        teacher_name_list.append(str(x))
        
    teacher_name_list.sort()
        
    timetable_dict = {
        'timetable': teacher_timetable,
        'teachers': teacher_name_list,
        'teacher_name': teacher_name,
        'date': date_list,
        'dates': all_monday
    }
    
    
    return render(request, 'timetable/teacher_table.html', timetable_dict)


# def update_shedule():
#     pass
