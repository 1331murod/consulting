from django.db import models
from django.core.validators import RegexValidator

class UniversityImage(models.Model):
    image = models.ImageField(upload_to="universities/")

class University(models.Model):
    name = models.CharField(max_length=200,verbose_name='univesitet nomi')
    province = models.CharField(max_length=100)
    gallery = models.ManyToManyField(UniversityImage, verbose_name="rasmlar")
    video = models.URLField(null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
class UniversityRequirements(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title
    

class Student(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='toliq ism')
    image = models.ImageField(upload_to="images/") 
    faculty = models.CharField(max_length=100,verbose_name = 'qaysi yonalish')
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, blank=True)  
    opinion = models.TextField(verbose_name='Konsalting haqidagi fikri')
    student_info = models.CharField(max_length=100)
    video = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.full_name}'
    
class Our_advantages(models.Model):
    title =  models.CharField(max_length=100)
    body = models.TextField()
    icon = models.CharField(max_length=50, null=True)
    order = models.PositiveIntegerField(default=1, verbose_name='Tartibi')
    
    def __str__(self):
        return f'{self.title}'
    

class Form(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='toliq ism')
    phone_number = models.CharField(max_length=20,
                                     verbose_name='Telefon raqami')
    message = models.TextField(verbose_name='Xabar')

    
    
    def __str__(self):
        return f'{self.full_name}'