from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=100)
    cal = models.IntegerField()
    # cal = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# class Today(models.Model):
#     fk = models.ForeignKey(
#         Food, on_delete=models.CASCADE, default=10)
#     # names = models.CharField(max_length=100)
#     # cals = models.IntegerField()
#     # name = Food.name

#     def __str__(self):
#         return self.name

#     @property
#     def name(self):
#         return self.fk.name

#     @property
#     def cal(self):
#         return self.fk.cal

class Today(models.Model):
    name = models.CharField(max_length=100, default="-")
    cal = models.IntegerField(default=0)
    # cal = models.CharField(max_length=100)

    def __str__(self):
        return self.name
