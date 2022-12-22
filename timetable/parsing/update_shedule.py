
import psycopg2
from psycopg2 import Error
import datetime
import json
import os

def update_shedule_db(data):
    try:
    # Подключиться к существующей базе данных
        connection = psycopg2.connect(database=os.getenv("NAME"), 
                                    user=os.getenv("USER"), 
                                    password=os.getenv("PASSWORD"), 
                                    host=os.getenv("HOST"), 
                                    port=os.getenv("PORT"))

        # Создайте курсор для выполнения операций с базой данных
        lesson = 'lesson_name'
        teacher = 'teacher'
        audience = 'audience'
        
        
        cursor = connection.cursor()
        time = ["08:30:00", "10:00:00", "11:40:00", "13:30:00", "15:00:00", "16:30:00"]
        dayweek = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
        for groups in data:
            for i in range(0, len(dayweek)):
                for date in data[groups][dayweek[i]]:
                    for x in range(0, len(time)):
                        datetime_object = datetime.datetime.strptime(f'{date} {time[x]}', '%Y-%m-%d %H:%M:%S')
                        # try:
                        #     if "Дисциплина" in groups:
                        #         continue
                            
                        #     cursor.execute(f"SELECT EXISTS (SELECT * FROM timetable_group WHERE \"group\" = '{groups}')")
                        #     group_check = cursor.fetchone()

                        #     if group_check[0]:
                        #         continue
                        #     else:
                        #         cursor.execute(f"INSERT INTO  public.timetable_group VALUES ('{groups}')")
                            
                                
                        # except (Exception, Error) as error:
                        #     print('Ошибка возникает тут: ', error)
                        #     continue
                    
                        try:
                            for j in range(1, 3):
                                cursor.execute(f"SELECT EXISTS (SELECT * FROM timetable_lesson WHERE lesson = '{data[groups][dayweek[i]][date][time[x]][lesson][str(j)]}')")
                                lesson_check = cursor.fetchone()
                                
                                if lesson_check[0]:
                                    continue
                                else:
                                    cursor.execute(f"INSERT INTO public.timetable_lesson VALUES ('{data[groups][dayweek[i]][date][time[x]][lesson][str(j)]}')")
                            
                        except (Exception, Error) as error:
                            print('Ошибка возникает тут: ', error)
                            continue
                        
                        try:
                            for j in range(1, 3):
                                
                                cursor.execute(f"SELECT EXISTS (SELECT * FROM timetable_teacher WHERE teacher = '{data[groups][dayweek[i]][date][time[x]][teacher][str(j)]}')")
                                teacher_check = cursor.fetchone()
                                
                                if teacher_check[0]:
                                    continue
                                else:
                                    cursor.execute(f"INSERT INTO public.timetable_teacher VALUES ('{data[groups][dayweek[i]][date][time[x]][teacher][str(j)]}')") 
                                    
                        except (Exception, Error) as error:
                            print('Ошибка возникает тут: ', error)
                            continue 
                        # # # {time[x]}

                        try:
                            for j in range(1, 2 + 1):
                                
                                cursor = connection.cursor()
                                cursor.execute(f"INSERT INTO public.timetable_timetable (day_name_id, audience, lesson_name_id, datetime, group_id, teacher_id) VALUES ('{dayweek[i]}', '{data[groups][dayweek[i]][date][time[x]][audience][str(j)]}', '{data[groups][dayweek[i]][date][time[x]][lesson][str(j)]}', '{datetime_object}', '{groups}', '{data[groups][dayweek[i]][date][time[x]][teacher][str(j)]}') ")
                                connection.commit()
                            
                        except (Exception, Error) as error:
                            print('Ошибка возникает тут: ', error)
                            continue   
                            
                                
            # cursor.execute(f"INSERT INTO public.timetable_lesson VALUES ('{(data[group][dayweek[0]][time[0]][lesson])}')")
            
            # cursor.execute(f"INSERT INTO public.timetable_group VALUES ('ИС-22') ")
            # cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'timetable_group'")
            # cursor.execute("SELECT group FROM public.timetable_group")
            
            # record = cursor.fetchall()
            # Получить результат
            connection.commit()
            print("Запись вставлена")
            # for x in record:
            #     print("*" * 100)
            #     print(f'Группа: {x[0]}')
            #     # print(f'Название урока: {x[2]}')
                # print(f'Кабинет: {x[1]}')
                # print(f'Дата: {x[3].time()}')
                # print(f'Группа: {x[4]}')
                # print(f'Преподаватель: {x[5]}')

        
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
    
    # print(dictionary[0][3])
    
# def update_date(data_list):
#     date = []
#     for dates in data_list[0][1]:
#         if dates == None or dates == "Дата ":
#             continue
#         else:
#             # dates = 
#             finish_date = datetime.datetime.date.today().strftime(f"%Y-%m-{dates}")
#             date.append(finish_date)
            
#     return date


# def update_date():
#     date_monday = datetime.datetime.strptime(get_date, "%Y-%m-%d").date()
#     date = [f'{date_monday}', f'{date_monday + datetime.timedelta(days=1)}', f'{date_monday + datetime.timedelta(days=2)}', f'{date_monday + datetime.timedelta(days=3)}', f'{date_monday + datetime.timedelta(days=4)}']
#     return date


