from django.db import models
from developer.models import Developer


# Create your models here.


class Education(models.Model):
    school = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    _from = models.DateField()
    to = models.DateField(blank=True, null=True)
    gpa = models.CharField(blank=True, max_length=10)
    grade = models.CharField(blank=True, max_length=30)
    # related_name enable backward relation ie Developer.educations
    developer = models.ForeignKey(Developer, related_name='education', on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.school