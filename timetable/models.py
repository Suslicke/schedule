import datetime
from django.db import models
from django.utils import timezone
tz = timezone.get_default_timezone()


# Create your models here.

#Здесь желательно в след. обновление сделать проверку на день недели
class DayOfWeek(models.Model):
    day = models.CharField(max_length=20, primary_key=True)
    
    class Meta:
        verbose_name = ("День недели")
        verbose_name_plural = ("Дни недели")
    
    def __str__(self):
        return f'{str(self.day)}'

    
class Lesson(models.Model):
    lesson = models.CharField(max_length=100, primary_key=True)
    
    class Meta:
        verbose_name = ("Пару")
        verbose_name_plural = ("Пары")
        
    def __str__(self):
        return f'{str(self.lesson)}'
    
    
class Group(models.Model):
    group = models.CharField(max_length=10, primary_key=True)
    
    
    class Meta:
        verbose_name = ("Группа")
        verbose_name_plural = ("Группы")
        
    def __str__(self):
        return f'{str(self.group)}'
    
    
class Teacher(models.Model):
    teacher = models.CharField(max_length=100, primary_key=True)
    
    
    class Meta:
        verbose_name = ("Преподавателя")
        verbose_name_plural = ("Перподаватели")
        
    
    def __str__(self):
        return f'{str(self.teacher)}'
    

class Timetable(models.Model):
    key = models.AutoField(primary_key=True)
    day_name = models.ForeignKey(DayOfWeek, on_delete=models.CASCADE) 
    audience = models.CharField(max_length=10, verbose_name="Номер кабинета")
    lesson_name = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def week_now(self):
        now = tz.now()
        
        return now - datetime.timedelta(days=1) <= self.datetime
        
    
    class Meta:
        verbose_name = ("Расписание")
        verbose_name_plural = ("Расписания")
        
    def __str__(self):
        return f'Дата и Время: {self.astimezone(tz).strftime("%d.%m.%Y %H:%M:%S")} Расписание студентов: {self.group}, {self.day_name}'
        
    
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField()
    

    class Meta:
        verbose_name = ("Новость")
        verbose_name_plural = ("Разработка")
    
    
    def __str__(self):
        return f'Название статьи: {self.title}'
