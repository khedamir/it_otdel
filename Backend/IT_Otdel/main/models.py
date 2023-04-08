from django.db import models
from django.conf import settings


class Frame(models.Model):
    MY_CHOICES = (
        ("A" , "A"),
        ("B" , "B"),
        ("C" , "C"),
    )
    name = models.CharField(max_length = 3, choices = MY_CHOICES)
    def __str__(self):
        return self.get_name_display()



class Cabinets(models.Model):
    number = models.CharField(max_length = 3)
    frame = models.ForeignKey(Frame, on_delete = models.CASCADE,blank =True, null=True)
    def frame_name(self):
        return self.frame.name
    def __str__(self):
        return str(self.number)

class Aplications (models.Model):
    author = models.CharField(max_length = 50)
    MY_CHOICES = (
        ("1", "Отсутствует интернет"),
        ("2", "Переферия"),
        ("3", "Архитектура ПК"),
        ("4", "Программное обеспечение"),
        ("5", "Отсутствует интернет"),
        ("6", "другое..."),
    )
    category = models.CharField(max_length = 6, choices=MY_CHOICES)
    comment = models.CharField(max_length = 50)
    date = models.DateField(auto_now_add = True)
    cabinet = models.ForeignKey(Cabinets, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,blank =True, null=True)
    status = models.BooleanField('Выполнено', default=False)

    def cab_name(self):
        return self.cabinet.number

    def frame(self):
        return self.cabinet.frame.name

    def __str__(self):
        return self.author