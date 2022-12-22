from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shedule/group/<str:group_name>/<str:get_date>', views.student_shedule, name='student_shedule'),
    path('shedule/teacher/<str:teacher_name>/<str:get_date>', views.teacher_shedule, name='teacher_shedule'),
    
]
