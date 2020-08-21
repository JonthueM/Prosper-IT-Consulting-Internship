from django.db import models


#
class Games_UpComing(models.Model):
    Game_Name = models.CharField(max_length=250, verbose_name="Game Name")
    Release = models.CharField(max_length=250, verbose_name="Potential Release")
    Main_Console = models.CharField(max_length=250, verbose_name="Main Console")
    Sources =models.CharField(max_length=250, verbose_name="Spy Sources")

    eventModel = models.Manager() # Object manager

    def __str__(self):
        return self.type
