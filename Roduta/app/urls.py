from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('professors/', views.professor_list, name='professor_list'),
    path('professors/create/', views.create_professor, name='create_professor'),
    path('professors/<int:professor_id>/', views.professor_detail, name='professor_detail'),
    path('professors/<int:professor_id>/update/', views.update_professor, name='update_professor'),
    path('professors/<int:professor_id>/delete/', views.delete_professor, name='delete_professor'),

    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.create_subject, name='create_subject'),
    path('subjects/<int:subject_id>/', views.subject_detail, name='subject_detail'),
    path('subjects/<int:subject_id>/update/', views.update_subject, name='update_subject'),
    path('subjects/<int:subject_id>/delete/', views.delete_subject, name='delete_subject'),

    path('student/', views.student_list, name='student_list'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('student/create/', views.create_student, name='create_student'),
    path('student/update/<int:student_id>/', views.update_student, name='update_student'),
    path('student/delete/<int:student_id>/', views.delete_student, name='delete_student'),

    path('schedules/', views.schedule_list, name='schedule_list'),
    path('schedule/<int:pk>/', views.schedule_detail, name='schedule_detail'),
    path('schedule/create/', views.create_schedule, name='create_schedule'),
    path('schedule/update/<int:pk>/', views.update_schedule, name='update_schedule'),
    path('schedule/delete/<int:pk>/', views.delete_schedule, name='delete_schedule'),
    path('schedule_list2/', views.schedule_list2, name='schedule_list2'),

]
