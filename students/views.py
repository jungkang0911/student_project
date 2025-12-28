from django.shortcuts import render, redirect
from .models import Student

def list_students(request):
    # 從資料庫拿所有學生
    data = Student.objects.all()
    return render(request, 'list.html', {'students': data})

def add_student(request):
    if request.method == "POST":
        # 這裡的 name="name" 要跟 HTML 裡的 input name 一樣
        Student.objects.create(
            name=request.POST['name'],
            sid=request.POST['sid'],
            email=request.POST['email']
        )
        return redirect('list') # 存完自動跳轉回清單頁
    return render(request, 'form.html')

def student_detail(request, id):
    # 使用 get(id=id) 抓取特定一筆資料
    student = Student.objects.get(id=id)
    return render(request, 'details.html', {'student': student})

