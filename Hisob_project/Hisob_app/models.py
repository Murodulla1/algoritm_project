from django.db import models

class Shart(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Bajarish(models.Model):
    shart = models.ForeignKey(Shart, on_delete=models.SET_NULL,null=True)
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    result = models.IntegerField()

    def __str__(self):
        return self.shart




