# marksheet_app/models.py
from django.db import models

class Student(models.Model):
    number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    sub1 = models.FloatField()
    sub2 = models.FloatField()
    sub3 = models.FloatField()
    sub4 = models.FloatField()
    sub5 = models.FloatField()
    sub6 = models.FloatField()

    def calculate_total(self):
        return self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5 + self.sub6

    def calculate_percentage(self):
        return (self.calculate_total() / 600) * 100

    def calculate_result(self):
        percentage = self.calculate_percentage()
        if percentage > 70:
            return 'Distinction'
        elif percentage > 60:
            return 'First class'
        elif percentage > 50:
            return 'Second class'
        elif percentage > 35:
            return 'Pass Class'
        else:
            return 'Fail'