def update_shedule(data_list, data2, get_date):
    date_monday = datetime.datetime.strptime(get_date, "%Y-%m-%d").date() + datetime.timedelta(days=3)
    date = [f'{date_monday}', f'{date_monday + datetime.timedelta(days=1)}', f'{date_monday + datetime.timedelta(days=2)}', f'{date_monday + datetime.timedelta(days=3)}', f'{date_monday + datetime.timedelta(days=4)}']

    # temp = 0 
    i = -2
    # q = 0
    group = data_list[0][3][0]
    audience = False
    teacher = False
    lesson = False
    day = 0
    dayweek = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    
    
    dayofweek_dict = {f"{dayweek[0]}": {f"{date[0]}": {"08:30:00": {"lesson": {"1": "", "2": ""}, 
                                                       "audience": {"1": "", "2": ""}, 
                                                       "teacher": {"1": "", "2": ""} }}},
                    f"{dayweek[1]}": {f"{date[1]}": {"08:30:00": {"lesson": {"1": "", "2": ""}, 
                                                       "audience": {"1": "", "2": ""}, 
                                                       "teacher": {"1": "", "2": ""} }}},
                    f"{dayweek[2]}": {f"{date[2]}": {"08:30:00": {"lesson": {"1": "", "2": ""}, 
                                                       "audience": {"1": "", "2": ""}, 
                                                       "teacher": {"1": "", "2": ""} }}},
                    f"{dayweek[3]}": {f"{date[3]}": {"08:30:00": {"lesson": {"1": "", "2": ""}, 
                                                       "audience": {"1": "", "2": ""}, 
                                                       "teacher": {"1": "", "2": ""} }}},
                    f"{dayweek[4]}": {f"{date[4]}": {"08:30:00": {"lesson": {"1": "", "2": ""}, 
                                                       "audience": {"1": "", "2": ""}, 
                                                       "teacher": {"1": "", "2": ""} }}},
                    }
    data = {group: dayofweek_dict}
    for x in range(3, 30):
        for lessons_and_group in data_list[0][x]:
            
            if i == 38 or lessons_and_group == "Э-14" or lessons_and_group == "ПБ-37":
                data2.update(data)
                # temp += 1
                i = -2
                day = 0
                
            if lessons_and_group == None:
                continue
                
            # print(lessons_and_group)
            if lessons_and_group == "Преподаватель":
                audience = False
                lesson = False
                teacher = True
                i = -1
                day = 0
                continue
            
            if lessons_and_group == " каб.":
                teacher = False
                lesson = False
                audience = True
                i = -1
                day = 0
                continue
            
            i += 1
                
            if i % 8 == 0 and day != 5:
                dates = date[day]
                days = dayweek[day]
                day += 1
                if day >= 2:
                    i += 1
            
            if i == -1:
                group = lessons_and_group
                dayofweek_dict = {f"{dayweek[0]}": {f"{date[0]}": {"08:30:00": {"lesson": {"1": "", "2": ""},
                                                                                "audience": {"1": "", "2": ""}, 
                                                                                "teacher": {"1": "", "2": ""} }}},
                    f"{dayweek[1]}": {f"{date[1]}": {"08:30:00": {"lesson": {"1": "", "2": ""}, 
                                                                  "audience": {"1": "", "2": ""}, 
                                                                  "teacher": {"1": "", "2": ""} }}},
                    f"{dayweek[2]}": {f"{date[2]}": {"08:30:00": {"lesson": {"1": "", "2": ""}, 
                                                                  "audience": {"1": "", "2": ""}, 
                                                                  "teacher": {"1": "", "2": ""} }}},
                    f"{dayweek[3]}": {f"{date[3]}": {"08:30:00": {"lesson": {"1": "", "2": ""}, 
                                                                  "audience": {"1": "", "2": ""}, 
                                                                  "teacher": {"1": "", "2": ""} }}},
                    f"{dayweek[4]}": {f"{date[4]}": {"08:30:00": {"lesson": {"1": "", "2": ""}, 
                                                                  "audience": {"1": "", "2": ""}, 
                                                                  "teacher": {"1": "", "2": ""} }}},
                    }
                
                data.update({group: dayofweek_dict})
                continue

            if "Дисциплина" in lessons_and_group:
                teacher = False
                audience = False
                lesson = True
                continue
            
            if (teacher or audience) and i == 0:
                i += 1
            
            # if lessons_and_group == "Ховякова Е.Ю.":
            #     lessons_and_group = lessons_and_group.split("1п")
            #     lessons_and_group.append('')
            
            
            if "Иностранный язык" in lessons_and_group:
                lessons_and_group = lessons_and_group.split("1п")
                lessons_and_group.append(f"{lessons_and_group[0]}")
            if "1п " in lessons_and_group and "2п" in lessons_and_group and "Иностранный язык" not in lessons_and_group[0]:
                lessons_and_group = lessons_and_group.split("1п")
                lessons_and_group[0] += "1п"
                lessons_and_group[1].lstrip(" ")
            elif "1п" in lessons_and_group:
                lessons_and_group = lessons_and_group.split("1п")
                lessons_and_group[0] += "1п"
            elif lesson and "Иностранный язык" not in lessons_and_group[0] and type(lessons_and_group) != list:
                lessons_and_group = lessons_and_group.split("1п")
                lessons_and_group.append('')
            elif audience and lessons_and_group != " " and type(lessons_and_group) != list:
                lessons_and_group = lessons_and_group.split(" ")
            elif teacher and lessons_and_group != " " and type(lessons_and_group) != list:
                lessons_and_group = lessons_and_group.split(". ")
                lessons_and_group[0] += "."
            if len(lessons_and_group) != 2:
                if type(lessons_and_group) == list:
                    lessons_and_group.append('')
                else:
                    lessons_and_group.rstrip(' ')
                    lessons_and_group = lessons_and_group.split("1п")
                    lessons_and_group.append('')
                    
            
                
                
            if i % 8 == 1 and i != 8 * day:
                if lesson:
                    data[group][days][dates]["08:30:00"] = {"lesson_name": {"1": lessons_and_group[0], "2": lessons_and_group[1]}}
                if audience:
                    data[group][days][dates]["08:30:00"].update({"audience": {"1": lessons_and_group[0], "2": lessons_and_group[1]}})
                if teacher:
                    data[group][days][dates]["08:30:00"].update({"teacher": {"1": lessons_and_group[0], "2": lessons_and_group[1]}})
            if i % 8 == 2 and i != 8 * day:
                if lesson:
                    data[group][days][dates]["10:00:00"] = {"lesson_name": {"1": lessons_and_group[0], "2": lessons_and_group[1]}}
                if audience:
                    data[group][days][dates]["10:00:00"].update ({"audience": {"1": lessons_and_group[0], "2": lessons_and_group[1]}})
                if teacher:
                    data[group][days][dates]["10:00:00"].update({"teacher": {"1": lessons_and_group[0], "2": lessons_and_group[1]}})
            if i % 8 == 3 and i != 8 * day:
                if lesson:
                    data[group][days][dates]["11:40:00"] = {"lesson_name": {"1": lessons_and_group[0], "2": lessons_and_group[1]}}
                if audience:
                    data[group][days][dates]["11:40:00"].update ({"audience": {"1": lessons_and_group[0], "2": lessons_and_group[1]}})
                if teacher:
                    data[group][days][dates]["11:40:00"].update({"teacher": {"1": lessons_and_group[0], "2": lessons_and_group[1]}})
            if i % 8 == 4 and i != 8 * day:
                if lesson:
                    data[group][days][dates]["13:30:00"] = {"lesson_name": {"1": lessons_and_group[0], "2": lessons_and_group[1]}}
                if audience:
                    data[group][days][dates]["13:30:00"].update({"audience": {"1": lessons_and_group[0], "2": lessons_and_group[1]}})
                if teacher:
                    data[group][days][dates]["13:30:00"].update({"teacher": {"1": lessons_and_group[0], "2": lessons_and_group[1]}} )
            if i % 8 == 5 and i != 8 * day:
                if lesson:
                    data[group][days][dates]["15:00:00"] = {"lesson_name": {"1": lessons_and_group[0], "2": lessons_and_group[1]}}
                if audience:
                    data[group][days][dates]["15:00:00"].update({"audience": {"1": lessons_and_group[0], "2": lessons_and_group[1]}})
                if teacher:
                    data[group][days][dates]["15:00:00"].update({"teacher": {"1": lessons_and_group[0], "2": lessons_and_group[1]}})
            if i % 8 == 6 and i != 8 * day:
                if lesson:
                    data[group][days][dates]["16:30:00"] = {"lesson_name": {"1": lessons_and_group[0], "2": lessons_and_group[1]}}
                if audience:
                    data[group][days][dates]["16:30:00"].update ({"audience": {"1": lessons_and_group[0], "2": lessons_and_group[1]}})
                if teacher:
                    data[group][days][dates]["16:30:00"].update({"teacher": {"1": lessons_and_group[0], "2": lessons_and_group[1]}})
            if i % 8 == 7 and i != 8 * day:
                if lesson:
                    data[group][days][dates]["18:00:00"] = {"lesson_name": {"1": lessons_and_group[0], "2": lessons_and_group[1]}} 
                if audience:
                    data[group][days][dates]["18:00:00"].update({"audience": {"1": lessons_and_group[0], "2": lessons_and_group[1]}})
                if teacher:
                    data[group][days][dates]["18:00:00"].update({"teacher": {"1": lessons_and_group[0], "2": lessons_and_group[1]}}) 
                    
                    
        # print(data)
        # print('*' * 100)
        
        

        print(data2)

    with open(f'data.json', 'w', encoding='utf-8') as file:
        json.dump(data2, file, indent=4, ensure_ascii=False)

    

# def update_shedule(data_list):
#     for x in range(3, 30):
#         for lessons_and_group in data_list[0][x]:
#             if lessons_and_group == "Преподаватель":
#                 print("YEEP")
                
            
        
    
# update_shedule_db(data='ds')