from django.shortcuts import render, redirect, get_object_or_404
from .models import Schedule, Subject, Professor, Student
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404
from .forms import SubjectForm, ProfessorForm, StudentForm
from django.db import IntegrityError
from django.contrib import messages


def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def base(request):
    return render(request, 'app/base.html')

def schedule_list2(request):
    return render(request, 'app/schedule_list2.html')

# List
def professor_list(request):
    professors = Professor.objects.all()
    return render(request, 'app/professor_list.html', {'professors': professors})


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'app/subject_list.html', {'subjects': subjects})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'app/student_list.html', {'students': students})

def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'app/schedule_list.html', {'schedules': schedules})

def schedule_list2(request):
    schedules = Schedule.objects.all()
    return render(request, 'app/schedule_list2.html', {'schedules': schedules})

# Create
def create_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
        else:
            return render(request, 'app/create_professor.html', {'form': form})


    form = ProfessorForm()
    return render(request, 'app/create_professor.html', {'form': form})

def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'app/create_subject.html', {'form': form})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'app/create_student.html', {'form': form})

def create_schedule(request):
    if request.method == 'POST':
        student = User.objects.get(id=request.POST['student'])
        subject = Subject.objects.get(id=request.POST['subject'])
        professor = Professor.objects.get(id=request.POST['professor'])
        day = request.POST['day']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        Schedule.objects.create(
            student=student,
            subject=subject,
            professor=professor,
            day=day,
            start_time=start_time,
            end_time=end_time
        )
        return redirect('schedule_list')

    students = User.objects.all()
    subjects = Subject.objects.all()
    professors = Professor.objects.all()
    return render(request, 'app/create_schedule.html', {
        'students': students,
        'subjects': subjects,
        'professors': professors,
    })


# Detail
def professor_detail(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)
    return render(request, 'app/professor_detail.html', {'professor': professor})


def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    return render(request, 'app/subject_detail.html', {'subject': subject})


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'app/student_detail.html', {'student': student})

def schedule_detail(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    return render(request, 'app/schedule_detail.html', {'schedule': schedule})

# Update
def update_professor(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm(instance=professor)

    return render(request, 'app/update_professor.html', {'form': form, 'professor': professor})


def update_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)

    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)

    return render(request, 'app/update_subject.html', {'form': form, 'subject': subject})


def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'app/update_student.html', {'form': form})

def update_schedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)

    if request.method == 'POST':
        schedule.student = User.objects.get(id=request.POST['student'])
        schedule.subject = Subject.objects.get(id=request.POST['subject'])
        schedule.professor = Professor.objects.get(id=request.POST['professor'])
        schedule.day = request.POST['day']
        schedule.start_time = request.POST['start_time']
        schedule.end_time = request.POST['end_time']
        schedule.save()
        return redirect('schedule_list2')

    students = User.objects.all()
    subjects = Subject.objects.all()
    professors = Professor.objects.all()

    return render(request, 'app/update_schedule.html', {
        'schedule': schedule,
        'students': students,
        'subjects': subjects,
        'professors': professors,
    })

# Delete
def delete_professor(request, professor_id):

    professor = get_object_or_404(Professor, id=professor_id)

    if request.method == 'POST':

        professor.delete()
        return redirect('professor_list')

    return render(request, 'app/delete_professor.html', {'professor': professor})


def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)

    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')

    return render(request, 'app/delete_subject.html', {'subject': subject})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'app/delete_student.html', {'student': student})

def delete_schedule(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)

    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule_list')

    return render(request, 'app/delete_schedule.html', {'schedule': schedule})


