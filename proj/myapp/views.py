from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        sform = StudentForm()
        return render(request, 'add_student.html', {'form': sform})

