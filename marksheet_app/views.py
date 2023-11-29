# marksheet_app/views.py
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def marksheet(request):
    students = Student.objects.all()
    return render(request, 'marksheet_app/marksheet.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marksheet')
    else:
        form = StudentForm()
    return render(request, 'marksheet_app/add_student.html', {'form': form})
