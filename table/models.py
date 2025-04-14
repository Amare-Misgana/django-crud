from django.db import models


class MarkList(models.Model):
    student_name = models.CharField(max_length=50)
    mark = models.IntegerField()

    def __str__(self):
        return f"{self.student_name} - {self.mark}"
