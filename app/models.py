from django.db import models

# Create your models here.
class Marks(models.Model):
    RollNumber = models.CharField(max_length=8)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    Maths = models.IntegerField()
    Physics = models.IntegerField()
    Chemistry = models.IntegerField()
    Total = models.IntegerField()
    Percentage = models.IntegerField()

    def __str__(self):
        return self.RollNumber

    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'
    
