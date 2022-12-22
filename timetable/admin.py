from .parsing import update_shedule

from django.contrib import admin
from .models import * 

from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import path, include


import json


# Register your models here.

admin.site.register(DayOfWeek)
admin.site.register(Lesson)
admin.site.register(Group)
admin.site.register(Teacher)

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    global entries
    entries = 0
    date_hierarchy = 'datetime'
    # ordering = ['datetime', 'day_name']
    # search_fields = ['group']


    # Попытка сделать кнопку
    change_list_template = "admin/shedule_change_form.html"
    
    global data_json
    data_json = '/Users/suslicketeam/Documents/Programming/Python/raspisanie/data.json'
    
    def get_urls(self):
    	# метод обработки url, с подстановкой необходимой view.

        urls = super(TimetableAdmin, self).get_urls()
        custom_urls = [
            path('update/', self.admin_site.admin_view(self.update) )]
        return  custom_urls + urls

    def update(self, request):
        # внутри данного метода (который подставится под запрос url), мы выполним какую-либо логику, и вернем в ответ пользовательский шаблон index.html 
        # update()
        
        with open(data_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
            update_shedule.update_shedule_db(data, entries)
            print(entries)
        
        update_dict = {
            'entries': entries
        }
            
        return render(request, 'timetable/update.html', update_dict)
    
    list_display = ('group', 'day_name', 'datetime')
    
    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

