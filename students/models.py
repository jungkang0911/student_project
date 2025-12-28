from django.db import models

class Student(models.Model):
    # 這就是我們要存進資料庫的欄位
    name = models.CharField(max_length=100)      # 學生姓名
    sid = models.CharField(max_length=20, unique=True) # 學號
    email = models.EmailField()                  # 電子信箱

    def __str__(self):
        return self.name