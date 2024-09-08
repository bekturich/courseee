from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Faculty(models.Model):
    name = models.CharField(max_length=44)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=99)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    enrollment_date = models.DateField(null=True, blank=True)
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.faculty}'

class Course(models.Model):
    name = models.CharField(max_length=44)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.code}'

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    building = models.CharField(max_length=99)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.room_number} - {self.building}'

class Timetable(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'MONDAY'),
        ('tuesday', 'TUESDAY'),
        ('wednesday', 'WEDNESDAY'),
        ('thursday', 'THURSDAY'),
        ('friday', 'FRIDAY'),
    ]

    lesson = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    days_of_week = MultiSelectField(choices=DAYS_OF_WEEK, max_choices=2, max_length=20)

    def __str__(self):
        return f'{self.lesson} - {self.classroom} - {self.days_of_week}'

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return f'{self.student} - {self.course}'