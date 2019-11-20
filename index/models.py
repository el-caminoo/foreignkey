from django.db import models


class school(models.Model):
    name = models.CharField(max_length=22)

    class Meta:
        verbose_name = 'school'
        verbose_name_plural = 'schools'
        ordering = ['name']

    def __str__(self):
        return self.name


class course(models.Model):
    name = models.CharField(max_length=33)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    
class student(models.Model):
    school = models.ForeignKey(school, blank=True, null=True)
    name = models.CharField(max_length=22)

    class Meta:
        ordering = ['name']
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return self.name
