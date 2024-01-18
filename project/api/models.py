from django.db import models

# Create your models here.

class DepartmentModel(models.Model):
    dep_name = models.CharField(max_length=100,verbose_name='Name')
    description = models.TextField(max_length=200,verbose_name='Desc')
    
    def __str__(self):
        return self.dep_name

class StudentModel(models.Model):
    stu_name=models.CharField(max_length=100,verbose_name='Name')
    stu_class=models.CharField(max_length=100,verbose_name='Class')
    # stu_department=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE,null=True)
    stu_department=models.ForeignKey(DepartmentModel,on_delete=models.PROTECT,null=True)
    stu_email=models.EmailField()
    stu_mobile=models.IntegerField()
    
    def __str__(self):
        return self.stu_name
 
