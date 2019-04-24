from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title       # set how this object defines it self, in this case by the 'title' name

