from email.mime import image

from django.shortcuts import redirect, render

from url_model.forms import StudentForm
from .models import Parson, Student

# Create your views here.
def home(request):
    return render(request,'home.html',{"pers" : Parson.objects.all()})
def about(request):
    return render(request,'about.html')
def form(request):
    return render(request,'form.html')  
def form_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        parson = Parson(name=name, age=age, address=address, image=image)
        parson.save()
    return render(request,'form.html')

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list.html') 
    else:
        form = StudentForm()
    
    return render(request, 'add_student.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


