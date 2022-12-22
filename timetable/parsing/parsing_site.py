#ver 1.0 by Leonid, with some remake ST

import ssl
import requests # Библиотека для работы с сайтом КГПК и получения файла Excel
from os import listdir # Для нахождения файла в каталоге и получение его имени для дальнейшего использывания
import openpyxl  # Библиотека для работы с Excel
# from shedule.timetable.parsing.update_shedule import update_date
from update_shedule import update_shedule
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#Функция для загрузки Excel файла
def download_file():
    site_href = "https://kg-college.ru/studentam/raspisanie" #Ссылка на расписание
    site_query = requests.get(site_href, verify=False) # Получение сайта

    if site_query.status_code != 200: # Проверка на работоспособность сайта
        return False 

    text_list = site_query.text.split() # Разделение всего html-скрипта на отдельные слова, для более удобного взаимодействия парсером

    # Получение ссылки
    for i in range(len(text_list)): # Цикл в котором обходим весь html скрипт
        if "№2</h2><p><a" in text_list[i]: # Нахождение нужной нам строки кода
            file = text_list[i + 1].replace("href=", "").replace("><b>Скачать", "")[2:-1] # Благодаря .replace мы убираем не нужный текст для ссылки
            file_link = requests.get(f"https://kg-college.ru/{file}", verify=False) # Получение нужного нам файла (Первоначально это Учебный Корпус №2).

            if file_link.status_code != 200: # Проверка на возможность скачать (Отзыв сайта *Статус*)
                return False

            file_name = file.replace("/files/studentam/raspisanie/", "").split("?") # Создание имени файла
            #Запись скаченного файла локально на сервер
            # file = open(f"{file_name[1]}_{file_name[0].split('.')[0]}.xlsx", "wb")
            file = open(f"{file_name[1]}_schedule2.xlsx", "wb")
            file.write(file_link.content)
            file.close()
#Получение информации по поводу 
def file_info(mode=None):
    file = listdir() # Для поиска файла в локальной директории
    file_list = [] # Список локальных файлов

    for i in range(len(file)): # Цикл для определения нужного нам имени(Excel файла)
        if "schedule2" in file[i] and ".~lock." not in file[i]: # При условии, что файл имеет в названии "schedule2" и он не имеет в названии ".~lock."
            parse_name_file = file[i].split("-")[1].split(".") # Определили какой у нас файл
            day = parse_name_file[0] # Берем из него день...
            month = parse_name_file[1] # Месяц
            year = parse_name_file[2].split("_")[0] # И год
            time_file = file[i].split("-")[0] # Берем первую часть файла
            
            
            if mode == "time":
                file_list.append(time_file)
            elif mode == "date":
                file_list.append(f"{year}-{month}-{day}")

            else:
                file_list.append(file[i])
    if mode == "date" or mode == "time":
        file_list.sort()
        file_list.reverse()
    return file_list

# Всё что связано с парсером
def parser_schedule(): #data_list, column, x
    
    offset_cell = (8, 44) # Работа со строками в Excel
    file_list = file_info()
    data2 = {}
    dates = file_info("date")
    # dates = pre_dates[0]
    
    for x in range(0, 6):
        column = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD"] # Колонки Excel
        data_list = [[[] for _ in range(len(column))] for _ in range(len(file_info()))]

        for iRange_file in range(len(file_list)):
            workbook = openpyxl.load_workbook(f'{file_list[len(file_list) - 1]}') # Открываем и работаем с нужным нам файлом iRange_file
            workbook_sheet = workbook[workbook.sheetnames[x]] # Листы в Excel берутся по id-шно

            # data_list[iRange_file].append([file_info("time"), file_info("date")]) // Добавление списка даты

            for iRange_column in range(len(column)):
                for iRange_cell in range(offset_cell[0], offset_cell[1]): # offset_cell посмотри и будет понятно, что тут идет обращение по id
                    cell = workbook_sheet[f"{column[iRange_column]}{iRange_cell}"].value
                    data_list[iRange_file][iRange_column].append(cell)
    
        
        # print(data_list)
        
        update_shedule(data_list, data2, dates[0])
        
        
        # print("*" * 100)
        
    

def create_parser():
    pass
    # for x in range(0, 6):
         # Конечный результат

        # return parser_schedule(data_list, column, x) 

#Вывод в отдельный файл для дебага
def finish(data_list):
    # print(data_list)
    # update_shedule(data_list)
    
    # print(data_list)
    # print(data_list[0])
    
    # for i in range(3, 30, 3):
    #     for x in data_list[0][i]:
    #         print(x)
    # # print(len(data_list[0][3]))
    
        # print(f'{lessons}')
        # q += 1
        # if len(data_list[0][i]) - 10 == q:
        #     i += 3
    
    # Делать JSON файл или словарь python
    print(data_list)
    
    # print(data_list)

def main():
    # download_file()
    
    # create_parser()
    parser_schedule()

if __name__ == "__main__":
    main()
