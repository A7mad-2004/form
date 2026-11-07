
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

# Create your models here.
class Cource(models.Model):
    name = models.CharField(max_length=20)
    hours = models.IntegerField()
    def __str__(self):
         return self.name
class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    # relationsheip 1 to 1
    #  blank=True تسمح للحقل بأن يكون فارغاً في النماذج
    choices = models.OneToOneField(Cource, on_delete=models.CASCADE, null=True, blank=True)

class Parson(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()
    image = models.ImageField(upload_to='image/',null=True)
    
    

    # يتخلي الاوبجيكت ينعرض ي اسمو
    def __str__(self):
        return self.name
    
    # بغير اسم الاكلاس في الادمن
    # class Meta:
    #     verbose_name = "Pepole"

    #  2 .  5
    # 23.25145
    # price = models.DecimalField(decimal_places=2,max_digits=5)



    

class Student(models.Model):
    
    name = models.CharField(max_length=100, validators=[
        RegexValidator(r'^[a-zA-Z\u0600-\u06FF\s]+$', 'الاسم يجب أن يحتوي على حروف فقط.')
    ], verbose_name="Full Name")
    
    university_id = models.IntegerField(unique=True, validators=[
        RegexValidator(r'^[12]\d{8}$', 'الرقم الجامعي يجب أن يبدأ بـ 1 أو 2 ويتكون من 9 أرقام.')
    ], verbose_name="University ID")

    national_id = models.IntegerField(validators=[
        RegexValidator(r'^[984]\d{8}$', 'رقم الهوية يجب أن يبدأ بـ 9 أو 8 أو 4 ويتكون من 9 أرقام.')
    ], verbose_name="National ID")

    mobile = models.CharField(max_length=10, validators=[
        RegexValidator(r'^(059|056)\d{7}$', 'رقم الجوال يجب أن يبدأ بـ 059 أو 056 ويتكون من 10 أرقام.')
    ], verbose_name="Mobile Number")
    
    address = models.CharField(max_length=150, verbose_name="Address")
    dob = models.DateField(verbose_name="Date of Birth")
    image = models.ImageField(upload_to='students/', verbose_name="Image")

    def __str__(self):
        return self.name