from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def list_students(request):
    # 1. 先抓取網址傳來的參數 (例如 ?sort=-sid)，如果沒傳，預設用 '-sid'
    sort_by = request.GET.get('sort', '-sid')
    
    # 2. 將變數帶入 order_by 中，不要寫死字串
    students = Student.objects.all().order_by(sort_by) 
    
    return render(request, 'list.html', {'students': students})

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

def edit_student(request, id):
    # 1. 抓取要修改的那位學生資料
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        # 2. 接收表單傳來的新資料並覆蓋舊資料
        student.name = request.POST['name']
        student.sid = request.POST['sid']
        student.email = request.POST['email']
        student.save() # 存回資料庫
        return redirect('list')

    return render(request, 'edit.html', {'student': student})

def delete_student(request, id):
    # 1. 找到那位學生
    student = get_object_or_404(Student, id=id)
    
    # 2. 執行刪除動作
    student.delete()
    
    # 3. 刪除後跳回清單頁面
    return redirect('list')